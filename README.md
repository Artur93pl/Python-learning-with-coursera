# Python-learning-with-coursera
Learning Python with coursera course "Python for everybody".

![img.png](img.png)

Fundamentals of programing with Python with the instructor Charles Severance.

In Introduction-1 
video instructor presents fundamental concepts of programming using Python, emphasizing the importance of becoming a creator of the technology rather than just a consumer.

Introduction-2
This lecture focuses on the fundamental concepts of hardware architecture, providing definitions and an overview of key components in a computer system.

Input/Output Devices

Input/output devices allow interaction between the computer and the outside world, including peripherals like keyboards and screens.
These devices are essential for user interaction and data exchange.

Central Processing Unit (CPU) and Memory

The CPU is the brain of the computer, executing instructions at high speeds (up to three billion instructions per second).
Main memory temporarily holds data and programs while secondary memory provides permanent storage, ensuring data is retained even when the computer is off.

Introduction-3
significance in the world of programming.

Introduction to Python

Python is a programming language created by Guido van Rossum over 20 years ago, designed to be both powerful and enjoyable to use.
The name "Python" is inspired by Monty Python's Flying Circus, reflecting a playful approach to programming.

Learning Python

As beginners, learners will encounter "syntax errors," which indicate that Python does not understand the code, not a judgment of their abilities.
The journey of learning Python may be frustrating at times, but persistence will lead to understanding and mastery.

Community and Culture

Those who learn Python often refer to themselves as "Pythonistas," fostering a sense of community among learners.
The lecture encourages learners to embrace mistakes as part of the learning process and to trust in their ability to grasp the language over time.

Next module focuses on introducing learners to programming with Python and the tools available for writing and testing code.

Installing and Using Python

Learners are encouraged to install Python on their devices to write programs effectively.
For those unable to install Python, a web-based Python Playground is provided for coding practice.

Python Playground Features

The Playground allows users to write and run code without grading, offering a space for experimentation.
It includes a feature for teaching staff to view and assist with student code, enhancing support and communication.

Best Practices for Learning Python

While the Playground is useful, learners are advised to develop skills on their own devices for a more comprehensive learning experience.
The course emphasizes the importance of practicing coding in a local environment when possible.

DAY 2

Video 1:

This course content introduces the basics of the Python programming language and how to interact with it.

Getting Started with Python

Python can be started on various operating systems through a command line interface, allowing users to input commands interactively.
The first command often involves an assignment statement, such as X = 1, which stores a value in memory.

Understanding Variables and Expressions

An assignment statement assigns a value to a variable, while the print function retrieves and displays that value.
Expressions can manipulate variables, such as adding one to X and updating its value.
Programming Structure and Syntax

Python has reserved words that have specific meanings, which cannot be used as variable names.

![img_1.png](img_1.png)


Writing a program involves creating lines of code that form sentences, which can be combined into paragraphs, ultimately creating a script or program file.

Video 2:

The course content focuses on the fundamental programming concepts in Python, particularly the patterns used in constructing programs.

Sequential Steps

The most basic programming pattern is sequential, where instructions are executed one after another.
An example is provided with a simple Python program that assigns a value to a variable and prints it.

Conditional Steps

Conditional programming allows for decision-making in code using "if" statements to execute certain actions based on conditions.
A flowchart illustrates how the program evaluates conditions and executes corresponding statements.

Looping and Iteration

The repeat pattern, using loops like "while" and "for," enables the execution of code multiple times until a condition is met.
The importance of iteration variables is highlighted to prevent infinite loops, ensuring the loop runs a defined number of times.
This overview sets the stage for deeper exploration of programming concepts in subsequent chapters.

Day 3

Video 1:

The content focuses on the first assignment of the course, which involves writing a simple "Hello World" program in Python.

Assignment Overview

The assignment requires students to print "Hello World" using Python.
Students will use an autograder to check their code and receive feedback.

Using the Autograder

