# Exercises

## Recursion

recursion (noun)
: *see* recursion

Formal Definition: an algorithmic technique where a function, in order to
accomplish a task, calls itself with some part of the task.

Recursive solutions involve two major parts:

1. *base cases*, in which the problem is simple enough to be solved directly.
2. *recursive case*.
	A recursive case has three components:
	* Divide the problem into one or more simpler or smaller parts of the problems,
	* Invoke the function (recursively) on each part, and
	* Combine the solutions of the parts into a solution for the problem.

Depending on the problem, any of these may be trivial or complex.

### Example: Sum ###

Non-recursively calculating the sum from a list:

	def it_sum(a_list):
	   result = 0
	   for x in a_list:
	      result += x
	return result

We say that the above function *iterates* over the values in the variable a
list, and returns their sum.

Recursion is similar to iteration, such that the operation being performed is
defined (partly) in terms of itself. Such an operation is said to be
recursive. Here is a recursive definition of the sum() function:

	def rec_sum(a_list):
	   if a_list == []:
	      return 0
	   else:
	      return a_list[0] + rec_sum(a_list[1:])

`rec_sum()` computes the same exact thing as it sum, but in a different way.
The first thing to note is that it does not use a for-loop. The second thing
to note is that the `rec_sum()` function calls itself. That is to say,
`rec_sum()` is defined in terms of itself; it is recursive.

How does it work? Let's go through the parts of recursion:

1. *base case*: what is the base case of rec_sum?
2. *recursive case*:
	* how do we divide the problem?
	* where do we invoke the function recursively?
	* finally, where do we combine the solutions?

