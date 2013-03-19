from pip import get_installed_distributions

for d in get_installed_distributions():
    print d.project_name,d.location,d.py_version,d.version
