#CLI-RPN-Calculator

## Implementation of a command-line reverse polish notation (RPN) calculator in Python3.

1. The calculator uses standard input and standard output
2. The calculator implements the four standard arithmetic operators ( +, -, *, /)
3. The calculator handles errors and recovers upon invalid input by printing 
"invalid input try again" along with the value of the number at the top of the stack
4. The calculator exits when it receives a "q" command or an end of input indicator
 (EOF / Ctrl+D)

### Implementation Details
The calculator is implemented using a stack. As numbers are input, they are pushed 
onto the top of the stack. When an arithmetic operator is input, the last 2 numbers 
added to the stack are used to complete that operation and the result is pushed back
on top of the stack. In the event of a string representation of a calculation in RPN
is input, the string is split on a space character(" "), then each element in the 
resulting list is used just as above(numbers pushed to the stack, operators calculated
then the result pushed to the stack).

Ex: `> 5 5 5 8 + + -`

results in this stack: 

>`[5, 5, 5, 8]` + 
>
>`[5, 5, 13]` + 
>
>`[5, 18]` - 
>
>`[-13]` 

The implementation is broken into 2 methods:

1. calculator()

    This method takes in user input and checks to see if it is a integer, float, operator, "q" or EOF, 
or any other string. As explained above, any numbers, either integer or float, are added to the 
stack. In the case of an operator, it will use the last 2 numbers added to the stack to perform
the calculation. In the case of a "q" or EOF, the calculator will quit. In the last case, any 
other string, this method calls the inline_calculator() method below, passing in the string as 
a list, split on space (" "), as well as the stack of numbers that is being used to track the 
numbers that have been input.
    
2. inline_calculator(input_list, nums)

    This method takes the list input from the calculator() method and loops through it pushing
the numbers to the stack and using any operators for calculations, just as the above method.

### Implementation Trade-offs
This calculator was built for people who are comfortable with UNIX-like CLI utilities. It also 
currently only supports the basic 4 operators. Eventually implementing more operators, such as 
mod, exponents, etc, would be useful. An alternate user interface would also be a good
future addition.

Another possible update could be finding a way to combine the calculator() method and the 
inline_calculator() method, since both methods do most of the same work. By combining these into
a single method, one could minimize the changes needed to make an update such as adding new 
operators. It will also make it easier to change the user interface in the future. For instance,
instead of passing in an input_list to the inline_calculator method, one could pass in a file.

### Example Input/Output
5 + 8 = 13
```
> 5 
5
> 8
8
> +
13
```
--------------

5 - (5 + (5 + 8)) = -13

-13 + 13 = 0
```
> 5 5 5 8 + + -
-13
> 13 +
0
```
--------------

-3 * -2 = 6

6 + 5 = 11
```
> -3
-3
> -2
-2
> *
6
> 5
5
> +
11
```
--------------

5 / (9 - 1) = 0.625
```
> 5
5
> 9
9
> 1
1
> -
8
> /
0.625
```
--------------

(2 - (4 + (-6 + 8))) * 10
```
> 2 4 -6 8 + + - 10 *
-40
```
--------------

(0.5 - (1.5 + (-2.5 + 3.5))) * 4.5
```
> 0.5 1.5 -2.5 3.5 + + - 4.5 *
-9.0
```