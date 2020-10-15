_**Niema Attarian**_

**_G00346901@gmit.ie_**

**OVERVIEW**
I created this GitHub repository for my Graph Theory project 2019. For my project, I was asked to write a Python program to execute regular expressions on strings using an algorithm known as Thompson's construction. In this, I have to build a non-deterministic finite automaton (NFA) from a regular expression, and can use this to check if the regular expression matches any given string text.

This project can be cloned by navigating to the clone button on GitHub. From here, you can 'cd' into the project and run the project via that 'python Project.py' command in the command window.

**SHUNTING YARD ALGORITHM**

The purpose of the Shunting Yard Algorithm is to parse expressions from infix notations to postfix expressions or notation strings using stacks.

Firstly, special characters such as '*', '.', '?', '+', '|' are added to a dictionary and assigned a value which gives them an order of precedence. Empty 'pofix' and 'stack' strings are initialized. The stack string is where the operators are push in and out and the pofix string is where the result stored.

The 'specials' dictionary is then passed through a loop containing a series of statements that will in turn determine the output for the postfix expression.

The expression evaluation begins at the far left. If an opening bracket '(' is encountered, it is pushed to the stack. 

**_NOTE: Remember that the stack is Last In First Out (LIFO)._**

If the following encountered is a closing bracket ')' then we look at the stack. We look at the character at the top of the stack that isn't the opening bracket and begin pushing the characters of the stack to the postfix expression. We do this for characters up to but not including the last character as it is the closing bracket. Once pushed to the postfix regular expression we remove the character.

If the character is in the special dictionary, we want to push the following from the stack to the postfix regular expression.

If it isn't an open bracket, closing bracket or a special character, we append what has already been read into the postfix regular expression.

We double check at the end of the function that everything in the stack has been pushed.

**Thompson's Construction**
Thompson's Construction is a method in which we transform a regular expression into a (NFA) non-deterministic finite automaton. This can further be used to match strings against the expression.
In this algorithm we created methods which will help execute what we intend to do.

#**Compile Method**
In this method we initially create an NFA stack which is empty. This will contain instances of the NFA class already created.
Firstly, we loop through the postfix regular expression one character at a time. We created an instance of the NFA class that has an accept state and an initial state. We join these via arrows labelled by the character.
We join the new initial state to nfa's initial state and new accept state and then join old accept state to the new accept state and nfa's initial state
Finally we append the new NFA to the NFA stack. We continue to do this with each of our characters in the dictionary.

When you run this, the user is shown the memory location of the NFA object.

**Matching Regular Expressions**

**Followes Function**
This helper function returns the set of states that can be reached from the state following 'e' arrows.
We do this by creating a new set with state as its only member.
We check if the state has arrows labeled e from it and we do this by looking for states where the label is 'None'.
If the states are labelled 'None' then we use nested if statement to follow the edges, 1 and 2.

**Match Function**
This function takes the regular expression, changes it to infix and compiles the postfix regular expression to an NFA.
We then create empty sets, 'current' and 'nexts' and loop through each character in the string and inside that loop we loop through the current set of states that we have.
We check if the state is labelled 's', if so, we add it into the 'next' set. That next state has now been set as a current state and the next state is cleared and is now a empty set.
We then check if the accept state is in the set of current states

Finally, we have a nested for loop which checks if the regular expression matches the string giving out a 'true' or 'false' output.


**Research**
In doing this project, I had no previous experience with Python so I knew that my research must be in depth. I completed this project over the course of a few weeks we continual practise of Python.

What I found most helpful were the videos uploaded to LearnOnline. My approach was to first understand the Algorithms on paper before coding. This would give me an understanding of the structure of the code and not seem clueless as to method of what is going on. Once I coded the algorithms, I went back to the on paper explanation to compare and walk-through step by step, side by side to try and get a full understanding of the code.

Furthermore, I researched online about each algorithm and found Wikipedia tobe very useful with it's diagrams and examples.

**_Reference links:_**
https://en.wikipedia.org/wiki/Thompson%27s_construction#Rules

https://en.wikipedia.org/wiki/Shunting-yard_algorithm#The_algorithm_in_detail

https://en.wikipedia.org/wiki/Shunting-yard_algorithm#Detailed_example

http://www.oxfordmathcenter.com/drupal7/node/628

https://swtch.com/~rsc/regexp/regexp1.html

https://web.microsoftstream.com/video/5e2a482a-b1c9-48a3-b183-19eb8362abc9

https://web.microsoftstream.com/video/cfc9f4a2-d34f-4cde-afba-063797493a90

https://web.microsoftstream.com/video/6b4ba6a4-01b7-4bde-8f85-b4b96abc902a

https://web.microsoftstream.com/video/946a7826-e536-4295-b050-857975162e6c

https://web.microsoftstream.com/video/1b3e7f4f-69e0-4316-853f-c63b14f9c36a
