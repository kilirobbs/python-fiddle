#!/usr/bin/env python
import fnmatch

def files_with_pattern(directory, pattern='*'):
    result = []
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                result.append(filename)
    return result