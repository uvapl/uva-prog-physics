## Exercises

Most of these exercises should be put in a file called `homework3.py`. You
should make sure this file immediately runs and gives correct output for every
exercise. The same goes for all other files you submit.

### Basics Exercises

The following exercises are not required, but will help you through this week's homework.

* Create a dictionary.
* Print the last digit of a number using a Python operator.
* Add a key and value to a dictionary.
* Add a list to an already existing key in a dictionary.
* Print all the keys of a dictionary. Then print all the values. Then print a list of tuples that contains the keys and values.
* Print five hashtags in a row using multiplication.
* Compute the distance between two points using Pythagoras' theorem.
* A ball is at point (2,3) and has velocity (2,4). Where is the ball 0.5 seconds later?
* A ball moves for 5 seconds, in steps of 0.01 seconds. How many steps need to be taken?
* Form a dictionary from two lists, using `dict` and `zip`.


### 3.0 Mutability

We've learned about many Python data structures (strings, lists, tuples,
dictionaries). For both "mutable" and "immutable", please give a short (5
words or fewer) definition, and then list what data structure(s) have that
characteristic.

Mutable:

<textarea name="a[3-1-1]"></textarea>

Immutable:

<textarea name="a[3-1-2]"></textarea>

### 3.1 Horizontal Bar Chart

For this exercise we will write a program that sorts a list of numbers by their last decimal and displays a simple bar chart for the number of times each decimal occurs.

First, write a function `sort_by_digit` that takes a list as parameter and returns a dictionary for which each number is sorted by its last digit. For example, the following input:

	[45, 90, 30, 33, 34, 64, 34, 28, 72, 20]

Should return this dictionary:

	{0: [90, 30, 20], 2: [72], 3: [33], 4: [34, 64, 34], 5: [45], 8: [28]}

Hint: think about how you can get the least significant digit from a number using a Python operator.

Then, write a function `chart` that plots a simple horizontal bar chart from such a generated dictionary. For the dictionary above, your output should look like this:

	0 ###
	2 #
	3 #
	4 ###
	5 #
	8 #

Write a test function `test_chart` that runs `chart` using at least three test cases. If you want some extra practice, make `test_chart` generate three lists of random numbers and chart those.

### 3.2 Finding Bugs

The following set of instructions were given to Ben Bitdiddle, and he produced
the code below. Find at least three bugs he made, and say how to fix them.

> Instructions: Write a negate function that takes a number and returns the
negation of that number. Also write a large num function that takes a number,
and returns True if that number is bigger than 10000, and False otherwise.
Additionally, write some code to test your functions.

This is the program Ben wrote:

	def negate(num):
		return -num

	def large_num(num):
		res = (num > 10000)

	negate(b)
	neg_b = num
	print 'b:', b, 'neg_b:', neg_b

	big = large_num(b)
	print 'b is big:', big

Bugs:

1. <textarea name="a[3-2-1]"></textarea>

2. <textarea name="a[3-2-2]"></textarea>

3. <textarea name="a[3-2-3]"></textarea>

### 3.3 Collision Detection of Balls

Many games have complex physics engines, and one major function of these
engines is to figure out if two objects are colliding. Weirdly-shaped objects
are often approximated as balls. In this problem, we will figure out if two
balls are colliding. You'll need to remember how to unpack tuples; refer to
the Tuples chapter in *Think Python* or ask an assistant if this is confusing.

We will think in 2D to simplify things, though 3D isn't different
conceptually. For calculating a collision, we only care about a ball's position
in space, as well as its size. We can store a ball's position with the $$(x,y)$$
coordinates of its center point, and we can calculate its size if we know its
radius. Thus, we represent a ball in 2D space as a tuple of $$(x, y, r)$$.

To figure out if two balls are colliding, we need to compute the distance
between their centers, then see if this distance is less than or equal to the
sum of their radii. If so, they are colliding.

Write a function `ball_collide` that takes two balls as parameters and computes
if they are colliding; your function should return a Boolean saying whether or
not the balls are colliding. Optional: For a little extra challenge, write your
function to work with balls in 3D space. How should you represent the balls?

Write your own test function for `ball_collide`. Be sure to figure out any *edge
cases* you need to test. (Do you know what edge cases are? If not, discuss with your teaching assistant!)

### 3.4 Moving Balls

Another important function of a physics engine is to calculate how an object moves under the laws of physics. This time, write a function `ball_step` that moves a ball over one time step. Your function should take as parameters a tuple  that contains the ball's position and speed - $$(x,y,vx,vy)$$ - and the length of the time step: `dt`. 

In your function, compute the change in position over a time `dt` for *x* and *y* separately. Let your ball bounce back from the walls at $$x=0$$, $$y=0$$, $$x=10$$, and $$y=10$$. Return the new position of the ball.

Now build another function `move_ball` that uses the step function to move a ball for a number of seconds. The input parameters are a ball tuple, a number of seconds, and a time step `dt`. Check your function with the following input:

	move_ball((2, 3, 1, -2), 5, 1)

This should give as output:

	(7, 7, 1, 2)

### 3.5 A Mystery Program

Ben next turned in the following uncommented code (WTF?? WHY) to the
assistants. Help us figure out what it does!

	 1 print "Think of a number between 1 and 100, but don't tell me what you choose."
	 2 min_n = 1
	 3 max_n = 100
	 4 right_answer = False
	 5
	 6 while not right_answer:
	 7     mid_n = (max_n + min_n + 1)/2
	 8     answer = raw_input('Is it ' + str(mid_n) + '? ')
	 9     if answer[0] == 'y':
	10         right_answer = True
	11     elif answer.startswith('higher'):
	12         min_n = mid_n + 1
	13     elif answer.startswith('lower'):
	14         max_n = mid_n - 1
	15     else:
	16         print "Sorry, I don't understand your answer."
	17
	18 print 'Woohoo! I got it!'

1. The while loop exits when the variable right answer is True. What will
   cause right answer to be true?

   <textarea name="a[3-3-1]"></textarea>

2. How many times will the program print out 'Woohoo! I got it!'?

   <textarea name="a[3-3-2]"></textarea>

3. What are we using the variable answer for?

   <textarea name="a[3-3-3]"></textarea>

4. The program makes a guess in line 8. What user responses will be understood
   by the program after it makes its guess?

   <textarea name="a[3-3-4]"></textarea>

5. If the program gets the response 'higher', what does that tell it about its
   guess?

   <textarea name="a[3-3-5]"></textarea>

6. What are the variables min n, max n and mid n used for?

   <textarea name="a[3-3-6]"></textarea>

This is an example of binary search, a simple but important algorithm in
computer science. If you're curious, or confused, read the Wikipedia article
on binary search to find out more and get a good explanation of what's going
on here.

### Data Processing

Proceed with the data processing tab at the top of this page.
