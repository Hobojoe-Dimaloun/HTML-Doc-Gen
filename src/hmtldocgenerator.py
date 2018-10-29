
import glob
import os
import markdown
#
# C documentation generator
#
print("C documentation generator. Creates function documentation from header files (.h)")
#
# get project path
#
projectPath = input('Input project directory:\n')
#
# get location of headers in project
#
includePath = projectPath + input("Input header file folder:\n")
#
# Get output path
#
output = input("Input documentation output location:\n")
#
# create Project Description File
#
project = projectPath.split('/')[-1]
#
# Open top file
#
with open(output + project +'.html','w') as projectFileHtml:
	#
	# Add Titles to top file
	#
	projectFileHtml.write(markdown.markdown('#' + project) + '\n\n')
	projectFileHtml.write(markdown.markdown('## Headers' + '\n\n'))
	#
	# Cycle through and parse files
	#
	for filename in glob.glob(os.path.join(includePath,'*.h')):
		print(filename)
		#
		# Parse header name to write to top file
		#
		headerFile = filename.replace(includePath + '\\','')
		headerFilelink = headerFile.replace('.h','')
		linking = markdown.markdown( '* [' + headerFile + '](' +headerFilelink + '.html)') + '\n\n'
		projectFileHtml.write(linking)
		#
		# Open file
		#
		with open(filename, 'r') as fileContent:
			#
			# Create headerfile html doc
			#
			headFileHtml = open(output + headerFilelink + '.html','w')
			headFileHtml.write(markdown.markdown('#' + headerFile) + '\n\n')
			#
			# Read in line by line
			#
			creation = False
			pretext = ''
			change = 0
			for line in fileContent:
				#
				# Check if the line contains a function definition
				#
				if '(' in line and ')' in line and ';' and '//' not in line:
					if change == 0:
						headFileHtml.write(pretext)
						change = 1

					#
					# Check if already parsing a function. If yes end parsing, write to file and start new
					#
					if creation == False:
						creation = True
					else:
						creation = False
						with open(htmlFileName, 'w') as htmlFile:
							htmlFile.write(text)
							htmlFile.write(markdown.markdown( '[' + headerFile + '](' +headerFilelink + '.html)'))
					#
					# strip function until only function name remains
					#
					function = line
					htmlname = function.split('(',1)[0]
					htmlname = htmlname.split(' ',1)[1]

					if '*' in htmlname:
						htmlname = htmlname.replace('*','')
						#function = function.replace('*','\*')
					if ' ' in htmlname:
						htmlname = htmlname.replace(' ','')
					#
					# Create new function file
					#
					htmlFileName = output + htmlname + '.html'
					#
					# Add html and Syntax to file for documentation
					#
					text = markdown.markdown('#' + htmlname) + '\n\n'# File name header
					text = text + markdown.markdown('## Header') + '\n\n'# Header header
					text = text + '#include "' + headerFile + '"\n\n' #Header file
					text = text + markdown.markdown('## Syntax') + '\n\n' # Syntax header
					text = text + function + '\n' # Syntax of function
					text = text + markdown.markdown('## Description') + '\n\n' # Description header
					#
					# Create a function link in header file
					#
					headFileHtml.write(markdown.markdown('* [' + htmlname + '](' + htmlname + '.html)') + '\n\n')
					#
					# Indicate that a new function has been started
					#
					creation = True
<<<<<<< HEAD
=======

				#
				# If // found, description of function reached. Print description to file and carry on parsing
				#
				if '//' in line:
					if creation == False:
						temp = line.replace('//','')
						temp = temp.replace('<',' &#60 ')
						temp = temp.replace('>',' &#62 ')
						temp = temp.replace('|',' &#8739 ')
						temp = temp
						pretext = pretext + temp +'<br>'
					else:
						text = text + line.replace('//','')  +'<br>'
>>>>>>> cb27c59928d17a1410805df58c75aec9ad21ea47
				#
				# If file definition is found, end of header reached. End current function parsing
				#
				if '_H' in line and creation == True:
					creation = False
					with open(htmlFileName, 'w') as htmlFile:
						htmlFile.write(text)
<<<<<<< HEAD
						htmlFile.write(markdown.markdown( '[' + headerFile + '](' +headerFilelink + '.html)'))
					break
				#
				# If // found, description of function reached. Print description to file and carry on parsing
				#
				if '//' in line:
					if creation == False:
						temp = line.replace('//','')
						temp = temp.replace('<',' &#60 ')
						temp = temp.replace('>',' &#62 ')
						temp = temp.replace('|',' &#8739 ')
						temp = temp
						pretext = pretext + temp +'<br>'
					else:
						text = text + line.replace('//','')  +'<br>'

			headFileHtml.write(markdown.markdown( '[' + project + '](' + project + '.html)'))
=======
>>>>>>> cb27c59928d17a1410805df58c75aec9ad21ea47
