#!/usr/bin/env python

import subprocess
import cgi



def run():
    form = cgi.FieldStorage()

    StudentId = form.getfirst('StudentId', '')


    result = subprocess.call(['python3', 'addApplication.py', StudentId])

    
if __name__ == '__main__':
    try:
        
        # Main program.
        run()
    except:
        cgi.print_exception()
