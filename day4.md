# Day 4: Secure Container

The fuel depot is locked with a code. The elves used to have the code, but 
somebody threw out the sticky note it was written on.

## Part 1

They remember some facts about the password, and they tell us:

* It's a 6-digit number.
* It's between the numbers in your puzzle input.
* It has 2 adjacent numbers that are the same (i.e; 1**22**345)
* Each digit is higher than or equal to the last.

The question we have to solve is "how many passwords meet these criteria?" I'm 
not sure if this is the most optimal solution, but I went about it like this:

1. Make a list of all possible passwords that meet every criteria except for 
the range (6-digit numbers with at least one digit doubled with no decreasing 
runs).
2. Make a list of all of the numbers in the range given by my puzzle input.
3. Print how many passwords are in the intersection of set 1 and 2.

## Part 2

They remembered another fact: the digit that's repeated is only used twice in 
the password.

This means that `123444` is no longer acceptable (the `44` is a part of a 
larger `444`), but `111122` is still acceptable (the `11`s are part of `1111`, 
but there's a `22`).

The way to solve this is to exclude a pair of matching digits when that digit 
is used more than twice in the password. Remaking set 1 and solving for the 
intersection of 1 and 2 will give your part 2 puzzle answer.
