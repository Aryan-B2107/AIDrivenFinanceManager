# Hare krishna

#python -m pip install cowsay


import cowsay
import sys


from Cs50_0021_sayings import goodbye


if len(sys.argv) == 2:
    # cowsay.cow("hello," + sys.argv[1])
    goodbye(sys.argv[1])