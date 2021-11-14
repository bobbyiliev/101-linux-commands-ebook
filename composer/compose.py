import argparse
import inspect
import json
import os
import re
import sys
import yaml
from glob import glob
from typing import List, Tuple, Dict, Union, Any, Optional, Callable, NewType

CONFIG_FILE = "config.yml"

PAT = re.compile(".*(?P<command_id>\d{3})-(?:the-)?(?P<slug>.*)-command.md")
PREFIX = '<strong>'
SUFFIX = '</strong>'
NAV_PATTERN = "<code>{command_id}:&nbsp;{slug}</code>"

SlugmapType = NewType("SlugmapType", Dict[str, Dict[str, str]])
CommandNavsType = NewType("CommandNavsType", List[Dict[str, str]])
NavsDataType = NewType("NavsDataType",
    Dict[str, List[Union[str, Dict[str,
        Union[str, List[Union[str, Dict]]]]]]])


def getcallargs(func: Callable, *args, **kwargs) -> Tuple[Dict, List, str]:
    """Returns a tuple of callargs (dict), d (list of call-args)
    and s (str) to write to a yaml file.

    Example:

        callargs, d, s = getcallargs(generate_nav)
    """
    callargs = inspect.getcallargs(func, *args, **kwargs)
    sig = inspect.signature(func)
    d = []
    for p in sig.parameters.values():
        if p.kind.name in ["POSITIONAL_OR_KEYWORD", "KEYWORD_ONLY"]:
            d.append(dict(name=p.name, dtype=p.annotation, value=p.default))

    s = "generate_nav:\n"
    for e in d:
        q = '"' if e.get('dtype') == str else ''
        s += f'  "{e.get("name")}": {q}{e.get("value")}{q}\n'
    return callargs, d, s

def get_navs_skeleton(
        files: List[str],
        docs_dir: str='../docs',
        command_filename_endswith: str="command.md",
        **kwargs
    ) -> Tuple[SlugmapType, CommandNavsType]:
    """Returns nav skeleton in the form of a list (`command_navs`) and a dict (`slugmap`)."""

    command_navs = []
    slugmap = dict()

    for file in files:
        if file.endswith(command_filename_endswith):
            #slug = PAT.findall(file)[0]
            match = PAT.match(file).groupdict()
            slug = match.get('slug')
            command_id = match.get('command_id')
            slug_label = slug
            parts = slug.split('-')
            if isinstance(parts, list):
                parts = [part.title() if 'introduction' == part else part for part in parts]
                slug = f'{PREFIX}' + f'{SUFFIX}&nbsp;and&nbsp;{PREFIX}'.join(parts) + f'{SUFFIX}'
            path = file.replace(f"{docs_dir}/", "")
            slugmap.update({slug_label: {
                "command_id": command_id,
                "slug": slug,
                "path": path,
                },
            })

            command_navs.append({NAV_PATTERN.format(slug=slug, command_id=command_id): path})

    return slugmap, command_navs

def create_navs_data(command_navs: CommandNavsType, **kwargs) -> NavsDataType:
    """Create the navigational structure for mkdocs.yml as a dict."""

    navs_data = {
        "nav": [
            # Section: Home
            {"<p><i class='fas fa-home'>&nbsp;</i> Home</p>": "index.md"},
            # Section: Commands
            {
                "<p><i class='fas fa-terminal'>&nbsp;</i>Commands</p>": command_navs +
                    [{"Wrap Up": "ebook/en/content/999-wrap-up.md"}],
            },
            # Section: Download
            {
                "<p><i class='fas fa-download'>&nbsp;</i>Download</p>": [
                    {"Download eBook": "download.md"},
                ],
            },
            # Section: About
            {
                "<p><i class='fas fa-info-circle'>&nbsp;</i>About</p>": [
                    {"Info": "about/index.md"},
                    {"License": "about/license.md"},
                ],
            },
        ],
    }

    return navs_data

def generate_nav(
        docs_dir: str='../docs',
        dry_run: bool=False,
        create_slugmap: bool=True,
        ebook_pattern: str="ebook/en/content/*.md",
        command_filename_endswith: str="command.md",
        slugmap_filename: str="slugmap.json",
        command_navs_filename: str="command_navs.yml",
        **kwargs
    ):
    """Generates nav structure from ebook content-files."""

    # Acquire target file names
    files = glob(f'{docs_dir}/{ebook_pattern}')
    files.sort()

    #print(len(files))

    # Generate nav skeleton for commands
    # :: for each "*-command.md" file:
    # - slugmap: a key-value mapping of slug used.
    # - command_navs: a list of key-value mapping of navs.
    slugmap, command_navs = get_navs_skeleton(
        files,
        docs_dir=docs_dir,
        command_filename_endswith=command_filename_endswith,
        **kwargs
    )

    # Write slugmap to a persistent file: 'composer/slugmap.json'
    if create_slugmap:
        with open(f'{docs_dir}/{slugmap_filename}', 'w') as f:
            f.write(json.dumps(slugmap, indent=2))

    # Generate navigation structure for mkdocs.yml
    navs_data = create_navs_data(command_navs, **kwargs)

    # Display/Write to file the navs-struture
    if dry_run:
        # Display
        print(yaml.dump(navs_data, None,
            default_flow_style=False,
            default_style='"',
            indent=2,
        ))
    else:
        # Write to file: 'composer/command_navs.yml'
        with open(f'{docs_dir}/{command_navs_filename}', 'w') as f:
            yaml.dump(navs_data, f,
                default_flow_style=False,
                default_style='"',
                indent=2,
            )

