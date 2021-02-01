#! python3

import os

text_color = '02'
with open('matrix.bat','w') as file:
	file.write('@echo off\n')
	file.write(f'color {text_color}\n')
	file.write(':a \n')
	file.write(f"echo {'%random%' * 20}\n")
	file.write('goto a')

os.system('matrix.bat')