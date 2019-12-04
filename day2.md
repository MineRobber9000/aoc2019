# Day 2: 1202 Program Alarm

Referencing the famous 1202 alarm on the Apollo Guidance Computer, we're going 
back to the well of "writing a simulator for an architecture".

## Part 1

Intcode is simple. What we are given for opcodes is:

 - `1 X Y Z` - add the value at X to the value at Y and store the result at Z
 - `2 X Y Z` - multiply the value at X to the value at Y and store the result 
at Z
 - `99` - halt immediately

Program an Intcode emulator, and use it over your puzzle input., remembering to 
set the value at 1 to `12` and the value at 2 to `2`. The value at 0 when the 
halt is reached is the puzzle answer.

## Part 2

You're congratulated on your emulator, and given a new task: determine which 
pair of inputs will output `19690720`, the date of the moon landing.

The puzzle input is the same, and you should brute-force this over a decently 
large interval; I got the solution for my input in [0,99] and [0,99]. Remember 
to reset the memory to your puzzle input after each trial.

Multiply the value at 1 by 100, add the value at 2, and that's your puzzle 
answer.
