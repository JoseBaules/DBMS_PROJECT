#!/usr/bin/env python

import subprocess
import cgi

def run():
    form = cgi.FieldStorage()
    major = form.getfirst('Smajor', '')
    result = subprocess.check_output(['python3', 'viewStudents.py', major], universal_newlines=True)    
    
    print(result)

if __name__ == '__main__':
    try:
        # Tell the browser it's an HTML page.
        print('Content-Type: text/html')
        # Blank line to indicate end of headers.
        print('')
        # Main program.
        run()
    except:
        cgi.print_exception()
