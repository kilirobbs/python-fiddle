import os

path = "schema/public/table/tablename/index/indexname"
dirname = os.path.dirname(path)
print dirname

print dirname.split("/")[-1]