The autograder allows students to submit their code and see if it runs correctly.
It provides feedback on errors, such as syntax errors or output mismatches.

Grading System

The grading is pass/fail, with students receiving either 100% or 0%.
Once a grade is set, students can experiment with their code without affecting their score.
Static Analysis

The autograder performs static analysis to ensure code quality, checking for proper use of programming constructs.
Students are encouraged to understand the assignments rather than copying code from others.

Support and Communication

Students can communicate with teaching assistants for help without posting code in forums.
This approach aims to promote learning and understanding of the material.

Video 2:

This course content focuses on the foundational elements of Python programming, specifically covering constants, variables, and reserved words.

Constants and Their Types

Constants are fixed values that do not change, such as numbers (e.g., integers and floating-point) and string constants (e.g., "hello world").
String constants allow programs to communicate with users, providing a way to display messages.

Reserved Words and Their Importance

Reserved words are specific keywords in Python that have predefined meanings (e.g., class, del, else) and should not be used as variable names.
Understanding these words is crucial to avoid conflicts and ensure proper code functionality.

Variables and Assignment Statements

Variables are user-defined names that represent memory locations where data can be stored and manipulated.
Assignment statements in Python allocate memory for variables and can overwrite existing values, following specific naming rules (e.g., starting with letters or underscores).

Video 3:

The content focuses on the importance of variable naming in Python programming and how it affects code readability for humans versus the Python interpreter.

Variable Naming

Choosing sensible variable names is crucial for code clarity, even though Python does not require mnemonic names.
Consistent naming within a program is more important than the specific names chosen.

Human vs. Python Understanding

Python treats all variable names equally, regardless of their meaning, which can lead to confusion for human readers.
Using clear and descriptive names helps others understand the code's purpose and logic.

Assignment Statements

Assignment in programming differs from mathematical equality; it involves storing computed values in variables.
The process allows for expressions like x = x + 1, which is common in programming but nonsensical in mathematics.

Day 4

Video 1:

The content focuses on the complexity of assignment statements and operators in programming, particularly in Python.

![img_2.png](img_2.png)

Understanding Operators

Programming languages use various operators like addition (+), subtraction (-), multiplication (*), and division (/), which have historical roots in early computer keyboards.
The modulo operator (%) is highlighted for its importance in computing, providing the remainder of a division operation.

Order of Evaluation

There is a specific order of evaluation for operators: parentheses first, followed by exponentiation, multiplication and division, and finally addition and subtraction.
Parentheses can be used to clarify the order of operations, making code easier to read and understand.

Practical Applications

The modulo operator is useful for generating random numbers within a specific range, such as simulating dice rolls or card selections.
Understanding the order of operations is crucial for evaluating expressions correctly, especially in programming assignments.

Video 2:

The content focuses on understanding constants, variables, and their types in Python, emphasizing how Python handles different data types.

Understanding Data Types

Python tracks the type of values in variables and constants, such as integers, floating-point numbers, and strings.
The plus operator behaves differently based on the data types of its operands, performing addition for integers and concatenation for strings.

Error Handling and Type Management

When incompatible types are combined (e.g., a string and an integer), Python raises a traceback error, indicating where the issue occurred.
The type function can be used to check the type of variable or constant, helping to debug type-related issues.

Number Types and Conversions

Integers are whole numbers, while floating-point numbers include decimal points, with floating points having a wider range but less precision.
Python provides built-in functions like int() and float() to convert between types, allowing for manipulation of data as needed.

Day 5 

Video 1:

This course video item focuses on the importance of documentation in programming, particularly through the use of comments and good variable names.

Documentation and Comments

Comments are lines in code ignored by Python, used to explain what the code is doing, making it easier to understand.
Comments help the programmer (often the future self) remember the purpose and function of code sections, aiding debugging and maintenance.

Video 2:

This course video item introduces the fundamental concept of programming by demonstrating a simple Python program that performs input, processing, and output.

Key Concepts of the Program

