import pytest
import haha.haha_file as hf


def test_01():
    print("this is {} testcase".format(__name__))

def test_hahaha():
    assert hf.haha_add(1,2) ==3


if __name__=='__main__':
    pytest.main()