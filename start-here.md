###Installation Guide and Running your First Python Script

####Running Python in Windows or Linux
- Download and install Python from here: http://www.python.org/download/releases/2.7.6/
- I prefer to use IDLE (bundled with Python) over the command prompt when possible -- simply put, it's easier to use.  If you need to run Python scripts from the command line, the Mac instructions below will work with minimal adjustment.
- When you run IDLE, you'll automatically be in the interactive interpreter mode where you can run Python commands one at a time.
- To create a new file from IDLE, go to File > New Window.  A new, blank screen will open up where you can create your Python projects.
- When you have a Python file open in IDLE, you can run it at any time by pressing **F5**.

####Running Python on a Mac

Python comes bundled with Macs already, so there's no extra setup for now.  You'll want to check which version you have, but it's not super important for writing your first scripts.

There's a known problem making it more difficult for Macs to run IDLE (see http://www.python.org/download/mac/tcltk/ for full details) -- but they can run Python just fine!

####Mac: Running Python commands one at a time (using the interactive interpreter)
- Open a terminal window (from the Finder, search for Terminal)
- Type **python** and hit enter
- Your command prompt should change from a dollar sign (**$**) to three greater than signs (**>>>**)
- The command prompt is a signal of where you are -- terminal is **$**; python is **>>>**
- Once you have the **>>>** prompt, you can enter as many Python commands as you like.
- Type **exit()** to quit and return to the command prompt.

####Mac: Running Python Files from the Terminal
- Open a terminal window (from the Finder, search for Terminal)
- When you open the terminal window, the words before your username are the folder you're in.
- You're probably on your desktop to start. I recommend creating a folder on your desktop to put your Python scripts in.
- For this example, let's say I named the folder pyscripts.
- Go back to the terminal and type in **cd pyscripts** -- this will change the folder the terminal is working in.
- When you create a Python script for Python to run, you should create it in TextEdit, TextWrangler, or some other text editor that can save files in **plain text** format -- any other kind of format will confuse Python!
- Let's also assume that I created a Python script called **lesson1_pbj.py**, and that file lives in **pyscripts** on the desktop.
- To run lesson1_pbj.py, I would type into the terminal: **python lesson1_pbj.py**

####Mac: Troubleshooting Running Python Files from the Terminal
- Make sure you're in the correct folder! You can check which folder the terminal is looking in by typing **pwd**
- Similarly, make sure the file you want to run is in the folder you're in! Type **ls** to see all of the files in the folder terminal is currently working in.
- Remember that when you see the dollar sign prompt (**$**), you're working in terminal, and can run scripts at the command line.  But when you see the **>>>** prompt, you're in Python's interactive interpreter mode, and you'll need to type **exit()** to get back.
