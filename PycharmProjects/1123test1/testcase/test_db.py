import pytest
@pytest.fixture()
def db():
    print('Connection successful')

    yield

    print('Connection closed')


def search_user(user_id):
    d = {
        '001': 'xiaoming'
    }
    return d[user_id]


def test_search(db):
    assert search_user('001') == 'xiaoming'

@pytest.fixture(params=[
    ('redis', '6379'),
    ('elasticsearch', '9200')
])
def param(request):
    return request.param


@pytest.fixture(autouse=True)
def db(param):
    print('\nSucceed to connect %s:%s' % param)

    yield

    print('\nSucceed to close %s:%s' % param)


def test_api():
    assert 1 == 1