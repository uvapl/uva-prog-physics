# Exercises

These exercises will take you on a trip through Python. You are supposed to try out the code in your Python interpreter as often as possible.

Some exercises ask you to create a program that you must save and submit at the end of the session.

## 1.0 Get Started

Follow the instructions on in the Get Started section to begin using IDLE, or to install Python on your own computer.

## 1.1 Hello, world!

Recall that a program is just a set of instructions for the computer to execute. Let's start with a basic command `print x` which prints the value of the expression `x`, followed by a *newline*.

Create a new program called `hello_world.py`. You will use this file to write your very first 'Hello, world!' program. How to create a program file:

1. Open a new window by choosing **New Window** from the **File** menu.

	![File -> New](file-new.png)

2. Save the file as `hello_world.py`. Do NOT skip the `.py` portion of the file name --- otherwise, you will lose out on `syntax highlighting`!

	![Filename](filename.png)

3. Start every program with a bank of comments, with a comment line for your name, the name of your file, the day of the week, and today's date. Recall that a comment line begins with a '#' (pound) symbol.

You can now write your very own *Hello, world!* program. This is the first program that most programmers write in a new programming language. In Python, *Hello world!* is a very simple program to write. Do this now... it should be only be one line!

When you are done, save your work and run it. Your code should look similar to this:

![Hello World example](hello-world.png)

To run your program, chose **Run Module** from the **Run** menu (or just hit F5 on Windows/Linux, or fn-F5 on a Mac). When you run the code, your shell should look similar to this:

![Shell Hello World](shell.png)

When you run your code, it first prints the line `>>> ===== RESTART =====`, then runs your code underneath that line. See?

## 1.2 – Printing

Download the [homework1.py](homework1.py) template. Remember to put your name and section at the top. If you don't we'll be highly grumpy.

Write a program using print that, when run, prints out a tic-tac-toe board. Remember to save your program regularly, to keep from losing your work! The purpose of this exercise is to make sure you understand how to write programs using your computing environment; many students in introductory courses experience trouble with assignments not because they have trouble with the material, but because of some weird environment quirk.

Expected output:

	  |  |
	--------
	  |  |
	--------
	  |  |

## 1.3 Variables

Recall that variables are containers for storing information. For example,

Program Text:

{: .language-python}
	a = "Hello, world!"
	print a

Output:

	Hello, world!

The `=` sign is an assignment operator which tells the interpreter to assign the value `"Hello, world!"` to the variable `a`.

Program Text:

{: .language-python}
	a = "Hello, world!"
	a = "and goodbye..."
	print a
		
Output:

	and goodbye...
		
Taking this second example, the value of a after executing the first line above is `"Hello, world!"`. But, after executing the second line, the value of a changes to `"and goodbye..."`. Since we ask the program to print out a only after the second assignment statement, that is the value that gets printed. If you wanted to save the values of both strings, you should change the second variable to another valid variable name, such as `b`.

Variables are useful because they can cut down on the amount of code you have to write. In your own `homework1.py`, write a program that prints out the tic-tac-toe board from exercise 1.2, but which uses variables to cut down on the amount of typing you have to do. **Hint**: how many different variables should you need?

## 1.4 Operators/Order of Operation

Python has the ability to be used as a cheap, 5-dollar calculator. In particular, it supports basic mathematical operators `+`, `-`, `*`, `/` as well as the power operator `**` and the modulus operator `%`.

Program Text:

{: .language-python}
	x = 5 + 7
	print x
	y = x + 10
	print y

Output:

	12
	22

Note that we can use variables in the definition of other variables! Mathematical operators only work on numbers: `int`s or `float`s. Statements such as `'Hi' + 5` or `'5 + 7` will not work.

