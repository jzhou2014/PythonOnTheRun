## Installing PyCharm
### Installing Python
In order to be able to run Python programs on your computer, you need to install a Python Interpreter. An interpreter is a program that is capable of reading a .py file that you have written, and translating the Python code in that file to instructions that your computer can easily execute. Begin by downloading Python:

[Mac Installer](https://www.python.org/ftp/python/3.10.10/python-3.10.10-macos11.pkg)

[Windows 64-bit installer](https://www.python.org/ftp/python/3.10.10/python-3.10.10-amd64.exe)

#### Installing Python on a Mac
**Note:** _Macs come with a version of Python installed, but this is an older version of Python (specifically, Python 2). the training requires the use of Python 3, so make sure to follow these instructions even if you think you already have Python installed. If you require the use of Python 2 for other work, you can still install Python 3, which exists alongside Python 2 rather than replacing it._
1. Open the downloaded Python installer file and follow the default instructions.
2. Open up your terminal application.
3. Type python3 and press enter. You should see something that looks like this:
```bash
Python 3.10.10 (main, Feb  8 2023, 05:44:44) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
#### Installing Python on Windows
1. Open the downloaded file. Before installing, there should be an option that says "Add Python 3.7 in PATH". **Make sure to check this box.** Then, continue installing normally.
2. Open up the command prompt.
3. Type py and press enter. You should see something that looks like this:
```bash
Python 3.10.10 (v3.7.3:9a3ffc0492, Feb 8 2023, 05:44:44)
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
### Check Python Versions
Every Python version has three digits.

The first digit represents the major version, the second the minor version, and the third digit represents the micro version or “revision level.”

You must also note that major versions are typically not fully compatible with each other. In other words, software written with Python version 2.x.x may not run correctly with Python 3.x.x.

However, minor releases are typically compatible with the previous releases. For example, code written in Python 3.1.x will run with Python 3.9.x (which is the current Python version).
#### Checking Python Version in Mac
To open the Terminal, open the Finder. Then navigate to Applications, and select Utilities. Find and launch the Terminal from here.

Enter the following command:
```bash
python --version
Python 2.7.16
```
You can find the version of Python 3 you’re using by entering the following command:
```bash
python3 --version
```
#### Checking Python Version in Windows
If you’re using Windows 10, you can find the Python version using Windows PowerShell/Git Bash. The simplest way of launching PowerShell is to hit the Windows key and type “powershell.” You can then select it from the list of options that appears.

All you have to do next is type the following:
```bash
 python --version
 Python 3.10.10
```
### Installing and Testing PyCharm
#### Installation
To get started, download and install the community or professional (if you have JetBrain license) version of PyCharm:

[Mac Download](https://www.jetbrains.com/pycharm/download/#section=mac) (Open the downloaded .dmg file and drag PyCharm into your Applications folder)

[Windows Download](https://www.jetbrains.com/pycharm/download/#section=windows) (Open the downloaded .exe file and install PyCharm, using all the default options.)

#### Testing PyCharm
Now that you have PyCharm downloaded and installed, open it up and follow the setup wizard, which allows you to choose some default settings. Feel free to install any additional plugins it suggests, although none will be necessary for this training.

PyCharm models a program as a 'project', which consists of one or more Python files, as well as any additional resources like images or text files. To get you familiar with working with projects in PyCharm, a python study project has been provided, which you can git clone [here](https://gitee.unigroupinc.com/learning-and-development/pythononthemove). To test out this project, and to gain familiarity with the PyCharm environment, open it in PyCharm (using the 'open' option on the first screen). Now, follow the steps below to run the project in PyCharm:

1. First, you need to configure the interpreter for the project, which essentially means that you want to specify the version of Python you'll be using to run your code. To do so, click 'configure Python Interpreter' at the top of your PyCharm window.
2. Then, select the dropdown at the top of the window and click 'show all'.
3. Then click the + button at the bottom left corner.
4. Now, Python 3.10 should automatically be selected on the next window. Click 'OK', and save your progress. PyCharm might take a while to recognize your interpreter, but you should eventually be good to go.
5. Once PyCharm has finished recognizing your interpreter (indicated by the progress bar in the bottom right corner), you should be ready to run your program! Click the green arrow in the top right of the window to run, and you should see your program's output in the bottom pane.
   If you get an error saying "cannot run program", click "runner" in the top right>edit configuration>python interpreter> Python 3.10.
6. Now, click 'terminal' in the bottom of your Window to open up PyCharm's integrated terminal. Type python3 runner.py (or on Windows, py runner.py and press enter to see the program's output.