The program solves a practical problem: converting European elevator floor numbers (where ground floor is zero) to U.S. floor numbers (where ground floor is one).
It consists of three main steps: taking input from the user, processing that input by converting and adding one, and outputting the result.

Day 6

Video 1:

In this video lecture introduces the concept of conditional execution in Python, which allows programs to make decisions and execute code selectively based on conditions.

Conditional Execution and the if Statement

The if statement enables conditional execution by evaluating a condition that returns True or False.
If the condition is True, the indented block of code following the if statement runs; otherwise, it is skipped.

Comparison Operators and Conditions

Conditions use comparison operators like <, <=, == (equality test), >=, >, and != (not equal) to form questions about values.
The double equals (==) is used to test equality, distinct from the single equals (=) which assigns values.

Indentation and Code Blocks

Indentation is crucial in Python to define blocks of code that belong to conditional statements.
Consistent indentation (usually 4 spaces) is required; mixing tabs and spaces can cause errors.
Multiple lines can be included in a conditional block by maintaining the same indentation level.

Nested Conditionals and else Clause

Conditionals can be nested inside one another to test multiple conditions sequentially.
The else clause provides an alternative block of code to execute if the if condition is False, enabling two-way decisions.
Understanding these concepts is fundamental to writing intelligent programs that can choose different execution paths based on data and conditions.

Video 2:

This course content explains how to use multi-way conditional statements in Python programming to control the flow of execution based on different conditions.

Understanding Conditional Blocks

An if-then-else structure forms a block with one entry and one exit point, where only one path of code runs based on the condition.
The block starts at the if statement and ends after the last indented line, ensuring clear logical flow.

Using elif for Multi-Way Decisions

The elif keyword allows checking multiple conditions sequentially, running only the first true condition's code block.
If none of the conditions are true, an optional else block can run as a catch-all.

Examples and Logical Flow

Conditions are checked in order; once a true condition is found, the corresponding block runs and the rest are skipped.
It is possible to have no else block, meaning no code runs if none of the conditions are met.
Logical puzzles illustrate how some conditions may never execute depending on the order and coverage of conditions.

Video 3:

The main idea of this course content is to explain the use of the try and except structure in Python for handling errors gracefully.

Understanding try and except

The try block contains code that might fail and cause a traceback error.
If the code in try works, the except block is skipped; if it fails, the except block runs instead of crashing the program.

How try and except works in practice

When a line of code inside try causes an error, Python jumps to the except block and executes that code.
This prevents the program from stopping abruptly and avoids showing a traceback error to the user.

Best practices and examples

Only put the risky lines of code inside the try block, not the entire program.
Example: converting user input to an integer inside try; if it fails, except sets a default value and continues.
This approach helps handle unexpected user input without crashing the program, making it more robust and user-friendly.


Day 7

Video 1:

This course item introduces the concept of functions in Python programming, focusing on the "store and reuse" pattern to avoid code repetition.

Functions and Their Definition

Functions allow programmers to store a block of code under a name and reuse it multiple times without rewriting it.
The keyword "def" is used to define a function, followed by the function name and parentheses; the function body is indented.

Calling and Executing Functions

Defining a function does not execute its code immediately; it only stores the function for later use.
Functions are called or invoked by using their name followed by parentheses, which executes the stored code and then returns control to the calling location.

Built-in Functions and Arguments

Python includes built-in functions like print(), input(), type(), int(), float(), max(), and min() that perform common tasks.
Functions can take arguments (inputs) and return values; for example, max() returns the largest item in a string or list.

Type Conversion and Function Behavior

Functions like int() and float() convert data types, which is useful when handling user input that is initially a string.
Function calls temporarily suspend the current operation, execute the function code, and then resume with the returned result.

Error Handling in Functions

Functions can cause errors if given inappropriate inputs, such as trying to convert a non-numeric string to an integer, which results in a traceback error.
Understanding function behavior and error handling is important for writing robust code.

Video 2:

