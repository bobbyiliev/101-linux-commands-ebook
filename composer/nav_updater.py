import os
from shutil import copyfile

mkdocs_file = "../mkdocs.yml"
mkdocs_genfile = "mkdocs_gen.yml"
mkdocs_backupfile = "mkdocs.yml.bkp"
generated_navs_file = '../docs/command_navs.yml'

lines = open(mkdocs_file, "r").readlines()

begin_nav, end_nav = 0, 0

for idx, line in enumerate(lines):
    if line.startswith("## @@ Begin NAVIGATION"):
        begin_nav = idx
    elif line.startswith("## @@ End NAVIGATION"):
        end_nav = idx

print(f'''
Summary for Existing mkdocs.yml:
    total lines: {len(lines)}
    begin_nav: {begin_nav+1}
    end_nav: {end_nav+1}
''')

print("1. Generating file with fresh nav content at: \n'composer/mkdocs_gen.yml'...")
if os.path.isfile(generated_navs_file):
    with open(mkdocs_genfile, 'w') as f:
        f.writelines(
            lines[:begin_nav+1] + ['\n', ]
            + open(generated_navs_file, 'r').readlines()
            + ['\n', ] + lines[end_nav:]
        )
    if os.path.isfile(mkdocs_genfile):
        print(f"2. Backing up existing mkdocs.yml file at location: \n'./composer/{mkdocs_backupfile}'...")
        copyfile(mkdocs_file, mkdocs_backupfile)
        print("3. Replacing old mkdocs file with fresh nav content...")
        copyfile(mkdocs_genfile, mkdocs_file)
    else:
        print(
            f"WARNING!!! The generated-mkdocs-file is missing: {mkdocs_genfile}. \n>>> SKIP UPDATING mkdocs.yml.")
else:
    print(
        f"WARNING!!! The generated-navs-file is missing: {generated_navs_file}. \n>>> SKIP UPDATING mkdocs.yml.")
