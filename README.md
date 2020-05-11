# Equation Solver

--------------------

Problem Description
--------------------

Your task is to write a python program to evaluate a set of equations, each specified on separate lines. An equation is defined by:

`<LHS> = <RHS>`

`<LHS>` is the left-hand side of the equation and is always a variable name. A variable name can only be composed of letters from the alphabet (e.g. for which `isalpha()` returns `True`). `<RHS>` is the right hand side of the equation and can be composed of variables, integers, and the `+` operator. 

Here is one example set of equations:
```
offset = 4 + random + 1
location = 1 + origin + offset
origin = 3         + 5
random = 2
```

Your program should take a filename as input. The file contains a set of equations, like the above. The program should evaluate the set of equations and print the unsigned integer value of each variable in this format: `<variable name> = <unsigned integer value>`. The output should be sorted by in ascending order by variable name.

The output for the example above would be:
```
location = 16
offset = 7
origin = 8
random = 2
```

Keep in mind: 
- You must use Python3.
- There will be one or more white spaces between each token.
- All variables in the equation set will have a definition. 
- You may also assume a variable is only defined once and will have a valid integer solution.

Submission
----------
Please wind down your investigations if you hit the 3 hour mark, or earlier if you hit diminishing returns.

You will be judged on:
- Completeness of the output
- Correctness of the output
- Code Quality
- Comments / Documentation

Submit your submission via email with the following:
1. Source code
2. (if necessary) Instructions on how to execute your code
3. (optionally) Any thoughts you'd like to share