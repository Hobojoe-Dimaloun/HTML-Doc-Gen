# HTML-Doc-Gen

Documentation generator for C projects. The generator works by scraping the header files in the include folder for the functions available to the program. The generator then creates a new html file for each header file, and for each function with the files. The program will scrape any description of the functions from the header and put into a description section of the relevant html files.

## Usage

When running the program it will ask for 3 inputs.
First it will ask for the directory location of the project folder, this should be entered as follows:

C:/.../project

It will then ask for the location of the header files, typically this is a separate folder and should be input as:

/include

Finally it will ask for the location of the output documentation. This can be any directory, however, it is recommended to keep documentation with the project. eg:

C:/.../project/docs

The program will then scrape the function names from each header file, along with any description following the function name.

## Header file formatting

To get maximum worth from the program, it is recommended that each function is given the full description expected to appear in the documentation. Each new description line should start with the // comment signature, not /* .... \*/
