from git import *
import subprocess

process = subprocess.Popen("/usr/bin/git rev-parse --show-toplevel",\
stdout=subprocess.PIPE,\
stdin=subprocess.PIPE,\
stderr=subprocess.STDOUT,\
shell=True)
result=process.communicate()
print result
if process.returncode==0:
	repodir = result[0].strip()
	repo 	= Repo(repodir)
	writer  = repo.config_writer()
	#writer  = repo.config_writer(config_level="repository")
	#writer  = repo.config_writer(config_level="global")
	#writer  = repo.config_writer(config_level="system")
	writer.set_value("sectionname", "key", "value") # without _ !!!
	reader 	= repo.config_reader()
	value   = reader.get("sectionname", "key")
	print value