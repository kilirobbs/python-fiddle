from nose import main # exit on error
from nose import run # not exit on error

from coverage import coverage
from os import getcwd
cov = coverage(
    branch=True,
    cover_pylib=False,
    source=[getcwd()]
)
cov.erase()
cov.start()
run()
cov.save()
cov.html_report(directory='htmlcov')