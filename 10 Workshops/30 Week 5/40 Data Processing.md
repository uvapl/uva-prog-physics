## Exercise: data processing

Put your work for these exercises in a separate file called `data.py`.

First, download [population.csv](population.csv) (**download, not open in
Excel!**), containing a list of the population counts in the Netherlands over
the last 60 years.

You will need to read this file and plot its data. Have a look at it first,
it's quite small.

Next, open your Python Shell and try to read it into Python:

	>>> import csv
	>>> file = csv.reader(open("population.csv"))
	>>> file.next()
	>>> ['country', 'country isocode', 'year', 'POP']

Cool! Apparently Python can read your file. This first line isn't so
interesting to our program. But it does tell us what data can be found where.

Did you notice that the line is output by Python as an **list**? That is very
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

### Printing the population list nicely

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

### Reading the list into a dictionary

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

	print population_dict('population.csv')

### Plotting the population

Now that we can read the census data into a dictionary, we can do other stuff
with it.

Create a function that plots data from a dictionary in a graph. Give it a
reasonable name. The function should have an extra parameter that tells us
what the title of the plot should be. Pass this title to `pyplot`.

Of course, because nothing is ever *easy*, you can't feed `pyplot` a
dictionary. It wants lists of the same length: in this case, one containing
the year labels, and one containing the data. How can you extract these lists
from a dictionary? It's quite simple, look it up.

Again, put a test that calls your function in the file! It needs to read a
dictionary and save it, and then pass that dictionary to the plotting function
you just made.

### Calculating year-over-year growth

Now, we want some more statistics. Let's calculate the year-over-year growth
percentage.

Create a function that takes one dictonary as a parameter and returns a new
dictionary containing year-over-year growth rates. You already know how to
extract the population count list from the dictionary. You also know how to
calculate a growth rate from one year to the next. And you know how to save
each calculated rate into a new list.

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

Plot your new dictionary using the same function that you defined previously.

### Acknowledgements

Thanks to Mark Guzdial's Computational Freakonomics class for a reference to
the data we used here.

The Netherlands population data / PWT 7.1 Alan Heston, Robert Summers and
Bettina Aten, Penn World Table Version 7.1, Center for International
Comparisons of Production, Income and Prices at the University of
Pennsylvania, Nov 2012.

### Double check

For every problem, check the following:

* Have you put the problem in a function?
* Have you added the problem to the right Python file?
* Have you put your name on top of that file?
* Have you made sure that we don't have to type anything when testing?
* Have you written at least three tests to show the program is correct?
* Do the tests give the expected output?

When you are done, make sure you have answered all exercise questions, and
submit your files at the submit tab. Check if you can perform the tasks in the summary below. If you have time left, take a go at the
Hacker edition :-)

### Summary

At the end of this week, you should be able to perform the following tasks. If you do not understand what is meant by the following tasks or cannot perform them, have another look at the exercises, or ask an assistant to help you out.

* Create a dictionary and add keys & values to it.
* Create a list of values if several values share the same key.
* Select the last digit of a number using the modulo operator.
* Print the keys and values of a dictionary.
* Represent a ball by a tuple that contains the position and size of the ball.
* Determine the distance between two points.
* Move a ball tuple that contains the position and velocity of the ball by one timestep `dt`.
* Let a ball bounce off a wall.
* Use a loop to move a ball for a given time in timesteps `dt`.
* Read and parse data from a file into lists or a dictionary.
* Convert a dictionary into lists to create a plot of the dictionary.
* Zip two lists into a list of tuples.
* Create a dictionary from a list of tuples.
