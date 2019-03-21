# Niema Attarian
# G00346901

# Shunting Yard Algorithm

# Shunt() function containing the string
# argument 'infix' - regular expression
def shunt(infix):
  # Dictionary for special characters gives them an order of precedence
  # * = 0 or more
  # + = 1 or more
  # ? = 0 or 1
  # | = or
  # . = concatenate
  specials = {'*': 60, '+': 55, '?': 50, '.': 40, '|': 20}

  # Initializing empty pofix and stack strings
  pofix, stack = "", ""  # Here we push operators in or out

  # This function reads the infix regular
  # expression one character at a time
  for c in infix:
    # Determining whether the character is an opening bracket
    if c == '(':
      stack = stack + c  # if 'c' == '(', then add it to the stack
    # Determining whether the next character is a closing bracket
    elif c == ')':
      # while the end of the stack is not an opening bracket
      while stack[-1] != '(':  # [-1] denotes any character at the end of the string
        pofix = pofix + stack[-1]  # places the character at the end of the stack in the pofix expression
        # Popping the stack - Removes the second-last character
        stack = stack[:-1]  # [:-1] denotes up to or including the last character
      stack = stack[:-1]  # removes the open bracket in the stack
    # Determine whether the character is in the 'specials' dictionary
    elif c in specials:
      while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
        pofix, stack = pofix + stack[-1], stack[:-1]
      stack = stack + c

    else:
      # Appending the character read in
      # from the infix regular expression into
      # the pofix regualr expression
      pofix = pofix + c

  while stack:
    pofix, stack = pofix + stack[-1], stack[:-1]

  # returns pofix argument
  return pofix

# Examples
# print(shunt("(a.b)|(c*.d)"))
# print(shunt("(a|b.c).c*"))

# Thompsons construction Algorithm

# State class - Represents a state with two arrows, labelled by label.
class state:
  # Note that each variable have been
  # set to none to assign no value to each.
  label, edge1, edge2 = None, None, None


# NFA class
class nfa:
  # initial nfa state, single accept state
  initial, accept = None, None

  # NFA constructor
  def __init__(self, initial, accept):
    self.initial, self.accept = initial, accept


# Compile function - this takes the postfix
# regular expression as the argument
def compile(pofix):
  # Creates new empty set
  nfaStack = []

  # looping through the postfix expression
  # one character at a time
  for c in pofix:
    # If c is the 'kleene star' operator
    if c == '*':
      # Pops single NFA from the stack
      nfa1 = nfaStack.pop()
      # Creating new initial and accept state
      initial, accept = state(), state()
      # Join the new initial state to nfa's
      # initial state and new accept state
      initial.edge1, initial.edge2 = nfa1.initial, accept
      # Join old accept state to the new accept state and nfa's initial state
      nfa1.accept.edge1, nfa1.accept.edge2 = nfa1.initial, accept
      # Pushes the new NFA to the stack
      nfaStack.append(nfa(initial, accept))
    # If c is the 'concatenate' operator
    elif c == '.':
      # Popping the stack, NOTE: stacks are L.I.F.O.
      nfa2, nfa1 = nfaStack.pop(), nfaStack.pop()
      # Merging the accept state of nfa1 to the initial state of nfa2
      nfa1.accept.edge1 = nfa2.initial
      # Appending the new nfa to the stack
      nfaStack.append(nfa(nfa1.initial, nfa2.accept))
    # If c is the 'or' operator
    elif c == '|':
      # Popping the stack
      nfa2, nfa1 = nfaStack.pop(), nfaStack.pop()
      # creates the initial state
      initial = state()
      initial.edge1, initial.edge2 = nfa1.initial, nfa2.initial
      # creates new accept state connecting the accept states
      accept = state()
      # Connects the new Accept state to the two NFA's popped from the stack
      nfa1.accept.edge1, nfa2.accept.edge1 = accept, accept
      # Pushes the new NFA to the stack
      nfaStack.append(nfa(initial, accept))
    # If c is the 'plus' operator
    elif c == '+':
      # Pops single NFA from the stack
      nfa1 = nfaStack.pop()
      # Creating new initial and accept state
      accept, initial = state(), state()
      # Join the new initial state to nfa's
      # initial state and new accept state
      initial.edge1 = nfa1.initial
      # Join old accept state to the new accept state and nfa's initial state
      nfa1.accept.edge1, nfa1.accept.edge2 = nfa1.initial, accept
      # Pushes the new NFA to the stack
      nfaStack.append(nfa(initial, accept))
    # if c is the '?' operator
    elif c == '?':
      # Pops a single NFA from the stack
      nfa1 = nfaStack.pop()
      # Creates new initial and accept states for the new NFA
      accept, initial = state(), state()
      # Joins the new accept state to the accept state of nfa1 and the new
      # initial state to the initial state of nfa1
      # Accept connected to inital because empty is acceptable
      initial.edge1, initial.edge2 = nfa1.initial, accept
      # Joins the old accept state to the new accept state
      nfa1.accept.edge1 = accept
      # Pushes the new NFA to the stack
      nfaStack.append(nfa(initial, accept))
    else:
      # accept state, initial state - creating a new instance of the class
      accept, initial = state(), state()
      # joins the initial to a character, edge1 is a pointer which points to the accept state
      initial.label, initial.edge1 = c, accept
      # Appends the new NFA to the stack
      nfaStack.append(nfa(initial, accept))

  # at this point, nfastack should have a single nfa on it
  return nfaStack.pop()


# Examples
# print(compile("ab.cd.|"))
# print(compile("aa.*"))
# print(compile("a?a.c*"))
# print(compile("(b.d)|(c+a*)."))

# Helper function - Returns set of states that can be reached from state following e arrows
def followes(state):
  # Create a new set, with state as its only member
  states = set()
  states.add(state)

  # Check if state has arrows labelled e from it
  if state.label is None:
    # If there's an 'edge1', follow it
    if state.edge1 is not None:
      states |= followes(state.edge1)
    # If there's an 'edge2', follow it
    if state.edge2 is not None:
      states |= followes(state.edge2)

  # Returns the set of states
  return states


# Matches a string to an infix regular expression
def match(infix, string):
  # Shunt and compile the regular expression
  postfix = shunt(infix)
  nfa = compile(postfix)

  # The current set of states and the next set of states
  current = set()
  nexts = set()

  # Add the initial state to the current set
  current |= followes(nfa.initial)

  # loop through each character in the string
  for s in string:
    # loop through the current set of states
    for c in current:
      # Check to see if state is labelled 's'
      if c.label == s:
        nexts |= followes(c.edge1)
    # set current to next and clears out next
    current = nexts
    # next is back to an empty set
    nexts = set()

  # Checks if the accept state is in the set for current state
  return (nfa.accept in current)


# Testcases for the matchString function
infixes = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c"]
strings = ["", "abc", "abbc", "abcc", "abad", "abbbc"]

for i in infixes:
  for s in strings:
    print(match(i, s), i, s)
