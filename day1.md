# Day 1: The Tyranny of the Rocket Equation

## Part One

This one is pretty simple. We're given an equation f(w), where f is the fuel needed to launch a module weighing w mass units.

f(w) = floor(w/3)-2

Given your list of puzzle inputs, evaluate f(w) over all of the inputs and sum the resulting list. Congrats! That's part one solved!

## Part Two

Of course, the issue with our simplistic approach to part one is that you need more fuel to carry your fuel. Negative or zero fuel will be got by "wishing really hard", so that doesn't factor into our mass decisions. So, here's one way to go about it:

1. Calculate the fuel required to launch the module with a mass of w.
2. If the fuel required to launch said fuel is a non-negligible amount (greater than 0), then go back to step 1, but use the mass of the fuel as w.
3. Once the weight of the fuel requires a negligible amount of fuel to carry, sum all of that.
4. That's your fuel count.

That may be hard to understand. Here's the process covered as it is in my implementation.

For w = 500 units;

1. f(500) = 264 fuel units
2. f(164) = 52 > 0, so go back to step 1

1. f(164) = 52 fuel units
2. f(52) = 15 > 0, so go back to step 1

1. f(15) = 3 fuel units
2. f(3) = 0, so move on
3. 164 + 52 + 15 + 3 = 234
4. You need 234 fuel units to launch a module weighing 500 mass units.

Write that in some form of code, evaluate it over your input, and voila!
