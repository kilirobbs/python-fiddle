#!/usr/bin/env python
from file import fullpath
from git import Repo

class gitcls(Repo):
    @property
    def status(self):
        """return git status"""
        return self.git.status()

    @property
    def nothing_to_commit(self):
        """return True if nothing to commit"""
        return self.status.find("nothing to commit") > 0

    @property
    def deleted(self):
        """return list of deleted files"""
        return map(lambda d: d.a_blob.path,
                   self.index.diff(None).iter_change_type("D"))

    @property
    def modified(self):
        """return list of modified files"""
        return map(lambda d: d.a_blob.path,
                   self.index.diff(None).iter_change_type("M"))


r=gitcls(fullpath("~/git/python/chrome.py"))
print r.modified

