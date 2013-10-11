# Pig Latin

Write a function pig_latin that takes in a single word, then converts the
word to Pig Latin. To review, Pig Latin takes the first letter of a word, 
puts it at the end, and appends "ay". The only exception is if the first 
letter is a vowel, in which case we keep it as it is and append "hay" to
the end. So:

|english  |pig latin|
|---------|---------|
|boot     |ootbay   |
|image    |imagehay |

It will be useful to define a list at the top of your code file called 
`VOWELS`. This way, you can check if a letter `x` is a vowel with the 
expression `x in VOWELS`. Remember: to get a word except for the first 
letter, you can use `word[1:]`.

Test your function with some interesting tests of which you already know
the answer!

## Sentences

Converting one word to Pig Latin is okay, but it would be more useful to be
able to convert whole sentences; so for this exercise, we'll use `raw_input`
to ask the user for a full sentence and translate it, word by word. It's
tricky for us to deal with punctuation and numbers with what we know so far,
so instead, ask the user to enter only words and spaces. You can convert 
their input from a string to a list of strings by calling split on the 
string; also, you can use lower to make a string all lowercase:

	>>> phrase = 'My namE is JohN SmIth'
	>>> word_list = phrase.split()
	>>> print word_list
	['My', 'namE', 'is', 'JohN', 'SmIth']
	>>> lowercase_phrase = phrase.lower()
	>>> print lowercase_phrase
	’my name is john smith’

Using such a list of words, you can go through each word and convert it to 
Pig Latin.

It will make your life much easier --- and your code much better --- if you
separate tasks into functions, e.g. have a function that converts one word
to Pig Latin rather than putting it into your main program code (you
already have that one!).

Extensions: once you have your program working, make it interactive such
that it keeps translating phrases into Pig Latin until the user enters in
the phrase QUIT. Or you can add in some more complex Pig Latin rules:
for example, words that start with "th", "st", "qu", "pl", or "tr" should
move *both* of those letters to the end.

|english|pig latin|
|-------|---------|
|stop   |opstay   |
|there  |erethay  |

There are many other Pig Latin rules that you can find online if you want
a true converter. Finally, you could try and deal with punctuation by 
looking for it within a string and moving it to the end of the word (the
solutions I wrote only handle commas, periods, !, ?, : and ; that appear 
at the ends of words, as they are pretty simple to handle).
