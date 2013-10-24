This small practice will cover how to set up Python and introduce you to IDLE,
the Python development environment we will be using throughout this course.

Python should be set up correctly on all Windows machines. Find **Python
(x,y)** in the start menu, and then choose "IDLE". This should start up the
Python development environment.

## Installing on your own machine

Warning: On the Python homepage, the latest version available for download
is actually 3.0. Do not install this! This version is not backwards compatible
with the code that you'll be writing in this course. This is also why Python
2.7 is still the most-used version in research. So, be sure to download
the version listed above.

## Using IDLE

IDLE is the standard Python development environment Its name is an acronym of
"Integrated DeveLopment Environment". It works well on both Unix and Windows
platforms.

It has a Python shell window, which gives you access to the Python interactive
mode. It also has a file editor that lets you create and edit existing Python
source files.

During the following discussion of IDLE's features, instead of passively
reading along, you should start IDLE and *try to replicate the screenshots*.

## Interactive Python shell

When you start up IDLE, a window with an interactive Python shell will pop up:

![IDLE Shell](st-shell.png)

You can type Python code directly into this shell, at the `>>>` prompt.
Whenever you enter a complete code fragment, it will be executed. For instance,
typing:

	>>> print "hello world"

and pressing ENTER, will cause the following to be displayed:

	hello world

Try typing an underscore (`_`). Can you see it? On some operating systems, the
bottoms of hanging letters such as 'g' or 'y', as well as underscorces, cannot
be seen in IDLE. If this is the case for you, go to **Options -> Configure
IDLE**, and change the size of the default font to 9 or 11. This will fix the
problem!

IDLE can also be used as a calculator:

	>>> 4+4
	8
	>>> 8**3
	512

Addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), modulo
(`%`) and power (`**`) operators are built into the Python language. This means
you can use them right away. If you want to use a square root in your
calculation, you can either raise something to the power of 0.5 or you can
import the `math` module. Do not worry about what it means right now, we will
cover this later during the course. Below are two examples of square root
calculation:

	>>> 16**0.5
	4.0
	>>> import math
	>>> math.sqrt(16)
	4.0

The math module allows you to do a number of useful operations:

	>>> math.log(16, 2)
	4.0
	>>> math.cos( 0 )
	1.0

Note that you only need to execute the import command once after you start
IDLE; however you will need to execute it agin if you restart the shell, as
restarting resets everything back to how it was when you opened IDLE. Don't
worry too much about this right now; we'll cover it more in depth soon!

## Exercise

Now, use IDLE to calculate:

1.	$$6 + 4 * 10$$

2.	$$(6 + 4) * 10$$

	Compare this to #1, and note that Python uses parentheses just like you 
	would in normal math to determine order of operations!
	
3.	23.0 to the 5th power

4.	Positive root of the following equation:

	$$34x ^ 2 + 68x - 510$$
	
	Recall that given an equation  
	
	$$ax ^ 2 + bx + c$$
	
	you can get one root using:
	
	$$x_1 = ( -b + sqrt (b ^ 2 - 4ac) ) / ( 2a )$$.

This short tutorial for IDLE is based on the official IDLE tutorial by Daryl
Harms.
