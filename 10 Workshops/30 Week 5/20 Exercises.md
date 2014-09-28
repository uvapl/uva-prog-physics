## Exercises

Most of these exercises should be put in a file called `homework3.py`. You
should make sure this file immediately runs and gives correct output for every
exercise. The same goes for all other files you submit.

### 3.0 Horizontal Bar Chart

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

### 3.1 Collision Detection of Balls

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

### 3.2 Moving Balls

Another important function of a physics engine is to calculate how an object moves under the laws of physics. This time, write a function `ball_step` that moves a ball over one time step. Your function should take as parameters a tuple  that contains the ball's position and speed - $$(x,y,vx,vy)$$ - and the length of the time step: `dt`. 

In your function, compute the change in position over a time `dt` for *x* and *y* separately. Let your ball bounce back from the walls at $$x=0$$, $$y=0$$, $$x=10$$, and $$y=10$$. Return the new position of the ball.

Now build another function `move_ball` that uses the step function to move a ball for a number of seconds. The input parameters are a ball tuple, a number of seconds, and a time step `dt`. Check your function with the following input:

	move_ball((2, 3, 1, -2), 5, 1)

This should give as output:

	(7, 5, 1, 2)

### Double check

For every problem, check the following:

* Have you put the problem in a function?
* Have you added the problem to the right Python file?
* Have you put your name on top of that file?
* Have you made sure that we don't have to type anything when testing?
* Have you written at least three tests to show the program is correct?
* Do the tests give the expected output?
