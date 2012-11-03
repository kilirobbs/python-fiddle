import os

os.chdir("/Users/nordmenss/git/pg_test")
#os.unlink(filename)


old_files = ['OID/2226957', '.DS_Store','OID/2226967']
map(os.unlink,old_files)