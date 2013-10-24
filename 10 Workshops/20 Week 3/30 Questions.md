# Questions to answer

## Warm up: recollections

Recall that a string is **immutable**, while a list is **mutable**. What does
this mean? Research it with your neighbor!

<textarea name="a[2-11]"></textarea>

## String operations

String operators might be a little less intuitive than those on numbers. This
exercise will give you a chance to practice those. Given the following 
variables:

	look = 'Look at me!'
	now = ' NOW'

What are the values of the following expressions? Try to guess on your own
before using your interpreter (but feel free to use your interpreter once you 
get stuck).

|expression                           |value                               |
|-------------------------------------|------------------------------------|
|`look[:4]`                           |<input name="a[2-12-1]" type="text">|
|`look[-1]`                           |<input name="a[2-12-2]" type="text">|
|`look*2`                             |<input name="a[2-12-3]" type="text">|
|`look[:-1] + now + look[-1]`         |<input name="a[2-12-4]" type="text">|
|`now[1]`                             |<input name="a[2-12-5]" type="text">|
|`now[4]`                             |<input name="a[2-12-6]" type="text">|
|`look*2 + look[:-1] + now + look[-1]`|<input name="a[2-12-7]" type="text">|

For more on strings, see [the Python docs](http://docs.python.org/release/2.6.6/library/stdtypes.html#string-methods).

