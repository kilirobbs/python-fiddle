from ConfigParser import RawConfigParser

config = RawConfigParser()
print config.sections()
try:
    config.add_section("s")
except:
    print "sections unique :)"
config.set("s","k","v")
print config.options('s')