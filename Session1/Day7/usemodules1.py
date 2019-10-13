import sys
sys.path.append('C:\\LordKrishna\\GitHub\\LearningPython_2019\\Session1\\CustomModules')

import bannermodule

program_title = 'Using Modules'
top_header = '='
bottom_header = '-'
function_footer = '+'
count = 50

bannermodule.create_banner('Addition of Numbers', top_header, bottom_header, count)
print("Hello World")


