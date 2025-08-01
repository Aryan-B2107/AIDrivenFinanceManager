# Hare krishna

import pytest

from Cs50_0003_definition import hello

def test_default():
    assert hello("Aayush") == "hello, Aayush"
    
    
def test_argument():
    assert hello() == "hello, world"