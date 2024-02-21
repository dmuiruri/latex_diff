#!/usr/local/bin python

"""This script processes all latex files to ensure diff comparisons
are carried out in the correct files.

"""
import os
import subprocess
import argparse
import json

parser = argparse.ArgumentParser(prog='Process latex files',
                                 description='This script is used to generate differences between two versions of manuscripts. \
                                    The changes are shown in different colors. The two versions of the manuscript must be placed \
                                    must be placed in the manuscript folder. The script should be run from the root directory.',
                                 epilog='Some parameters must be adjusted in the config file for the script to work.')
parser.add_argument('version1', help='Provide directory name containining first version for comparison')
parser.add_argument('version2', help='Provide directory name containining second version for comparison')
args = parser.parse_args()

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
ignored_files = config["ignored_files"]
ignored_folders = config["ignored_dirs"]
dirs = config["dirs"]

def test_function():
    """
    Test the execution of the tool
    """
    print('>> {}'.format(test_function.__name__))
    cmd = './latexdiff/latexdiff latexdiff/example/example-draft.tex latexdiff/example/example-rev.tex > latexdiff/example/example-diff.tex'
    subprocess.run(cmd, shell=True)

def process_files(version1, version2):
    """
    Check all files and conduct differences.

    version1: directory containing older version
    version2: directory containing updated version
    """
    print('>> {}'.format(process_files.__name__))
    v1 = f"./manuscript/{version1}/"
    v2 = f"./manuscript/{version2}/"
    tool = "./latexdiff/latexdiff "
    # first process files in the root folder then walk through the directories
    for f in os.listdir(f'{v1}'):
        fp = os.path.join(f'{v2}', f)
        if os.path.isfile(fp) and f not in ignored_files:
                print(f'>> {v1}/{f}')
                arg1 = f"{v1}/{f} "
                arg2 = f"{v2}/{f} "
                output = f"> manuscript/diff/{f} "
                subprocess.run(tool + arg1 + arg2 + output, shell=True)
        else:
            dirpath = os.path.join(v1, f)
            if os.path.isdir(f"{dirpath}"):
                if os.path.isdir(v1 + f) and os.path.isdir(v2 + f) and f in dirs:
                    print(os.path.isdir(v1 + f))
                    for file in os.listdir(v2 + f):
                        print(f"{v2}{f}/{file}")
                        tool = "./latexdiff/latexdiff "
                        arg1 = f"{v1}{f}/{file} "
                        arg2 = f"{v2}{f}/{file} "
                        output = f"> manuscript/diff/{f}/{file}"
                        subprocess.run(f"mkdir -p manuscript/diff/{f} && " + tool + arg1 + arg2 + output, shell=True)

def process_standalone_files():
        """
        Process standalone files in the project's root folder
        """
        files = ['main.bib', 'main.tex']
        tool = './latexdiff/latexdiff '
        print('>> {}'.format(process_standalone_files.__name__))
        tool = './latexdiff/latexdiff '
        for f in files:
            cmd = tool + f'manuscript/{old_ver}/{f} manuscript/{new_ver}/{f} > manuscript/mlopsdiff/{f}'
#            cmd = tool + f'manuscript/{old_ver}/{} manuscript/{new_ver}/{} > manuscript/mlopsdiff/{}'.format(f, f, f)
            subprocess.run(cmd, shell=True)

if __name__ == '__main__':
    # test_function()
    # parse these as command line arguments
    old_ver = args.version1
    new_ver = args.version2

    process_files(old_ver, new_ver)
    # process_standalone_files()
