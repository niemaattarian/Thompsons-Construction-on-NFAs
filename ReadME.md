# _**Niema Attarian**_

# **_G00346901@gmit.ie_**

###**OVERVIEW**
I created this GitHub repository for my Graph Theory project 2019. For my project, I was asked to write a Python program to execute regular expressions on strings using an algorithm known as Thompson's construction. In this, I have to build a non-deterministic finite automaton (NFA) from a regular expression, and can use this to check if the regular expression matches any given string text.

This project can be cloned by navigating to the clone button on GitHub. From here, you can 'cd' into the project and run the project via that 'python Project.py' command in the command window.

###**SHUNTING YARD ALGORITHM**

The purpose of the Shunting Yard Algorithm is to parse expressions from infix notations to postfix expressions or notation strings using stacks.

Firstly, special characters such as '*', '.', '?', '+', '|' are added to a dictionary and assigned a value which gives them an order of precedence. Empty 'pofix' and 'stack' strings are initialized. The stack string is where the operators are push in and out and the pofix string is where the result stored.

The 'specials' dictionary is then passed through a loop containing a series of statements that will in turn determine the output for the postfix expression.

The expression evaluation begins at the far left. If an opening bracket '(' is encountered, it is pushed to the stack. 

**_NOTE: Remember that the stack is Last In First Out (LIFO)._**

If the following encountered is a closing bracket ')' then we look at the stack. We look at the character at the top of the stack that isn't the opening bracket and begin pushing the characters of the stack to the postfix expression. We do this for characters up to but not including the last character as it is the closing bracket. Once pushed to the postfix regular expression we remove the character.

If the character is in the special dictionary, we want to push the following from the stack to the postfix regular expression.

If it isn't an open bracket, closing bracket or a special character, we append what has already been read into the postfix regular expression.

We double check at the end of the function that everything in the stack has been pushed.

###**Thompson's Construction**
Thompson's Construction is a method in which we transform a regular expression into a (NFA) non-deterministic finite automaton. This can further be used to match strings against the expression.
In this algorithm we created methods which will help execute what we intend to do.

####**Compile Method**
In this method we initially create an NFA stack which is empty. This will contain instances of the NFA class already created.
Firstly, we loop through the postfix regular expression one character at a time. We created an instance of the NFA class that has an accept state and an initial state. We join these via arrows labelled by the character.
We join the new initial state to nfa's initial state and new accept state and then join old accept state to the new accept state and nfa's initial state
Finally we append the new NFA to the NFA stack. We continue to do this with each of our characters in the dictionary.

When you run this, the user is shown the memory location of the NFA object.
