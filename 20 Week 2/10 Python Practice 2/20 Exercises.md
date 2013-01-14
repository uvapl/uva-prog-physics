# Exercises

## 2.0 Print vs Return

This isn't really an exercise, just an important bit of reading. Download the
file [homework2.py](homework2.py). In it, these two functions are defined:

	def f1(x):
	    print x + 1
	
	def f2(x):
	    return x + 1

Run this code in the shell. What happens when we call these functions?

	>>> f1(3)
	4
	>>> f2(3)
	4

It looks like they behave in exactly the same way. But they really don't. 
Try this:

	>>> print f1(3)
	4
	None
	>>> print f2(3)
	4

In the case of `f1`, the function, when evaluated, prints `4`; then it returns
the value `None`, which is printed by the Python shell. In the case of `f2`,
it doesn't print anything, but it returns `4`, which is printed by the Python
shell. Finally, we can see the difference here:

	>>> f1(3) + 1
	4
	Traceback (most recent call last):
	   File "<stdin>", line 1, in ?
	TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
	>>> f2(3) + 1
	5

In the first case, the function doesn't return a value, so there’s nothing 
to add to 1, and an error is generated. In the second case, the function 
returns the value 4, which is added to 1, and the result, 5, is printed by 
the Python read-eval-print loop.

But for just about everything we do, it will be returned values that matter, 
and printing will be used only for debugging, or to give information to the
user.

Print is very useful for debugging. It's important to know that you can
print out as many variables and strings as you want in one line, when they 
are separated by commas. Try this:

	>>> x = 100
	>>> print 'x:', x, 'x squared:', x*x, 'sqrt(x):', x**0.5
	x: 100 x squared: 10000 sqrt(x): 10.0

## Intermezzo: Functions

> Note: So far we have been using raw_input to get user input. For the 
> remainder of this course we will move away from this tool, instead writing
> **functions** that take in parameters as opposed to prompting the user for 
> input. So, for this and all following problems, do not use raw_input unless
> explicitly told to do so.

## 2.1 Defining A Function

Recall how we define a function using `def`, and how we pass in parameters. 
In homework2.py (download this from the website if you haven’t yet), 
transform your code from exercise 1.7 (the rock, paper, scissors game) into 
a function that takes parameters, instead of asking the user for input. Make 
sure to return your answer, rather than printing it.

Think a bit about the name you give to the function. Discuss with your 
neighbor what name would be best.

## Intermezzo: Testing

> In order to quickly evaluate the code you have written, and to get some
> practice in writing test, you are to include **at least 3** test cases
> below your code for each exercise.

> Because rock, paper, scissors now is a function that returns a value,
> you can easily call it in a test.

## 2.2 Testing your function

Write three test cases for rock, paper, scissors. Put them directly below
your function and mark in a comment that they are testing statements.

## 2.3 Writing simple methods

In this problem you'll be asked to write two simple methods (*method* is an
interchangeable term for *function*). Be sure to test your functions well, 
including at least 3 test cases for each method.

1. Write a method `is_divisible` that takes two integers, `m` and `n`. The
   method returns `True` if `m` is divisible by `n`, and returns `False`
   otherwise.

   Here's three test cases for that one:

		print "is_divisible(10, 5) == True",  is_divisible(10, 5) == True
		print "is_divisible(18, 7) == False", is_divisible(18, 7) == False
		print "is_divisible(42, 0) == ",      is_divisible(42, 0) == False
	
   Look at the conditions that they test and try to make sure your future 
   test cases are comprehensive.

2. Imagine that Python doesn't have the `!=` operator built in. Write a
   method `not_equal` that takes two parameters and gives the same result 
   as the `!=` operator. Obviously, you cannot use `!=` within your 
   function! Test if your code works by thinking of examples and making sure
   the output is the same for your new method as `!=` gives you.

## 2.4 Additional List Practice

After the crash course last week, you'll probably need some more practice
with lists.

Write a function list_intersection that takes two lists as parameters. Return
a list that gives the intersection of the two lists --- a list of elements 
that are common to both lists.

	def list_intersection(list1, list2):
		# your code here

Put the following test cases below your program and make sure your results 
are the same. Order doesn't matter, as long as the list contains the same 
elements.

	list_intersection([1, 3, 5], [5, 3, 1])               # [1, 3, 5]
	list_intersection([1, 3, 6, 9], [10, 14, 3, 72, 9])   # [3, 9]
    list_intersection([2, 3], [3,  3,  3,  2, 10])        # [3, 2]
    list_intersection([2, 4, 6], [1, 3, 5])               # []

## 2.5 The `math` module

In this exercise, we will play with some of the functions provided in the 
`math` module. A **module** is a Python file with a collection of related 
functions. To use the module, you need to add the following line at the 
top of your program, right underneath the comments with your name:

	import math

If you want to find out what is $sin(90circ)$, we first need to convert 
from degrees to radians and then use the sin function in the math module:
