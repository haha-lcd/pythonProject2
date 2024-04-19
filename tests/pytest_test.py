import pytest

def test_01():
    print("this is {} testcase".format(__name__))

def test_hahaha():
    assert 1 == 1

if __name__=='__main__':
    pytest.main()