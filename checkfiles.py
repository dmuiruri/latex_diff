#!/usr/local/bin python

"""This script processes all latex files to ensure diff comparisons
are carried out in the correct files.

"""
import os
import sys
import subprocess

ignore_files = ['IEEEcsmag.cls', 'IEEEtran.bst', 'IEEEtran.cls', 'IEEEtranS.bst', 'README', 'main.bib', 'main.tex']
ignore_folders = ['images', 'sections', 'tables']

def test_function():
    """
    Test the execution of the tool
    """
    cmd = './latexdiff/latexdiff latexdiff/example/example-draft.tex latexdiff/example/example-rev.tex > latexdiff/example/example-diff.tex'
    subprocess.run(cmd, shell=True)

def process_files():
    """
    Check all files and conduct differences.
    """

    for item in os.listdir():
        if os.isfile(item):
            # check diff
            subprocess.call(['./latexdiff/latexdiff', 'manuscript/mlopsv1/'.format(item), ''], shell=True) #using the call() function
        if os.isdir(item):
            for files in os.listdir(item):
                subprocess.call(['./latexdiff/latexdiff', 'manuscript/mlopsv1/'.format(item), ''], shell=True) #using the call() function

if __name__ == '__main__':
    test_function()
