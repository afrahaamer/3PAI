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
 <body>
   <h1>Form Page</h1>

   <form method=GET>
    <fieldset>
   <legend>SAMPLE FORM</legend>
   <ul>
    <li>First Name: <input name='first'></li>
    <li>Last Name:  <input name='last'></li>
   </ul>
   <input type='submit' value='Submit Form'>
   </fieldset>
   </form>

 </body>
</html>""")
f.close()

webbrowser.open_new_tab('lms.html')