This course content explains how to define and use functions in Python, focusing on the DEF keyword and function invocation.

Function Definition and Invocation

The DEF statement defines a function but does not execute its code immediately; the function code is stored for later use.
To run the function code, you must explicitly call or invoke the function by using its name followed by parentheses.

Function Reuse and Parameters

Defining a function allows code reuse by calling the function multiple times in different parts of the program.
Functions can accept arguments (parameters) inside the parentheses, which act as aliases for the input values during each function call.

Example of Function with Parameters

A function can use a parameter as a placeholder to perform different actions based on the input value.
When the function is called with different arguments, the parameter inside the function refers to the current argument, enabling dynamic behavior.

Video 3:

This course content explains the concept and use of functions in Python, focusing on how return statements work and how functions handle parameters and return values.

Function Return Values and Execution

The return statement in a function stops the function execution and sends back a residual value to the caller.
This residual value can be used immediately, such as within a print statement, to display or process the returned data.

Using Arguments and Return Values

Functions can take arguments (parameters) to customize their behavior and return values based on those inputs.
Examples show how different language codes passed as arguments result in different greeting messages returned and printed.

Understanding Built-in Functions and Multiple Parameters

The max function example illustrates how a function processes input, finds a result, and returns it to be used elsewhere in the program.
Functions can have multiple parameters, and the order and number of arguments in the call must match the function definition; the function can then return a computed result.

Fruitful vs. Non-fruitful Functions

Functions that return values are called fruitful functions.
Functions that do not return values are called non-fruitful functions.
Overall, this introduction aims to build a foundational understanding of functions so learners can confidently create and use them when needed.

Day 8

Video 1:

This lecture explains the concept of loops and iteration in Python programming, focusing on how computers perform repetitive tasks efficiently.

While Loops and Iteration Basics

A while loop repeatedly executes a block of code as long as a condition remains true, allowing computers to perform tasks multiple times without manual repetition.
The loop uses an iteration variable that changes each time through the loop to eventually make the condition false and stop the loop, preventing infinite loops.

Controlling Loop Execution

Infinite loops occur if the iteration variable does not change, causing the loop to run endlessly and potentially freeze the computer.
The break statement can be used inside a loop to exit immediately, while the continue statement skips the rest of the current iteration and moves to the next one.

Practical Examples and Loop Behavior

The lecture demonstrates a countdown example using a while loop that decrements a variable until it reaches zero, then prints "Blastoff!"
It also shows how to use break and continue in loops that process user input, such as exiting the loop when a specific word is entered or skipping lines starting with a certain character.
Overall, the lecture introduces indefinite loops with while, emphasizing careful control of the iteration variable and the use of break and continue to manage loop flow. It sets the stage for learning definite loops with for in the next lesson.

Day 9

Video 1:

This course content explains the concept and usage of definite loops in Python, specifically focusing on the "for" loop construct.

Definite Loops and the "for" Keyword

Definite loops iterate over a finite set of items, such as elements in a list, lines in a file, or characters in a string.
The "for" loop in Python uses an iteration variable and the keyword "in" to go through each item in the collection, executing the loop body once per item.

How the "for" Loop Works

The iteration variable takes on each successive value from the collection, and the loop body runs for each value.
Python manages the loop control, so you don't need to manually handle loop conditions or increments.
Example: looping through a list of integers or strings, printing each value.

Conceptual Understanding of the "for" Loop

The "for" loop acts as a contract to run the code block a specific number of times, with the iteration variable set to each item in turn.
It simplifies looping by abstracting the iteration logic, making code easier to write and understand.
The keyword "in" signifies membership or inclusion in the collection being iterated over.

Video 2:

This course content explains how to use loops in Python to solve problems by iterating through a set of values and progressively working towards a result.

Understanding Loop Purpose

Loops are used to process each value in a collection to find results like the largest number, smallest number, total, or count.
The goal is to set initial variables before the loop, update them during each iteration, and obtain the final answer after the loop finishes.

Human vs Computer Approach

