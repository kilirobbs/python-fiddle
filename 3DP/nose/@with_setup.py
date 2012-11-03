from nose.tools import assert_equal, with_setup

answer = 42


def setup_func():
    print('setup')


def teardown_func():
    print('teardown')


@with_setup(setup_func, teardown_func)
def test_answer():
    assert_equal(answer, 42)