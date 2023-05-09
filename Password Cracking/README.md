Extra Credit Assignment 1

In this extra credit assignment, you will explore password cracking in more detail, by creating a password cracking program for the gift card site used in Homework 2.
Part 1

Write a Python program named pwcrack.py that takes as input a password hash (in the format used by the Gift Card site) and a list of words in a text file, and cracks the password hash (i.e., prints out which word from the file matches the provided hash).

What to submit:

    pwcrack.py
    As proof that your password cracker works, crack the password for the admin account (hash: 000000000000000000000000000078d2$18821d89de11ab18488fdc0a01f1ddf4d290e198b0f80cd4974fc031dc2615a3). Include a writeup, part1.txt, that lists the password, the wordlist you used, and the speed of your password cracker (in guesses per second).

Part 2

Write a Python program, pwcrack_online.py that does the same thing as the program in Part 1, but without access to the password hash. It should take as input a username and a list of passwords to try. To do this, you will need to write a program that connects to the web site and tries to log in as a particular user (perhaps using the requests library).

    pwcrack_online.py
    A brief writeup, in part2.txt, that lists the performance of the online version of the password cracker, again in guesses per second. You should also describe how a web site could protect against this kind of attack.