def load_config(config_file: str="config.yml"):
    """Loads in the nav-generation configuration from config
    yaml-file and return a dict.
    """
    cf = f'{config_file}'
    config = {}
    if os.path.isfile(cf):
        with open(cf, 'r') as f:
            config = yaml.safe_load(f)
    return config

def argparser():
    """Parse commandline arguments."""

    # Generate default keyword arguments from
    # the function definition: 'generate_nav()'
    defaultargs, _, s = getcallargs(generate_nav)

    from_where = "from composer/compose.py"
    template_help = "Relative location of {placeholder} " + f"{from_where}."
    parser = argparse.ArgumentParser(
        # prog="compose", # sys.argv[0]
        description='Dynamically generate navigation for documentation.',
        allow_abbrev=True,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=True,
    )
    # Create config_file at default location with
    # default parameters. The parameters are generated
    # from the function definition of 'generate_nav()'.
    if not os.path.isfile(CONFIG_FILE):
        with open(CONFIG_FILE, 'w') as f:
            yaml.dump(s, f,
                default_flow_style=False,
                default_style='"',
                indent=2,
            )
    parser.add_argument(
        "-c", "--config",
        type=str,
        default=CONFIG_FILE,
        # metavar="C",
        help=template_help.format(placeholder="the config file")
    )
    parser.add_argument(
        "-d", "--docs_dir",
        type=str,
        default=defaultargs.get("docs_dir"), # "../docs",
        # metavar="D",
        help=template_help.format(placeholder="docs directory"),
    )
    action_selector = lambda x: f'store_{str(not defaultargs.get(x)).lower()}'
    dry_run_action = action_selector("dry_run")
    parser.add_argument(
        "-r", "--dry_run",
        # when not specified, defaults to False: "store_true"
        action=dry_run_action,  # "store_true",
        help="Print the nav output (without updating any file).",
    )
    create_slugmap_action = action_selector("create_slugmap")
    parser.add_argument(
        "-s", "--create_slugmap",
        # when not specified, defaults to True: "store_false"
        action=create_slugmap_action, # "store_false",
        help="Controls wether to save the slugmap to a file.",
    )
    parser.add_argument(
        "-p", "--ebook_pattern",
        type=str,
        default=defaultargs.get("ebook_pattern"), # "ebook/en/content/*.md",
        # metavar="P",
        help="The glob pattern to choose the chapter markdown files.",
    )
    parser.add_argument(
        "-e", "--command_filename_endswith",
        type=str,
        default=defaultargs.get("command_filename_endswith"),  # "command.md",
        # metavar="E",
        help="The glob pattern to choose the chapter markdown files.",
    )
    parser.add_argument(
        "-S", "--slugmap_filename",
        type=str,
        default=defaultargs.get("slugmap_filename"),  # "slugmap.json",
        # metavar="S",
        help=f"The filename for saving slugmap (w.r.t {from_where}).",
    )
    parser.add_argument(
        "-N", "--command_navs_filename",
        type=str,
        default=defaultargs.get("command_navs_filename"),  # "command_navs.yml",
        # metavar="N",
        help=f"The filename for saving command_navs (w.r.t {from_where}).",
    )

    args = parser.parse_args()

    return args, drop_empty_keys(defaultargs)

def drop_empty_keys(d: Dict) -> Dict:
    for k in list(d.keys()):
        if not d.get(k, {}):
            d.pop(k)
    return d


def main():
    args, defaultargs = argparser()
    print(f'parsed args: {json.dumps(vars(args), indent=2)}')

    # Load configurations from: 'composer/config.yml'
    config = load_config(config_file=args.config)
    delta_config = dict(set(vars(args).items()) - set(defaultargs.items()))

    print(f'delta_config: {json.dumps(delta_config, indent=2)}')

    # Generate nav for mkdocs.yml
    if config:
        conf = config.get("generate_nav", {})
        conf.update(delta_config)
        generate_nav(**conf)
    else:
        generate_nav(**delta_config)

if __name__ == "__main__":
    # NOTE: This file must be run from
    #       within the 'composer/' directory.

    # The parser object collects user specified params
    # NOTE: Priority is as follows (lowest-left TO highest-right).
    # default-args << config.yml args << commandline arg specifications

    main()
