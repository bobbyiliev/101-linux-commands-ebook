import os
import sys
from glob import glob
from parse import parse
import json
import re
import yaml
import argparse

PAT = re.compile(".*(?P<command_id>\d{3})-(?:the-)?(?P<slug>.*)-command.md")
PREFIX = '<strong>'
SUFFIX = '</strong>'
NAV_PATTERN = "<code>{command_id}:&nbsp;{slug}</code>"

# docs_dir = "../docs"
# files = glob(f'{docs_dir}/ebook/en/content/*.md')
# files.sort()
#print(files)

def generate_nav(docs_dir: str='../docs', dry_run: bool=False, create_slugmap: bool=True, ebook_pattern: str="ebook/en/content/*.md"):

    files = glob(f'{docs_dir}/{ebook_pattern}')
    files.sort()
    command_navs = []
    slugmap = dict()
    #print(len(files))

    for file in files:
        if file.endswith("command.md"):
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

    if create_slugmap:
        with open(f'{docs_dir}/slugmap.json', 'w') as f:
            f.write(json.dumps(slugmap, indent=2))

    navs_data = {"nav": [
        {"<p><i class='fas fa-home'>&nbsp;</i> Home</p>": "index.md"},
        {
            "<p><i class='fas fa-terminal'>&nbsp;</i>Commands</p>": command_navs +
                [{"Wrap Up": "ebook/en/content/999-wrap-up.md"}],
        },
        {
            "<p><i class='fas fa-info-circle'>&nbsp;</i>About</p>": [
                {"Info": "about/index.md"},
                {"License": "about/license.md"},
            ],
        },
    ]}

    if dry_run:
        yaml.dump(navs_data, None,
                  default_flow_style=False,
                  default_style='"',
                  indent=2,
                  )
    else:
        with open(f'{docs_dir}/command_navs.yml', 'w') as f:
            yaml.dump(navs_data, f,
                default_flow_style=False,
                default_style='"',
                indent=2,
            )

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Dynamically generate navigation for documentation.')
    generate_nav()
