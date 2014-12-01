This week, you'll be visualizing physical phenomena. Download the PDF
for complete instructions.

* [Slides](Lecture_6_slides_blok2.pdf)
* [Assignment](Lecture_6_Assignments_UvA.pdf)
* [Animation template](animation_template.py)

Hand in your solutions on this web site!

### Basics Exercises

The following exercises are not required, but will help you through this week's homework. Read the introduction to the assignments first.

* Generate a list of ball tuples. Give the ball tuples a random velocity.
* Update each ball tuple in the list by one timestep `dt` using the function `ball_step` from last week.
* Simulate moving the balls for several seconds using the function `ball_step` multiple times.
* After each step, append the x- and y-coordinates of the first ball to two lists. After the simulation, plot the two lists.
* Now plot only the x-coordinate, as a function of the step number.
* Remove a ball from the list.
* Sum the distances between all the particles in the list using a double `for` loop.