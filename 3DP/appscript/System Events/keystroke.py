from appscript import *
appscript.app('System Events').keystroke(key ,using=[k.command_down])
print app('System Events').processes[its.name == 'iTunes'].count()