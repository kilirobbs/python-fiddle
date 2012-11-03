from nose.tools import eq_

answer = 43


def test_answer():
    eq_(answer, 42)


if __name__ == "__main__":
    test_answer()