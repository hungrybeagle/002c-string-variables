## SDSS Computing Studies Python Assignment
### Assignment #002b Variable Operations with Strings (Total Marks 8)

Objectives:
* To use mathematical operators with string variables
* Explore different ways of combining variables and string literals

Remember, a string variable is one that does not contain numerical values, but instead contains words or collections of symbols.  Some of the mathematical operators that we can use with numbers can also be used with strings.

The + sign can be used to join two strings together.  These can be variables that contain strings or they can be just strings themselves.  The joining of two string
literals in this way is called "concatenation" or we are "concatenating" these string
literals.

examples:
```
word1 = "Hello"
word2 = "world"
answer = word1 + word2        
answer = word1 + " " + word2  # this one joins the 2 words together, but also adds a space in the middle

joined = "hello" + "world"    # this can also be used to join 2 strings together directly
```

The * sign can be used to repeat a string a number of times.  The format is: int * string
examples:
```
word1 = "star"
num1 = 5
answer = num1 * word1         # this example uses variables that contain an int and a word
answer = 5 * "star"           # this example uses an actual number and a string literal
```

There are times when we might want to combine a variable and a string literal in a 
print statement.  There are several ways to do so, and the method you pick may
depend on the situation or your personal preference.

Consider the following:
```
x = 6
print(x)
```
This will only print the variable, but suppose you want the output to look like this:
```
The number is 6
```

Option 1:
Convert or CAST the integer value of x into a string literal
x = 6
xv = str(x)
print("The number is " + xv)

or
x=6
print("The number is " + str(x) )


Option 2:
Use the comma to separate output in your print statement. Note: the output will always be separated by a space, so this is not as good if you wanted to not have a space there.
x = 6
print("The number is " , x)

Option 3:
Use formatted strings using the f-string
x = 6
print(f"The number is {x}")

Option 4:
Use the "end" option to not put a line break after a print statement. This is excellent if you are not sure how many things you need to add, but you want them all to be on the same line.
x = 6
print("The number is " , end="")
print(x)

### 6 Tasks

##### Task 1
Open up the file task1.py
The file contains 2 variables: noun and verb
Use the + operator to join them together and store the new value in the variable called result.  
Make sure to include a space so that when you display the output, the words contain a space
Display the new variable using the print() command
(1 points) 

##### Task 2
Copy all of task1.py and store it into a file called task2.py
Modify the existing code so that the two words are placed on different lines
Hint: You will need to use the escaped character that represents a line break
Your program still needs to have the new value stored in result and should display the output
(1 points) 

##### Task 3
Create a file called a3.py
You will create 2 variables: x and y
Store the numerical value of 5 into x
Store the string value of "donut" into y
Do not create a variable to store the result, but instead print the result directly using x and y with the multiplication operator in the print statement.
print() the result
(1 points) 

##### Task 4
Open up the file task4.py
It is not currently working because there are several errors.  
Correct the program so that it correctly displays the output:
```
This little piggy went to market.
```
(1 points) 

##### Task 5
Open up the file task5.py
It is not currently working. 
Correct the program so that it correctly displays the output:
```
here, kitty kitty kitty
```
(1 points) 

##### Task 6
Open up the file task6.py
Correct the code so that it displays the following.  Choose an appropriate command to not have the space between the $ and the wage variable
```
John earns $6 per hour
```
(1 points) 

###### Task 