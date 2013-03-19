from ConfigParser import RawConfigParser

config = RawConfigParser()
config.read(None)
config.add_section("s")
config.set("s","k","v")
print config.write(open("ini.ini","w"))