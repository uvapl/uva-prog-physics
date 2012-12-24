Exercise 1.12 – Boolean operators
Boolean operators can seem tricky at first, and it takes practice to evaluate them correctly. Write the value (True or False) produced by each expession below, using the assigned values of the variables a, b, and c. Try to do this without using your interpreter, but you should check yourself when you think you’ve got it. Hint: Work from the inside out, starting with the inner-most expressions, like in arithmetic.
a = False
b = True
c = False
1. b and c
2. b or c
3. not a and b
4. (a and b) or not c

5. not b and not (a or c)

Exercise 1.13 – Conditionals
The purpose of this exercise is to understand conditionals. Tiberius is looking for his dream job, but has some restrictions. He loves California and would take a job there if it paid over 40,000 a year. He hates Massachusetts and demands at least 100,000 to work there. Any other place he’s content to work for 60,000 a year, unless he can work in space in which case he would work for free. The following code shows his basic strategy for evaluating a job offer.
pay = _____
location = _____
if location == "U.S.S. Enterprise":"
    print "So long, suckers! I’ll take it!"
elif location == "Massachusetts":
    if pay < 100000:
       print "No way"
    else:
       print "I’ll take it!"
elif location == "California" and pay > 40000:
    print "I’ll take it!"
elif pay > 60000:
    print "I’ll take it!"
else:
    print "No thanks, I can find something better."
For each of the following job offers, write down the output that would be generated. Do this without running the code. It is an important skill to be able to understand what a piece of code does without running it.
1. location = "Massachusetts" pay = 50000
2. location = "Iowa" pay = 50000
3. location = "California" pay = 50000
4. location = "U.S.S. Enterprise" pay = 1
5. location = "California" pay = 25000

Exercise 1.14 – Understanding loops
For each of the following fragments of code, write what the output would be. Again, do this without running the code (although feel free to check yourself when you’re done).
1. num = 10
while num > 3:
         print num
         num = num - 1
2. divisor = 2
for i in range(0, 10, 2):
         print i/divisor
3. num = 10 while True:
         if num < 7:
            break
         print num
         num -= 1
4. count = 0
for letter in ’Snow!’:
         print ’Letter #’, count, ’is’, letter
         count += 1

		Exercise 1.15 – Buggy loop (aka Find The Bug!)
		Consider the following program that Ben Bitdiddle handed in to the course staff (again, try to do this exercise without running the code in IDLE!):
		n = 10 i = 10
		while i > 0:
		   print i
		if i % 2 == 0: i=i/2
		else: i=i+1
		What do you think this code is doing? Without comments it is hard to guess what Ben’s intention was (*cough* this is why the staff loves to look at commented code!!), so read through it and make a sensible guess as to what it is doing. There’s a lot of mistakes in the code so your guess is as good as ours!
		1. Draw a table that shows the value of the variables n and i during the execution of the program. Your table should contain two columns (one for each variable) and one row for each iteration. For each row in the table, write down the values of the variables as they would be at the line containing the print statement.
		2. Ben made a lot of mistakes. State what you think Ben was trying to do and suggest one or more ways he could fix his code (there’s a few good answers for this depending on what you think the code should be doing).
		
