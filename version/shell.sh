#!/bin/sh
python -c 'import platform; print platform.python_version()'
python -c 'import sys; print sys.version_info[0]'
python -c 'import sys; print sys.version_info[1]'
python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))'