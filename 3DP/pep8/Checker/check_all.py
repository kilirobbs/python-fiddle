from pep8 import Checker

checker = Checker('test2.py', show_source=False)
file_errors = checker.check_all()
print file_errors