Humans often spot the largest number visually, but computers must check each number sequentially.
The computer keeps track of the "largest so far" as it iterates through the list, updating this value when a larger number is found.

Implementing the Loop in Python

Initialize a variable (e.g., largest_so_far) before the loop to hold the current largest value.
For each number in the list, compare it to largest_so_far and update if the current number is larger.
After the loop completes, largest_so_far holds the maximum value in the list.
This approach demonstrates a common loop pattern: initialize, iterate and update, then finalize the result. The next lessons will cover similar patterns for finding minimums, counting, averaging, and summing values.

Day 10

Video 1:

This course content explains how to use loops in Python to perform common tasks such as counting, totaling, averaging, filtering, and searching.

Counting and Totals

Initialize a counter variable to zero before the loop and increment it by one each iteration to count items.
Initialize a total variable to zero and add each item’s value to it during the loop to compute a running total.

Averages and Filtering

Use both a counter and a total variable to calculate the average by dividing the total by the count after the loop.
Use an if statement inside the loop to filter items based on a condition, such as printing only values greater than 20.

Searching with Boolean Variables

Use a Boolean variable initialized to false to track if a specific value is found during the loop.
Set the Boolean to true when the value is found and optionally break the loop early since the search is complete.

Video 2:

This course content explains how to find the smallest value in a list using Python loops, building on the concept of finding the largest value.

Finding the Smallest Value

Simply changing the comparison from greater than to less than and renaming variables is not enough because starting with an initial value like -1 can cause logic errors.
Using a large initial value (e.g., 100 or 1000) is unreliable because the list might contain larger numbers, and negative numbers can break the logic.

Using None as a Flag Value

Instead of starting with a numeric value, use None to indicate that no value has been seen yet.
The first time through the loop, if the smallest value is None, assign the current number to it; afterward, compare normally to find smaller values.

Loop and Logical Operators

The "is" and "is not" operators are used to check if a variable is exactly None, which is stronger than using equality (==).
This technique of using None as a flag is a common idiom to initialize loop variables when searching for minimum or maximum values.

Summary of Loop Concepts Covered

The course also reviewed definite and indefinite loops, break and continue statements, iteration variables, and common loop idioms like counting, averaging, and finding extremes.

Day 11

Video 1:

In the video, Dr. Chuck walks through Exercise 5.1 from the Python for Everybody textbook (Chapter 5).
This example is closely related to your next Assignment: Finding the Largest and Smallest Numbers, which was originally Exercise 5.2 in the textbook.
We invite you to watch and work along with this demonstration to review key concepts from previous lectures and prepare for your upcoming assignment.

Day 12

Video 1:

This lecture from the "Python Data Structures" course focuses on understanding and manipulating strings in Python, which is essential for processing text data.

String Basics and Indexing

Strings are sequences of characters that can be indexed starting at 0, meaning the first character is at position 0.
The index operator uses square brackets to access individual characters, e.g., fruit[1] returns the second character.

Looping Through Strings

You can loop through strings using a while loop with an index variable or more simply with a for loop that iterates directly over each character.
The for loop is preferred for its simplicity and readability, automatically handling the iteration process.

String Slicing and Length

Slicing allows extracting substrings using the syntax string[start:end], where the end index is up to but not including the specified position.
The len() function returns the length of a string, which helps control loops and slicing operations.

Additional Notes

Input from users is always treated as strings and may need conversion to integers or floats for arithmetic operations.
Python handles out-of-range slicing gracefully by returning the substring up to the end without error.
The "in" keyword is useful for checking membership of characters in strings and is a powerful abstraction for iteration and condition checking.

Day 13

Video 1:

This lecture focuses on string manipulation in Python, covering fundamental operations and methods that make working with strings efficient and powerful.

String Operations and Logical Tests

The + operator concatenates strings exactly as given, without adding spaces; spaces must be explicitly included.
The in operator checks for the presence of a substring within a string, returning True or False, useful in conditional statements.

