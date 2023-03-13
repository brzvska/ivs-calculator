
# Calculator with GUI
  
## Project 2 from [IVS](https://www.fit.vut.cz/study/course/231042/.en) university course 2022/23

## Introduction

### Task

The task is to create a calculator with basic math operations **(+,-,*,/)**, **factorial**, **exponentiation with natural exponents** (exponents are natural numbers), **common root** (common square root), and one other function.

* The program will consist of a library with mathematical functions (including basic operations such as +,-,* etc.), on top of which a graphical user interface will be built.
* Help message will be part of the user interface
* The program can be controlled by keyboard (minimum basic operations)
* User and program documentation will be supplied with the program
* The user documentation will include, among other things, the **procedure for installing and uninstalling** the program using the installer (uninstaller).
* In addition, instructions will be given for **manual (un)installation**, i.e. the process of compiling from source, creating shortcuts (icons) and other actions performed by the installer.
* The program will be distributed open source under a license [GNU GPL v.1, 2 or 3](https://en.wikipedia.org/wiki/GNU_General_Public_License).

### Additional

* Program documentation must be generated for the mathematical library and the entire program. The preferred tool is [Doxygen](https://www.doxygen.nl/).
* It will include a Makefile for compiling the project, which will contain at least the following goals:
* *all* (translates the project - including the profiling program) - ***use the scripting language to download dependencies***, or choose the option below
* *pack* (packs the project so that it can be submitted)
* *clean* (deletes all files that should not be committed)
* *test* (runs math library tests)
* *doc* (starts the documentation generation)
* *run* (starts the program)
* *profile* (starts the translation of the program to calculate the standard deviation for profiling) - ***if you choose the scripting language, use it to download the dependencies***, or choose the option below   
    
    
* Unless absolutely necessary (e.g. installation paths such as /usr/bin), the Makefile will not contain absolute paths.
* If possible, the Makefile will not contain the name of either source file.
* You ***must*** try debugging on the calculator - you will submit a screenshot of the debugger in the math library.
* A mockup of the user interface of the next version of the calculator will be created (planned for the future), which will support scientific mode, graphing and some other potentially useful function (BMI calculation, stopwatch, statistical functions, ...). Must be clear how the new version will look and work, create more mockups if needed.

## Profilng

Using functions from your math library, the task is to create a program (as a separate executable file) to calculate the [sample standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) from a sequence of numbers that the program reads from standard input (in C, e.g. using the scanf function) to the end of the file and must be able to read ***at least 1000 numbers***. Only numbers separated by whitespace (space, line break or tab) will be on the input and their number is not predefined. Formula for the sampling standard deviation to be used:
$$
s = \sqrt{\frac{1}{N-1}(\sum_{i=1}^N x^2_i - N\overline{x}^2)}
$$$$
\overline{x}^2 = \frac{1}{N}\sum_{i=1}^Nx_i
$$
Profile this program with inputs of 10, 10³ and 10⁶ numeric values. Submit a log containing the profiler output and a brief summary - which places the program spends the most time, and indicate what is best to focus on when optimizing the code.
### Additional
* The program detects the number of input numbers automatically - you must not be required to enter it. 
* The output of the program is only one number - the sample standard deviation - which the program prints to the standard output.
* The program must be able to be compiled using the included Makefile.

## Project structure
```
mockup/
  *.png|jpg|svg|pdf
plan/
profiling/
  vystup.*
  zprava.txt|pdf
src/
  zdrojový kód a testy
  Makefile
  Doxyfile
  zdrojový kód pro profiling
debugging.png|jpg|pdf|txt
dokumentace.pdf
screenshot.png|jpg
skutecnost.txt
hodnoceni.txt
README.md|txt
.gitignore
.editorconfig
```
 