#!/usr/bin/env python

import re
import sys

#input_file = sys.argv[1]
input_file = '_build/latex/book.tex'
output_file =input_file[:-4] + '_modified.tex'

with open(input_file, 'r') as old_file, open(output_file, 'w') as new_file:

    counter = 1
    for line in old_file:
        if counter == 32:
            new_file.write(r'\setcounter{secnumdepth}{0}' + '\n')
            
        if line.startswith(r'\chapter{'):
            pattern = r'\\chapter\{([\{\}\\&:\s\d\w]+)\}'
            new = re.findall(pattern, line)

            new_file.write(r'\chapter*{' + new[0] +  '}\n')
            new_file.write(r'\addcontentsline{toc}{chapter}{' + new[0] + '} \n')

        else:
            new_file.write(line)

        counter += 1