#!/usr/local/bin python

"""This script processes all latex files to ensure diff comparisons
are carried out in the correct files.

"""
import os
import subprocess

ignored_files = ['IEEEcsmag.cls', 'IEEEtran.bst', 'IEEEtran.cls', 'IEEEtranS.bst','README.md', 'main.bib',
                 'main-diff.tex', 'mlopsv1.zip', 'mlopsv2.zip', '.DS_Store', 'references.bib', 'acmart.cls']

ignored_folders = ['images']

folders = ['sections', 'tables', 'cases'] # folders to be processed

old_ver = 'deployment_v1'
new_ver = 'deployment_v2'

def test_function():
    """
    Test the execution of the tool
    """
    print('>> {}'.format(test_function.__name__))
    cmd = './latexdiff/latexdiff latexdiff/example/example-draft.tex latexdiff/example/example-rev.tex > latexdiff/example/example-diff.tex'
    subprocess.run(cmd, shell=True)

def command(dir, file):
    """
    Create a command to execute
    """
    tool = "./latexdiff/latexdiff"
    arg1 = f"manuscript/{old_ver}/{dir}/{file}"
    arg2 = f"manuscript/{new_ver}/{dir}/{file}"
    output = f"> manuscript/diff/{dir}/{file}"
    return tool + arg1 + arg2 + output

def process_files():
    """
    Check all files and conduct differences.
    """
    print('>> {}'.format(process_files.__name__))
    v1 = f"./manuscript/{old_ver}/"
    v2 = f"./manuscript/{new_ver}/"
    tool = "./latexdiff/latexdiff "
    # first process files in the root folder then walk through the directories
    for f in os.listdir(f'./manuscript/{old_ver}'):
        fp = os.path.join(f'./manuscript/{old_ver}', f)
        if os.path.isfile(fp) and f not in ignored_files:
                print(f'>> {v1}/{f}')
                arg1 = f"{v1}/{f} "
                arg2 = f"{v2}/{f} "
                output = f"> manuscript/diff/{f} "
                subprocess.run(tool + arg1 + arg2 + output, shell=True)
        else:
            dirpath = os.path.join(v1, f)
            if os.path.isdir(f"{dirpath}"):
                if os.path.isdir(v1 + f) and os.path.isdir(v2 + f) and f in folders:
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
    process_files()
    # process_standalone_files()