**Part I**: Input the following sets of equations, and note the difference between `int` arithmetic and `float` arithmetic. You can do this just in your interpreter (you don't need to turn anything in for this part), but pay attention to the output!
	
1.	$$5/2$$, $$5/2.0$$, and $$5.0/2$$

	Note that as long as one argument is a float, all of your math 
	will be floating point!

2.	$$7 xx (1 / 2)$$ and $$7 xx (1 / 2.0)$$

3.	`5 ∗∗ 2`, `5.0 ∗∗ 2`, and `5 ∗∗ 2.0`

4.	$$1/3.0$$

	Note that the final digit is rounded. Python does this for
	non-terminating decimal numbers, as computers cannot store infinite
	numbers!

**Part II**: In `homework1.py`, transcribe the following equations into Python (without simplifying!), preserving order of operation with parenthesis as needed. Save each as the value of a variable, and then print the variable.

1.	$$(3 xx 5) / (2 + 3)$$

2.	$$sqrt(7 + 9) xx 2$$

3.	$$(4 - 7) ^ 3$$

4.	$$root4(-19+100)$$

5.	$$6 mod 4$$

	If you aren't familiar with modular arithmetic, it is pretty
	straightforward: the modulus operator, in the expression $$x mod y$$,
	gives the remainder when $$x$$ is divided by $$y$$. Try a couple of modular
	expressions until you get the hang of it.

**Part III**: In `homework1.py`, use order of operation mathematics to create two equations that look the same (i.e., have the same numbers) but evaluate to different values (due to parenthesization). Save each as the value of a variable, then print the variables.

## 1.5 User input

Do this exercise in `homework1.py`. In this exercise, we will ask the user for his/her first and last name, and date of birth, and print them out formatted. Recall that you can get input from the user using the command `raw_input("text")`, as shown in lecture.

**Note**: There are two functions to get user input. The first, `raw_input`, turns whatever the user inputs into a `string` automatically. The second, `input`, preserves type. So, if the user inputs an `int`, or a `float`, you will get an `int` or a `float` (rather than a `string`). Be careful though: you still want to use raw input if you want a string back, or otherwise the user will have to put quotes around their answer. Use raw input here: it's good for string processing, like this problem. `input` will come in handy when using user input to compute math, like in Exercise 1.8.

Here is an example of what this program should do:

	Enter your first name: Chuck
	Enter your last name: Norris
	Enter your date of birth:
	Month? March
	Day? 10
	Year? 1940
	Chuck Norris was born on March 10, 1940.
		
To print a string and a number in one line, you just need to separate the arguments with a comma (this works for any two types within a print statement). The comma adds a space between the two arguments. For example, the lines:

{: .language-python}
	mo = 'October'
	day = '20'
	year = '1977'
	print mo, day, year

will have the output

	October 20 1977

## 1.6 Pretty printing

Now, for something completely different... a discussion on how to print
strings, most prettily...

Note that none of the commas are in this output! To do that you want something like this:

{: .language-python}
	print mo, day + ',', year

The `+` sign concatenates two strings, but can only be used on two strings. Using it on a number and a string will cause an error (because it is ambiguous as to what you want the program to do!)

That's why it's a great idea to use `raw_input` for this problem; if you use
input you'd have to convert the `int` to a `string`. We'll cover this more
in-depth later on, when we get to strings, but you may want to play with string
concatenation operations now to get everything to look its prettiest.

## Intermezzo: Questions

These questions do not ask you to create a new Python program, but instead ask you to read some code and predict the answer. Sometimes the questions are about other things related to programming.

Sign in to this website *before* you start filling in these forms. If you do, your answers will be saved and you can submit your answers when the day is done.

## 1.7 Variable Names

The Python interpreter has strict rules for variable names. Which of the following are legal Python names? If the name is not legal, state the reason.

|expression |legal?                             |
|-----------|-----------------------------------|
|`and`      |<input name="a[1-9-1]" type="text">|
|`_and`     |<input name="a[1-9-2]" type="text">|
|`var`      |<input name="a[1-9-3]" type="text">|
|`var1`     |<input name="a[1-9-4]" type="text">|
|`1var`     |<input name="a[1-9-5]" type="text">|
|`my-name`  |<input name="a[1-9-6]" type="text">|
|`your_name`|<input name="a[1-9-7]" type="text">|
|`COLOR`    |<input name="a[1-9-8]" type="text">|

## 1.8 Types

It is important that we know the type of the values stored in a variable so that we can use the correct operators (as we have already seen!). Python automatically infers the type from the value you assign to the variable. Write down the type of the values stored in each of the variables below. Pay special attention to punctuation: values are not always the type they seem!

|variable       |type                                |
|---------------|------------------------------------|
|`a = False`    |<input name="a[1-10-1]" type="text">|
|`b = 3.7`      |<input name="a[1-10-2]" type="text">|
|`c = 'Alex'`   |<input name="a[1-10-3]" type="text">|
|`d = 7`        |<input name="a[1-10-4]" type="text">|
|`e = 'True'`   |<input name="a[1-10-5]" type="text">|
|`f = 17`       |<input name="a[1-10-6]" type="text">|
|`g = '17'`     |<input name="a[1-10-7]" type="text">|
|`h = True`     |<input name="a[1-10-8]" type="text">|
|`i = '3.14159'`|<input name="a[1-10-9]" type="text">|

To verify your answers, you can use the interactive Python shell, but first try to do the exercise without help.

	>>> x = 100
	>>> type(x)
	<type 'int'>
	>>>

## 1.9 Natural Language Processing

Consider the following sentence:

> **Alice saw the boy on the hill with the telescope.**

1. Draw a sketch of what's described in this sentence.

2. Draw a different sketch that could also be described by this sentence.

3. Write the sentence in two different ways, that clarifies the meaning of each of your sketches (hint: rewrite the sentence using extra words, commas, etc).

<textarea name="a[1-11-3]"></textarea>

The ambiguity illustrated by this sentence is known as "prepositional phrase attachment." Think about this as you continue to learn how to program, and consider how programming languages are designed to avoid the ambiguity illustrated by this example!

## 1.10 New Operators

Open up IDLE and play around with operators. Make sure that you understand how to use them and what they are used for! The operators `==`, `!=`, `<`, `>`, `<=`, `>=` are called *relation* operators. 

They work on all types, not just numbers, and return a `Boolean` (`True`/`False`) value. Remember, if you are using `Boolean`s, to capitalize `True` and `False`! Here's an example shell session; try other examples you can think of.

	>>> 5 >= 7
	False
	>>> 'abc' != 'def'
	True
	>>> x = 'abc'
	>>> x == 'abc'
	True

This next example is strange! Try to understand what’s going on here, and ask if you're confused.

	>>> a = True
	>>> b = (5 < 7)
	>>> a == b
	True

Next, the operators `+=`, `-=`, `*=`, `/=` change the value of a stored variable in a quicker way. In the following example, we add 6 to a variable in two different ways; note that we get the same result! Try using all of these operators in your interpreter window before moving on.

	>>> x = 5
	>>> x = x + 6
	>>> print x
	11
	>>> y = 5
	>>> y += 6
	>>> print y
	11

## 1.11 Boolean operators

Boolean operators can seem tricky at first, and it takes practice to evaluate them correctly. Write the value (`True` or `False`) produced by each expession below, using the assigned values of the variables `a`, `b`, and `c`. Try to do this without using your interpreter, but you should check yourself when you think you've got it. Hint: Work from the inside out, starting with the inner-most expressions, like in arithmetic.

|expression              |value                             |
|------------------------|----------------------------------|
|`a`                     |False                             |
|`b`                     |True                              |
|`c`                     |False                             |
|`b and c`               |<input name="a[12-1]" type="text">|
|`b or c`                |<input name="a[12-2]" type="text">|
|`not a and b`           |<input name="a[12-3]" type="text">|
|`(a and b) or not c`    |<input name="a[12-4]" type="text">|
|`not b and not (a or c)`|<input name="a[12-5]" type="text">|

## 1.12 Conditionals

The purpose of this exercise is to understand conditionals. Tiberius is looking for his dream job, but has some restrictions. He loves California and would take a job there if it paid over 40,000 a year. He hates Massachusetts and demands at least 100,000 to work there. Any other place he's content to work for 60,000 a year, unless he can work in space in which case he would work for free. The following code shows his basic strategy for evaluating a job offer.

{: .language-python}
	pay = _____
	location = _____

	if location == "U.S.S. Enterprise":
		print "So long, suckers! I'll take it!"
	elif location == "Massachusetts":
		if pay < 100000:
			print "No way"
		else:
			print "I'll take it!"
	elif location == "California" and pay > 40000:
		print "I'll take it!"
	elif pay > 60000:
		print "I'll take it!"
	else:
		print "No thanks, I can find something better."

For each of the following job offers, write down the output that would be generated. Do this without running the code. It is an important skill to be able to understand what a piece of code does without running it.

1.	`location = "Massachusetts"`  
	`pay = 50000`

	<textarea name="a[1-13-1]"></textarea>

2.	`location = "Iowa"`  
	`pay = 50000`

	<textarea name="a[1-13-2]"></textarea>

3.	`location = "California"`  
	`pay = 50000`

	<textarea name="a[1-13-3]"></textarea>

4.	`location = "U.S.S. Enterprise"`  
	`pay = 1`

	<textarea name="a[1-13-4]"></textarea>

5.	`location = "California"`  
	`pay = 25000`

	<textarea name="a[1-13-5]"></textarea>

## 1.13 – Understanding loops

For each of the following fragments of code, write what the output would be. Again, do this without running the code (although feel free to check yourself when you're done).

{: .language-python}
	num = 10
	while num > 3:
		print num
		num = num - 1

> <textarea name="a[1-14-1]"></textarea>

{: .language-python}
	divisor = 2
	for i in range(0, 10, 2):
		print i/divisor

> <textarea name="a[1-14-2]"></textarea>

{: .language-python}
	num = 10
	while True:
		if num < 7:
			break
		print num
		num -= 1

> <textarea name="a[1-14-3]"></textarea>

{: .language-python}
	count = 0
	for letter in 'Snow!':
		print 'Letter #', count, 'is', letter
		count += 1

> <textarea name="a[1-14-4]"></textarea>

## 1.14 Buggy loop (aka Find The Bug!)

Consider the following program that Ben Bitdiddle handed in to the course staff (again, try to do this exercise without running the code in IDLE!):

{: .language-python}
	n = 10
	i = 10
	
	while i > 0:
		print i
		if i % 2 == 0:
			i = i / 2
		else:
			i = i + 1

What do you think this code is doing? Without comments it is hard to guess what Ben’s intention was (*cough* -- this is why the staff loves to look at commented code!!), so read through it and make a sensible guess as to what it is doing. There's a lot of mistakes in the code so your guess is as good as ours!

1.	Make a table that shows the value of the variables `n` and `i` during the
	execution of the program. Your table should contain two columns (one for
	each variable) and one row for each iteration. For each row in the table,
	write down the values of the variables as they would be at the line
	containing the print statement.

	<textarea name="a[1-15-1]"></textarea>

2.	Ben made a lot of mistakes. State what you think Ben was trying to do and
	suggest one or more ways he could fix his code (there's a few good answers
	for this depending on what you think the code should be doing).

	<textarea name="a[1-15-2]"></textarea>

## 1.15 List operations

Say we have this list:

	a_list = [3, 5, 6, 12]

For the following, write the line(s) of code that will emit the given output
making use of the variable `a_list`. For each problem there may be more than
one correct answer; just give one.

1.	Output: `3`

	<textarea name="a[2-13-1]"></textarea>

2.	Output: `12`

	<textarea name="a[2-13-2]"></textarea>

3.	Output: `[5, 6, 12]`

	<textarea name="a[2-13-3]"></textarea>

4.	Output:

		3
		5
		6
		12

	<textarea name="a[2-13-4]"></textarea>

5.	Output: `[12, 6, 5, 3]`

	<textarea name="a[2-13-5]"></textarea>

6.	Output: `[9, 15, 18, 36]`

	<textarea name="a[2-13-6]"></textarea>

7.	Output: `[False, False, True, True]`

	<textarea name="a[2-13-7]"></textarea>

## 1.16 Rock, Paper, Scissors

In this exercise, you are going to practice using conditionals (`if`, `elif`, `else`). You will write a small program that will determine the result of a "rock, paper, scissors" game, given Player 1 and Player 2's choices. Your program will print out the result. Here are the rules of the game:

![Rock, paper, scissors](rock.png)

1. First create a truth table for all the possible choices for player 1 and 2, and the outcome of the game. This will help you figure out how to code the game!

   **Protip**: you can fill out the table below in your browser. If you are logged in to the website, your answers will be saved and remembered until the next time you login.

	|Player 1      |Player 2      |Result        |
	|--------------|--------------|--------------|
	|Rock          |Rock          |Tie           |
	|Rock          |Scissors      |Player 1      |
	|<input name="a[1-7-1]" type="text"> |<input name="a[1-7-2]" type="text"> |<input name="a[1-7-3]" type="text"> |
	|<input name="a[1-7-4]" type="text"> |<input name="a[1-7-5]" type="text"> |<input name="a[1-7-6]" type="text"> |
	|<input name="a[1-7-7]" type="text"> |<input name="a[1-7-8]" type="text"> |<input name="a[1-7-9]" type="text"> |
	|<input name="a[1-7-10]" type="text">|<input name="a[1-7-11]" type="text">|<input name="a[1-7-12]" type="text">|
	|<input name="a[1-7-13]" type="text">|<input name="a[1-7-14]" type="text">|<input name="a[1-7-15]" type="text">|
	|<input name="a[1-7-16]" type="text">|<input name="a[1-7-17]" type="text">|<input name="a[1-7-18]" type="text">|
	|<input name="a[1-7-19]" type="text">|<input name="a[1-7-20]" type="text">|<input name="a[1-7-21]" type="text">|

2. Download [rps.py](rps.py) and put in the code to generate the outcome of the rock, scissors, paper game. The program should ask the user for input and display the answer as follows:

		Player 1? rock
		Player 2? scissors
		Player 1 wins.

The only valid inputs are `rock`, `paper`, and `scissors`. If the user enters anything else, your program should output "This is not a valid object selection". Use the truth table you created to help with creating the conditions for your if statement(s).

**Note**: If you have a long condition in your `if` statement, and you want to split it into multiple lines, you can either enclose the entire expression in parenthesis, e.g.

{: .language-python}
	if (player1 == 'rock' and
		player2 == 'scissors'):
		print 'Player 1 wins.'

Or, you can use the *backslash* symbol to indicate to Python that the next line is still part of the previous line of code, e.g.

{: .language-python}
	if player1 == 'rock' and\
		player2 == 'scissors':
		print 'Player 1 wins.'

Use whichever form you feel comfortable using. When you are done coding *and testing*, print a copy of the file and turn it in. Make sure your name and section number is in the comment section of your program.

## For Loops

You have read about while loops in chapter 6. Another commonly used form of iteration is using for loops. Where a while loop evaluates a certain condition before every iteration, a for loop runs through the elements of a list, where each element can be used in one iteration. For example, the following code:

	for element in mylist:
		print element

prints the elements of `mylist`. For each iteration, the variable `element` takes the value of the next element in `mylist`, until the last element is reached and the iteration stops. 
You could also write 

	for number in [1,2,3,4]:
		print 'the value of the variable \'number\' for this iteration is: ',number

to print the numbers in the list `[1,2,3,4]`. Try this code for yourself.

To generate a list of numbers, we can use the `range` command. The full syntax is `range(start,stop,step)`, to print a list of integer numbers between the value `start` and `stop`, not including stop, in steps of `step`. The `start` and `step` variables are optional. For example, the command

	range(5)

generates the list `[0,1,2,3,4]`. Now try for yourself to generate the list `[2,4,6,8,10]` using the `range` command.

Using a combination of `range` and `len` in a for loop, we can let the iteration variable run over the index numbers of the list. Then we can use slicing to get the value associated with the index number. Try the following code:

	mylist = [9,4,5,3,8,7,6]
	for i in range(len(mylist)):
		print 'index:',i,' value:',mylist[i]
		
Using the index number instead of the value of an element can be very useful, but also very confusing! The following code:

	for i in mylist:
		print mylist[i]

generates an `IndexError: list index out of range` message. The error occurs already at the first run through the loop, when `i=9`, and `mylist[9]` does not exist because the length of mylist is only 7. Beware of this common mistake when writing larger programs!

Note that most while loops can also be formulated in a for loop and vice versa. For example, the elements of a list can also be printed by:

	index = 0
	while(index < len(mylist)):
		print mylist[index]
		index += 1

In general, while loops are more useful when a certain condition needs to be reached for the loop to end and for loops are more useful when a fixed number of iterations is required. However, as there is no intrinsic difference in efficiency, ultimately it remains a design choice. It can make your code much easier to read, though.

## 1.17 For & While Loops Exercise

Download [loops.py](loops.py) and use it for all parts of this exercise. Remember the difference between input and raw input? If not, look at Exercise 1.5 again.

Be sure to test your code for each part before moving on to the next part.

1. Using a for loop, write a program that prints out the decimal equivalents of $$1 / 2, 1/3, 1 / 4, ..., 1/10$$.

2. Write a program using a while loop that asks the user for a number, and prints a countdown from that number to zero. What should your program do if the user inputs a negative number? As a programmer, you should always consider "edge conditions" like these when you program! (Another way to put it: always assume the users of your program will be trying to find a way to break it! If you don't include a condition that catches negative numbers, what will your program do?)

3. Write a program using a for loop that calculates exponentials. Your program should ask the user for a base `base` and an exponent `exp`, and calculate `base`<sup>`exp`</sup>. You can't use the `**` operator!

4. Write a program using a while loop that asks the user to enter a number that is divisible by 2. Give the user a witty message if they enter something that is not divisible by 2, *and make them enter a new number*. Don't let them stop until they enter an even number! Print a congratulatory message when they *finally* get it right. You can check if a number is divisible by another number with the modulo operator `%`.

5. Use the list [9,4,5,3,8,7,6], the modulo operator, and a for loop. Print every third element using `range` and `len`. Then print every element that is divisible by 3 without using `range` and `len`.

6. Write a program that prints the multiplication table for a given number *n*. Using a while loop, check for every number whether it is divisible by *n* with the modulo operator. Add the numbers to a list, stop after 10 are found, and print the list. 

7. Rewrite the multiplication table program using a for loop, and this time use the `break` command to stop when the first number is found that is also divisible by 10.

8. Write a program that asks the user for a list of numbers and prints the largest number: use a for loop to examine each number in the list and a variable to save the largest number. While going through the list, compare each element to the previous maximum and 'remember' the new maximum. After the loop, print out the maximum. 

## 1.18 Additional List Practice

You'll probably also need some practice with lists. Write a program
`list_intersection` that takes the intersection of the two lists; so, a list of
elements that are common to both lists. Put the program in `homework1.py`.

Do not use the construction `if x in list`. Instead, loop through the lists and manually check every element.

Put the following test cases above your program and make sure your results are
correct. Order doesn't matter, as long as the list contains the same elements.

	l1 = [1, 3, 5]
    l2 = [5, 3, 1]  =>  [1, 3, 5]
	l3 = [1, 3, 6, 9]
    l4 = [10, 14, 3, 72, 9]  =>  [3, 9]
    l5 = [2, 3]
    l6 = [3,  3,  3,  2, 10]  =>  [3, 2]
    l7 = [2, 4, 6]
    l8 = [1, 3, 5]  =>  []
    
    # your code here for each intersection (l1, l2), (l3, l4), ...

When you are done, make sure you have answered all exercise questions, and
submit your files at the submit tab! Check if you can perform the tasks in the summary below. If you have time left, take a go at the
Hacker edition :-)

## Summary

At the end of this week, you should be able to perform the following tasks. If you do not understand what is meant by the following tasks or cannot perform them, have another look at the exercises, or ask an assistant to help you out.

* Print a string, a variable, or a combination of the two.
* Assign a value to a variable.
* Change the order of operation in a computation using brackets.
* Convert a variable to a string, integer, or float.
* Check the type of a variable.
* Divide two integers without rounding the result to an integer.
* Use the modulo and power operators.
* Assign user input to a variable using either `raw_input` or `input`.
* Use the relation operators (`==`,`!=`,`<`,`>`,`<=`,`>=`).
* Combine Booleans using `and`, `or`, and `not`.
* Combine several statements in an `if` condition using `and`/`or`.
* Use `range` to print a list of numbers.
* Use the modulo operator to check if a number is divisible by another number.
* Add an element to a list.
* Select one or more elements from a list using the index `[i]`.
* Use a `for` loop to traverse a list. Use as iteration variable either:
	* the elements of the list
	* the index of the list
* Use a `while` loop to check if a condition has been reached.
* `break` a `for` loop when a certain condition is satisfied.
* Rewrite a `for` loop into a `while` loop.
* Traverse a list and find the largest number.
* Use a double `for` loop to compare the elements of two lists.
