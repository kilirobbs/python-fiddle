#!/usr/bin/env python
        return map(lambda d: d.a_blob.path,
                   self.repo.index.diff(None).iter_change_type("M"))
