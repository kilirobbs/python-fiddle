import os
import sys
from git.config import GitConfigParser

# stolen from gitpython/repo/base.py

def _get_config_path(config_level="global"):
    if sys.platform == "win32" and config_level == "system":
        config_level = "global"

    if config_level == "system":
        return "/etc/gitconfig"
    elif config_level == "global":
        return os.path.normpath(os.path.expanduser("~/.gitconfig"))

        raise ValueError("Invalid configuration level: %r" % config_level)

files = _get_config_path()
config = GitConfigParser(files, read_only=True)
print config.get("user", "name")
