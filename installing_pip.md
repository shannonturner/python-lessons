## Installing the Python Package Managers

Packages are groups of functions that someone else has built in Python to share with the world
Packages can help you perform a set of functions
For example, the **requests** package lets you visit a webpage and retrieve the contents (source) as a string.

Before you can use someone else's package, you must install it onto your computer.
Before you can install it on your computer, you'll need to install a package manager.

The preferred package manager is called pip, but we need to take a few steps to get there.

## Complete these two steps before going on to your system-specific instructions below.
* First, go here: https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
* Copy / save that file to your computer

**Windows-specific instructions**
* Make sure you complete the first two steps above first.
* Create the folder 'scripts' inside C:\python27
* Save the ez_setup.py inside C:\python27\scripts
* If in Windows, now you'll need to add "C:\Python27\scripts" to your PATH environment variable.
* To do that, go to My Computer > Properties > Advanced System Settings > Environment Variables > Path
* You'll also need to add "C:\Python27" to your PATH environment variable.
* Don't delete everything else.  Add onto it, separating the entries with a semicolon.
* Open your terminal (Start Menu > Run > cmd) or (Start Menu > Search > cmd)
* Use cd to change the directory you're working in: cd c:/python27/scripts
* Type **python ez_setup.py** and hit enter.
* Type **easy_install pip** and hit enter.
* Type **pip install requests** and hit enter.  If it was successful, you're done! Help a neighbor.

**Mac-specific instructions**
* Make sure you complete the first two steps above first.
* Run that program in Python.
* Type **easy_install pip** and hit enter.  If you get permission errors, try **sudo easy_install pip**
* Type **pip install requests** and hit enter.  If you get permission errors, try **sudo pip install requests**
* If it was successful, you're done! Help a neighbor.