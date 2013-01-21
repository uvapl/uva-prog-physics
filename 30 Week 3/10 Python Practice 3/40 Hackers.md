# Hacker exercise

## Palindromes!

Write a function is palindrome which takes a string as parameter, and returns
True if the string is a palindrome (meaning it is the same forwards as
backwards), and False otherwise. Save your work in `palindromes.py`. This
problem is kind of tricky so feel free to ask for help; turn in any progress
you make on it as well as comments explaining what does and doesn't work. For
an additional challenge, try writing this as a recursive function.

Some useful things to remember:

* Use the function `len` to find the length of a string.

* To get just a piece of a string, use the slice operator. For example:

		astring = 'hello'
		substr  = astring[1:-1]  #sets substr to 'ell'

* You can decide for yourself whether you want your function to correctly
  identify palindromes that have spaces (such as 'able was i ere i saw elba').
  Look up `string.join` for a useful function to use.

* `string.lower` may also be a useful function.

* BE SURE TO TEST WELL! Include multiple test cases, including one where the
  word isn't a palindrome, but the first and last letters are equal (such as
  "yummy").

* It is easiest to do this with a while loop, although there are a few
  different ways of structuring such a loop. Think about what conditions need
  to be met for a palindrome to be true, and when you can stop testing for one
  (hint: the words 'ana' and 'anna' are both palindromes; when do we know to
  stop checking?)
