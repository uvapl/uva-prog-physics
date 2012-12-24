Exercise 1.6 – New Operators
Open up IDLE and play around with the new operators showed today in class. Make sure that you understand how to use them and what they are used for! The operators ==, !=, <, >, <=, >= are called relation operators. They work on all types, not just numbers, and return a Boolean (True/False) value. Remember, if you are using Booleans, to capitalize True and False! Here’s an example shell session; try other examples you can think of.
>>> 5 >= 7
False
>>> ’abc’ != ’def’
True
>>> x = ’abc’
>>> x == ’abc’
True
This next example is strange! Try to understand what’s going on here, and ask if you’re confused.
>>> a = True
>>> b = (5 < 7)
>>> a == b
True
Next, the operators +=, -=, *=, /= change the value of a stored variable in a quicker way. In the following example, we add 6 to a variable in two different ways; note that we get the same result! Try using all of these operators in your interpreter window before moving on.
>>> x = 5
>>> x = x + 6
>>> print x
11
>>> y = 5
>>> y += 6
>>> print y
11
We strongly suggest you finish all the written exercises now, before continuing on with the next code problem.

Exercise 1.7 – Rock, Paper, Scissors
In this exercise, you are going to practice using conditionals (if, elif, else). You will write a small program that will determine the result of a rock, paper, scissors game, given Player 1 and Player 2’s choices. Your program will print out the result. Here are the rules of the game:
Image by MIT OpenCourseWare.
1. First create a truth table for all the possible choices for player 1 and 2, and the outcome of the game. This will help you figure out how to code the game!
￼￼Paper
beats rock
￼￼￼￼￼Scissors
beats paper
￼￼￼￼￼￼￼Rock
beats scissors
Player 2
Rock
Scissors
Player 1
Rock Rock
Result
Tie Player 1
2. Create a new file rps.py that will generate the outcome of the rock, scissors, paper game. The program should ask the user for input and display the answer as follows:
  Player 1? rock
  Player 2? scissors
  Player 1 wins.
The only valid inputs are rock, paper, and scissors. If the user enters anything else, your program should output “This is not a valid object selection”. Use the truth table you created to help with creating the conditions for your if statement(s). Read on to the next page before starting...

Note If you have a long condition in your if statement, and you want to split it into multiple lines, you can either enclose the entire expression in parenthesis, e.g.
     if (player1 == ’rock’ and
        player2 == ’scissors’):
        print ’Player 1 wins.’
Or, you can use the backslash symbol to indicate to Python that the next line is still part of the previous line of code, e.g.
     if player1 == ’rock’ and\
        player2 == ’scissors’:
        print ’Player 1 wins.’
Use whichever form you feel comfortable using. When you are done coding and testing!, print a copy of the file and turn it in. Make sure your name and section number is in the comment section of your program.
Exercise 1.8 – For & While Loops
Create a new file called loops.py and use it for all parts of this exercise. Remember the difference between input and raw input? If not, look at Exercise 1.5 again.
Be sure to test your code for each part before moving on to the next part.
1. Using a for loop, write a program that prints out the decimal equivalents of 1/2, 1/3, 1/4, . . . , 1/10.
2. Write a program using a while loop that asks the user for a number, and prints a countdown from that number to zero. What should your program do if the user inputs a negative number? As a programmer, you should always consider “edge conditions” like these when you program! (Another way to put it- always assume the users of your program will be trying to find a way to break it! If you don’t include a condition that catches negative numbers, what will your program do?)
3. Write a program using a for loop that calculates exponentials. Your program should ask the user for a base base and an exponent exp, and calculate baseexp.
4. Write a program using a while loop that asks the user to enter a number that is divisible by 2. Give the user a witty message if they enter something that is not divisible by 2- and make them enter a new number. Don’t let them stop until they enter an even number! Print a congratulatory message when they *finally* get it right.
When you are done, print a copy of the file and turn it in. Make sure your name and section number is in the comment section of your program.

