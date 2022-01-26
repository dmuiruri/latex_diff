#!/usr/local/bin python

"""This script processes all latex files to ensure diff comparisons
are carried out in the correct files.

"""
import os
import subprocess

ignored_files = ['IEEEcsmag.cls', 'IEEEtran.bst', 'IEEEtran.cls', 'IEEEtranS.bst',
    'README', 'main.bib', 'main.tex', 'main-diff.tex', 'mlopsv1.zip', 'mlopsv2.zip', '.DS_Store']
folders = ['sections', 'tables']

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
    arg1 = 'manuscript/mlopsv1/{}/{} '.format(dir, file)
    arg2 = 'manuscript/mlopsv2/{}/{} '.format(dir, file)
    output = '> manuscript/mlopsdiff/{}/{}'.format(dir, file)
    return tool + arg1 + arg2 + output

def process_files():
    """
    Check all files and conduct differences.
    """
    print('>> {}'.format(process_files.__name__))
    v1 = './manuscript/mlopsv1/{}'
    v2 = './manuscript/mlopsv2/{}'
    for dir in os.listdir('./manuscript/mlopsv1'):
        if os.path.isdir(v1.format(dir)) and os.path.isdir(v2.format(dir)) and dir in folders:
            for file in os.listdir('./manuscript/mlopsv2/{}'.format(dir)):
                print('{}:{}'.format(dir, file))
                cmd = command(dir, file)
                subprocess.run(cmd, shell=True)

def process_references():
        """
        Process references
        """
        print('>> {}'.format(process_references.__name__))
        tool = './latexdiff/latexdiff '
        arg1 = 'manuscript/mlopsv1/main.bib '
        arg2 = 'manuscript/mlopsv2/main.bib '
        output = '> manuscript/mlopsdiff/main.bib'
        cmd = tool + arg1 + arg2 + output
        subprocess.run(cmd, shell=True)

def process_main():
        """
        Process main file
        """
        print('>> {}'.format(process_main.__name__))
        tool = './latexdiff/latexdiff '
        arg1 = 'manuscript/mlopsv1/main.tex '
        arg2 = 'manuscript/mlopsv2/main.tex '
        output = '> manuscript/mlopsdiff/main.tex'
        cmd = tool + arg1 + arg2 + output
        subprocess.run(cmd, shell=True)

if __name__ == '__main__':
    test_function()
    process_files()
    process_main()
    process_references()
