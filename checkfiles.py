#!/usr/local/bin python

"""This script processes all latex files to ensure diff comparisons
are carried out in the correct files.

"""
import os
import subprocess

ignored_files = ['IEEEcsmag.cls', 'IEEEtran.bst', 'IEEEtran.cls', 'IEEEtranS.bst',
    'README', 'main.bib', 'main.tex', 'main-diff.tex', 'mlopsv1.zip', 'mlopsv2.zip', '.DS_Store']
folders = ['sections', 'tables']

old_ver = 'mlops_v2' #'mlopsv1'
new_ver = 'mlops_v3'

def test_function():
    """
    Test the execution of the tool
    """
    print('>> {}'.format(test_function.__name__))
    cmd = './latexdiff/latexdiff latexdiff/example/example-draft.tex latexdiff/example/example-rev.tex > latexdiff/example/example-diff.tex'
    subprocess.run(cmd, shell=True)

def is_file_dir_ignored(item):
    if item in ignored_files or item in ignore_folders:
        return True
    else:
        return False

def command(dir, file):
    """
    Create a command to execute
    """
    tool = './latexdiff/latexdiff '
    arg1 = f'manuscript/{old_ver}/{dir}/{file}'#.format(dir, file)
    arg2 = f' manuscript/{new_ver}/{dir}/{file}'#.format(dir, file)
    output = f' > manuscript/mlopsdiff/{dir}/{file}'#.format(dir, file)
    return tool + arg1 + arg2 + output

def process_files():
    """
    Check all files and conduct differences.
    """
    print('>> {}'.format(process_files.__name__))
    v1 = f'./manuscript/{old_ver}/'
    v2 = f'./manuscript/{new_ver}/'
    for dir in os.listdir(f'./manuscript/{old_ver}'):
        if os.path.isdir(v1 + dir) and os.path.isdir(v2 + dir) and dir in folders:
            for file in os.listdir(f'./manuscript/{new_ver}/' + dir):
                print('{}:{}'.format(dir, file))
                cmd = command(dir, file)
                subprocess.run(cmd, shell=True)

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
    test_function()
    process_files()
    process_standalone_files()
