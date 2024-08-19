import pytest


def test_printOne():
    print("This is test One")

def test_prinTwo():
    print("This is test Two")
    assert False,"test Failed"

def test_printThree():
    assert True
