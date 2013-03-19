import cssutils
# https://bitbucket.org/cthedot/cssutils
 
css = u'''/* a comment */ 
     @namespace html "http://www.w3.org/1999/xhtml";
     @variables { BG: #fff }
     html|a { color:red; background: var(BG) }'''
sheet = cssutils.parseString(css)
 
for rule in sheet:
    if rule.type == rule.STYLE_RULE:
        # find property
        for property in rule.style:
            if property.name == 'color':
                property.value = 'green'
                property.priority = 'IMPORTANT'
                break
        # or simply:
        rule.style['margin'] = '01.0eM' # or: ('1em', 'important')
 
sheet.encoding = 'ascii'
sheet.namespaces['xhtml'] = 'http://www.w3.org/1999/xhtml'
sheet.namespaces['atom'] = 'http://www.w3.org/2005/Atom'
sheet.add('atom|title {color: #000000 !important}')
sheet.add('@import "sheets/import.css";')
 
# cssutils.ser.prefs.resolveVariables == True since 0.9.7b2
print sheet.cssText