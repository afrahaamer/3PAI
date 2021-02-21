# write-html-2-windows.py

import webbrowser

f = open('lms.html','w')
'''
message = """<html>
<head></head>
<body><p>Hello World!</p></body>
</html>"""
'''

f.write("""<html>
<head></head>
<body><p>Hello World!</p></body>
</html>""")
f.close()

webbrowser.open_new_tab('lms.html')