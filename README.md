# HTML-Doc-Gen

C documentation generator.

<<<<<<< HEAD
## Usage
=======
##Usage
>>>>>>> 64eba7f36d5f1fa62dc2065ccc1c6bf4a4bba0ed

When running the program it will ask for 3 inputs.
First it will ask for the directory location of the project folder, this should be entered as follows:

C:/.../project

It will then ask for the location of the header files, typically this is a separate folder and should be input as:

/include

Finally it will ask for the location of the output documentation. This can be any directory, however, it is recommended to keep documentation with the project. eg:

C:/.../project/docs

The program will then scrap the function names from each header file, along with any description following the function name.

<<<<<<< HEAD
## Header file formatting
=======
##Header file formatting
>>>>>>> 64eba7f36d5f1fa62dc2065ccc1c6bf4a4bba0ed

To get maximum worth from the program, it is recommended that each function is given the full description expected to appear in the documentation. Each new description line should start with the // comment signature, not /* .... \*/
