import pytest


@pytest.mark.finished
def test_func1():
    assert 1 == 1


@pytest.mark.unfinished
def test_func2():
    assert 1 != 1


@pytest.mark.skip
def test_func2():
    assert 1 != 1


@pytest.mark.skipif(pytest.__version__ < '6.2.0', reason='not supported until v7.2.0')
def test_api():
    pass


@pytest.mark.xfail(pytest.__version__ < '0.2.0',
                   reason='not supported until v0.2.0')
def test_api():
    id_1 = pytest.unique_id()
    id_2 = pytest.unique_id()
    assert id_1 != id_2
