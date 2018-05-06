
import glob
import os
import markdown
#
# get project path
#
projectPath = input('Input project directory:\n')
#
# get location of headers in project
#
includePath = projectPath + input("Input header file folder:\n")
#
# Create Project Description File
#
project = projectPath.split('/')[-1]

projectFileHtml = open('../docs/' + project +'.html','w')

linking = markdown.markdown('#' + project + '\n\n')

projectFileHtml.write(markdown.markdown('#' + project) + '\n\n')
projectFileHtml.write(markdown.markdown('## Headers' + '\n\n'))

for filename in glob.glob(os.path.join(includePath,'*.h')):
	print(filename)
	#
	# Open file
	#
	headerFile = filename.replace(includePath + '\\','')
	headerFilelink = headerFile.replace('.h','')
	linking = markdown.markdown( '* [' + headerFile + '](' +headerFilelink + '.html)') + '\n\n'
	projectFileHtml.write(linking)
	with open(filename, 'r') as fileContent:
		#
		# Create headerfile html doc
		#
		headFileHtml = open('../docs/' + headerFilelink + '.html','w')
		headFileHtml.write(markdown.markdown('#' + headerFile) + '\n\n')
		#
		# Read in line by line
		#
		creation = False

		for line in fileContent:
			#
			# Parse lines to pull out critical data
			#
			if '(' in line and ')' in line:
				if creation == False:
					creation = True
				else:
					creation = False
					with open(htmlFileName, 'w') as htmlFile:
						htmlFile.write(text)

				function = line
				htmlname = function.split('(',1)[0]
				htmlname = htmlname.split(' ',1)[1]

				if '*' in htmlname:
					htmlname = htmlname.replace('*','')
					function = function.replace('*','\*')
				if ' ' in htmlname:
					htmlname = htmlname.replace(' ','')

				htmlFileName = '../docs/' + htmlname + '.html'
				#with open(htmlFileName,'w') as htmlFile:

				text = markdown.markdown('#' + htmlname) + '\n\n'# File name header
				text = text + markdown.markdown('## Header') + '\n\n'# Header header
				text = text + '#include "' + headerFile + '"\n\n' #Header file
				text = text + markdown.markdown('## Syntax') + '\n\n' # Syntax header
				text = text + function + '\n' # Syntax of function
				text = text + markdown.markdown('## Description') + '\n\n' # Description header

				headFileHtml.write(markdown.markdown('* [' + htmlname + '](' + htmlname + '.html)') + '\n\n')
				creation = True ;
			if '_H' in line and creation == True:
				creation = False
				with open(htmlFileName, 'w') as htmlFile:
					htmlFile.write(text)
			if '//' in line:
				text = text + line.replace('//','')


#
# Parse the file for functions
#

#
# Generate documentation
#