String Comparison and Object Methods

Strings can be compared using ==, <, and > based on character encoding order, with uppercase letters generally sorting before lowercase.
Strings are objects in Python with built-in methods like lower(), upper(), replace(), and find() that return modified copies without changing the original string.

Common String Methods and Usage

![img_3.png](img_3.png)

Methods like capitalize(), find(), replace(), strip(), and startswith() help manipulate and query strings effectively.
Slicing combined with find() allows extracting substrings based on dynamic positions, such as extracting parts of an email address.
Python 3 uses Unicode strings by default, improving handling of diverse character sets compared to Python 2.

Day 14

Video 1:

This lecture focuses on Exercise 6.5 from the "Python for Everybody" textbook, which teaches how to parse text strings in Python.

Parsing Text Strings

The exercise involves extracting a specific part of a string and converting it to a floating point number.
This skill is foundational for later tasks such as reading files or data from the Internet.

Using a Programming Editor and Directory Navigation

The instructor demonstrates creating and saving a Python file using the Atom editor.
Basic command line navigation is shown, including moving between directories and listing files.

String Parsing Techniques

The method involves finding the position of a colon in the string using the find() function.
Extracting the substring after the colon and converting it to a float is demonstrated.
Adjustments are made to handle spaces and ensure the correct substring is parsed.

Practical Application and Future Use

The exercise prepares learners for handling data from various sources like files, databases, and the Internet.
Emphasis is placed on the importance of string manipulation before moving on to file handling in the next chapter.

Day 15

Video 1:

This lecture introduces the concept of working with files in Python, marking a shift from temporary in-memory data to permanent storage.

Understanding File Interaction

Up to this point, programs have manipulated data only in memory, which disappears when the program ends.
Files provide a way to store data permanently on disk, allowing programs to read from and write to them.

File Types and Formats

The focus is on flat text files, which are simple files consisting of lines of text separated by newline characters.
An example file format discussed is the mailbox format (mbox.txt), commonly used to export email folders as plain text.

Opening and Handling Files in Python

Files must be opened before reading or writing, using Python's built-in open() function, which returns a file handle.
The file handle acts as a connection or porthole to the file, not the file's content itself.
Reading from or writing to the file is done through this handle, and the file should be closed when done.

Newline Characters and File Structure

Newlines (\n) are special characters that mark the end of a line and the start of a new one.
They are represented as two characters in strings but are actually a single non-printing character.
Different operating systems may use different newline conventions, but the concept remains the same.

Error Handling and Practical Notes

Attempting to open a non-existent file results in an error (traceback), which can be managed using try-except blocks.
The print function in Python automatically adds a newline at the end of output unless specified otherwise.

Video 2:

This course item explains how to work with files in Python, focusing on reading files line by line and processing their contents efficiently.

Reading Files Line by Line

A file handle in Python can be treated as a sequence of lines, allowing a for loop to iterate over each line easily.
This approach eliminates the need for manual end-of-file checks or while loops, making file reading straightforward and readable.

Counting and Searching Lines

You can count lines by initializing a counter and incrementing it inside the loop that reads each line.
Searching for specific lines is done by checking conditions like whether a line starts with a certain string, and printing or processing only those lines.

Handling Newlines and Whitespace

Lines read from a file include newline characters, which can cause extra blank lines when printed.
Using the rstrip() function removes trailing whitespace and newlines, preventing unwanted blank lines in output.

User Input and Error Handling

The filename can be read from user input to make the program flexible for different files.
Using try and except blocks helps handle errors gracefully if the file cannot be opened, avoiding program crashes and providing user-friendly messages.

Filtering Lines with Conditions

You can use if statements with continue to skip lines that do not meet criteria, making the code cleaner and easier to manage.
Searching for substrings within lines (e.g., "uct") is also possible using the in keyword.
Overall, this lecture emphasizes Python's elegant and simple approach to file handling, reading, and processing, which is essential for data manipulation tasks.