from appscript import app

terminal = app('Terminal')
print terminal.windows.first.selected_tab().close()