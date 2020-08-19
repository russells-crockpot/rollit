"""
"""
import os.path
import sys

parent_dir = os.path.dirname(os.path.dirname(__file__))
# make sure that the chital source directory is first on the list
sys.path.insert(0, os.path.join(parent_dir, 'src'))