Now, let's pretend to be a Python interpreter and execute the recursive calls ourselves.

	rec_sum([1, 2, 3])
	= 1 + rec_sum([2, 3])
	= 1 + (2 + rec_sum([3]))
	= 1 + (2 + (3 + rec_sum([]))
	= 1 + (2 + (3 + 0))
	= 1 + (2 + 3)
	= 1 + 5
	= 6

Note that our base case is when the list is empty. That is the recursive call
to `rec_sum([])`, which evaluates to 0. A base case is very important: it is
the stopping point for recursion.

The recursive case is demonstrated by calls to `rec_sum` where the argument is
a non-empty list. During a recursive case, we make incremental progress
towards solving the problem, and also make a recursive call to the function
with a smaller input space.

## Excercise: recursion ##

You are asked to write several recursive functions. Test them for at least
three special cases. Put this excercise in `homework4.py`.

For all these problems, be sure to carefully consider your base and recursive
cases carefully before you start coding!

1. Write a function that takes in two numbers and recursively multiplies them
   together.

2. Write a function that takes in a `base` and an `exp` and recursively computes
   `base`<sup>`exp`</sup>. You are not allowed to use the `**` operator!

3. Write a function using recursion to print numbers from `n` to `0`.

4. Write a function using recursion to print numbers from `0` to `n` (you just
   need to change one line in the program of problem 3).

5. Write a function using recursion that takes in a string and returns a
   reversed copy of the string. The only string operation you are allowed to use
   is string concatenation (using `+`).

6. Write a function using recursion to check if a number `n` is prime (you have
   to check whether `n` is divisible by any number below `n`).

7. Write a recursive function that takes in one argument `n` and computes
   $$F(n)$$, the `n`th value of the Fibonacci sequence. Recall that the Fibonacci
   sequence is defined by the relation

   $$F(n) = F(n−1) + F(n−2)$$

   where

   $$F(0) = 0$$ and $$F(1) = 1$$.

Visit the Wikipedia page on the Fibonacci Number for more information if
you're still confused.

## Exercise: data processing ##

First, download [population.csv](population.csv), containing a list of the
population counts in the Netherlands over the last 60 years. Put it in your
N:-drive!

You will need to read this file and plot its data. Have a look at it first,
it's quite small.

Next, open your Python Shell and try to read it into Python:

	>>> import csv
	>>> file = csv.reader(open("n:\population.csv"))
	>>> file.next()
	>>> ['country', 'country isocode', 'year', 'POP']

Cool! Apparently Python can read your file. This first line isn't so
interesting to our program. But it does tell us what data can be found where.

Did you notice that the line is output by Python as an **array**? That is very
convenient. It appears that `csv.reader` will read a line and convert it into
an array containing the data fields.

Now, let's go on:

	>>> file.next()
	>>> ['Netherlands', 'NLD', '1950', '10113.527']

Now, that's the *real* data. Line 2 and all other lines contain the data that
was promised.

Let's parse the data:

	>>> line = file.next()
	>>> line[0]
	'Netherlands'

So you can actually save the next line in a variable and use it as a list.
Column 0 always contains the string `'Netherlands'`. And column 1 always
contains `'NLD'`.

Column 2 and 3 are more interesting. They contain the year and population in
that year. But... they are strings. That's of no use in calculations. And
there's a decimal point in the population count!

### Printing the population list nicely ###

Your first assignment with this file is to print the data to the screen.
Define a function like this:

	def print_population_list(filename):
		'''
		Prints the population read from a CSV file, containing 
		years in column 2 and population / 1000 in column 3.

		@param filename: the filename to read the data from
		'''

It is called `print_...` so it may print something! It should have this
**exact** output:

	1950: 10113527
	1951: 10264311
	1952: 10381988
	...

... and so on for each line in the data set.

Put your test call right below the function definition:

	print_population_list('N:\population.csv')

### Reading the list into a dictionary ###

This data connects a population count to a year. So a **dictionary** is the
perfect data structure to put this data in.

Define a function that reads all lines and `return`s the data in a dictionary
object.

	def population_dict(filename):
		'''
		Reads the population from a CSV file, containing 
		years in column 2 and population / 1000 in column 3.

		@param filename: the filename to read the data from
		@return dictionary containing year -> population
		'''

Also, the year in the dictionary should be of a reasonable type. An integer is
ok, but a string is also fine. The population however, is interesting to do
calculations with, so we would like to have that as an integer.

Test the function with this call below your code:

	print population_dict('N:\population.csv')

### Plotting the population ###

Now that we can read the census data into a dictionary, we can do other stuff
with it.

Create a function that plots the data in a graph showing the population growth
over time. Give it a reasonable name.

Of course, `pyplot` does not want the data in a dictionary. It
wants two lists of the same length: one containing the year labels, and one
containing the data.

How can you extract these lists from a dictionary? It's quite simple, look it
up.

### Calculating year-over-year growth ###

Now, we want some more statistics. Let's calculate the year-over-year growth
percentage.

Create a function that takes one dictonary as a parameter and returns a new
dictionary containing year-over-year growth rates.

You know how to extract the population count list from the dictionary. You
also know how to calculate a growth rate from one year to the next. And you
know how to save each calculated rate into a new list.

You probably don't know yet how you can easily create a new dictionary from
the list you just calculated. Say we have created a list `growth_rates` and we
already had the list `years`, then:

	growth_rates = [0.2, 0.23, 0.209, 0.31, ...]
	years = [1950, 1951, 1952, 1953, ...]
	
	growth_rate_dict = dict(zip(years, growth_rates))

`zip` is actually a very cool function. It creates one list from two lists.
Each element of the new list is a tuple, containing one element from list 1
and one element from list 2. And then we put it in the `dict` function to
convert it to a dictionary. Nice!

## Acknowledgements

Thanks to Mark Guzdial's Computational Freakonomics class for a reference to
the data we used here.

The Netherlands population data / PWT 7.1 Alan Heston, Robert Summers and
Bettina Aten, Penn World Table Version 7.1, Center for International
Comparisons of Production, Income and Prices at the University of
Pennsylvania, Nov 2012.
