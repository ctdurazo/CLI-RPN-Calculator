# CLI-RPN-Calculator

## Implementation of a command-line Reverse Polish Notation (RPN) calculator in Python3.
1. The calculator uses standard input and standard output.
2. The calculator implements the four standard arithmetic operators (+, -, *, /), as
well as modulus(%) and exponents(^).
3. The calculator handles errors and recovers upon invalid input by printing 
"invalid input try again" along with the value of the number at the top of the stack.
4. The calculator exits when it receives a "q" command or an end of input indicator
 (EOF / Ctrl+D).
 
## Use
1. CLI version

    In your terminal/command-line run `python3 rpn.py`.
    
    This will open up the CLI version directly in your current terminal, where you can
paste or type in your equations. There are some examples of inputs and outputs for this
version below.
    
2. GUI version

    To run the GUI version you must first install Kivy. I did this using a python virtual 
environment and pip. To create the virtual environment run `python3 -m venv venv` in 
your terminal/command-line from the project folder. Then you can run `sh frontend.sh`.
    
    This will open a calculator window where you can paste or type in your equations to 
the output area, or use the buttons to input your equation. In order for the equations
to register correctly, remember to use the space button between each input.
    
### Implementation Details
The calculator is implemented using a stack. As numbers are entered, they are pushed 
onto the top of the stack. When an arithmetic operator is entered, the last 2 numbers
added to the stack are used to complete that operation and the result is pushed back
on top of the stack. In the event of a string representation of a calculation in RPN
is entered, the string is split on any whitespace, then each element in the 
resulting list is used just as above (numbers pushed to the stack, operators calculated,
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

1. calculator(String, List)

    This method takes in a String, splits it into a list delimited by whitespace, then checks 
to see if each list item is an integer, float, operator, "q" or EOF. As explained above, any 
numbers, either integer or float, are added to the stack. In the case of an operator, it will
call the get_operators method, which uses the last 2 numbers added to the stack to perform the 
calculation. In the case of a "q" or EOF, the calculator will quit.

2. get_operators(String, List)

    This method takes in a String that doesn't match either an integer, float, or "q" or EOF. 
It then determines if it is one of the supported operators, or if it is an invalid input. In
the case of a supported operator, it will pop the last 2 numbers that were added to the stack,
perform the calculation, then push the result to the top of the stack. 

### Implementation Trade-offs
This calculator was built for people who are comfortable with UNIX-like CLI utilities. It also 
currently only supports the basic 4 operators plus 2 other common operators, modulus and exponents.
Eventually implementing more operators could be useful. An alternate user interface would also be a good
future addition.

In version 1, this calculator used 2 methods to handle the possible user input styles, inline vs. single 
value input. This was updated to combine the calculator() and the 
inline_calculator() methods, since both methods did most of the same work. By combining these into
a single method, I was able to minimize the changes needed to make an update such as adding new 
operators. Along with this I made the operators logic its own method to make it a little bit more easily
readable. While adding this get_operators() method, I also implemented a couple new common operators, 
modulus and exponents. This change should also make it easier to change the user interface in the future. 
For instance, instead of passing in an input_list to the inline_calculator method, one could now pass in 
any string representation, whether that is from a file, a websocket, etc.

### Front-End Addition
I have created an example front-end for this application using a Python GUI framework called Kivy. The design
for this is loosely based off of the Calculator App built into iOS. This was the first app I have made using 
the Kivy framework and I found it to be a pretty easy framework to get started with quickly. In order to use
Kivy, you must first install it. I did this using a python virtual environment and pip. To create the virtual
environment type `python3 -m venv venv` in the terminal from the project folder. From here you can run 
`sh frontend.sh`, which will install Kivy and start the calculator application, or you can run the following 
to install Kivy using pip:
```
source venv/bin/activate
pip install -r requirements.txt
```

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

(2 - (4 + (-6 + 8))) * 10 = -40
```
> 2 4 -6 8 + + - 10 *
-40
```
--------------

(0.5 - (1.5 + (-2.5 + 3.5))) * 4.5 = -9
```
> 0.5 1.5 -2.5 3.5 + + - 4.5 *
-9.0
```
--------------

2 ^ 2 = 4
4 + 6 = 10
10 % 3 = 1
```
> 2 2 ^
4
> 6 + 
10
> 3 %
1
>
```
