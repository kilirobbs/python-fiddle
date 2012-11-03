#! /usr/bin/python

import lxml.html

doc = lxml.html.document_fromstring("""<html>
 <body>
   <span class="simple_text">One</span> text</br>
   <span class="cyrillic_text">Second</span> text</br>
 </body>
</html>
""")