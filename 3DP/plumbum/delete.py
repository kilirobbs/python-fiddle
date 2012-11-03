from plumbum import local
from plumbum.cmd import wc, ls, echo, grep
from plumbum.utils import copy, delete

delete(local.cwd // "*/*.pyc")