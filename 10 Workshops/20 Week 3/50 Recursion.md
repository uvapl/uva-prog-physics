## Totally Extra Exercises on Recursion

These exercises are fully optional but can be very interesting mind teasers.

> recursion (noun)
> : *see* recursion

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

### Example: sum

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

### Exercises

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
