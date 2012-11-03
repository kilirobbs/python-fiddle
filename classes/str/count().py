schema_path="schema/schemaname.sql"

table_path="schema/schemaname/table/tablename.sql"

index_path="schema/schemaname/table/tablename/index/indexname.sql"

def level(path):
	return (path.count("/")+1) / 2

print schema_path.count("/"), level(schema_path)
print table_path.count("/"), level(table_path)
print index_path.count("/"), level(index_path)