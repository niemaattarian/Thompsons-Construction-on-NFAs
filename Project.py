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
  specials = {'*': 60, '+': 60, '?': 60, '.': 40, '|': 20}

  # Initializing empty pofix and stack strings
  pofix = ""
  stack = "" # Here we push operators in or out

  # This function reads the infix regular
  # expression one character at a time
  for c in infix:
    # Determining whether the character is an opening bracket
    if c == '(':
      stack = stack + c # if 'c' == '(', then add it to the stack
    # Determining whether the next character is a closing bracket
    elif c == ')':
      # while the end of the stack is not an opening bracket

      while stack[-1] != '(': # [-1] denotes any character at the end of the string
        pofix = pofix + stack[-1] # places the character at the end of the stack in the pofix expression
        # Popping the stack - Removes the second-last character
        stack = stack[:-1] # [:-1] denotes up to or including the last character
      stack = stack[:-1] # removes the open bracket in the stack
    # Determine whether the character is in the 'specials' dictionary
    elif c in specials:
      while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
        pofix = pofix + stack[-1]
        stack = stack[:-1]
      stack = stack + c
    else:
      # Appending the character read in
      # from the infix regular expression into
      # the pofix regualr expression
      pofix = pofix + c

  while stack:
    pofix = pofix + stack[-1]
    stack = stack[:-1]
  stack = stack[:-1]

  # returns pofix argument
  return pofix

# Examples
print(shunt("(a.b)|(c*.d)"))
print(shunt("(a|b.c).c*"))

# Thompsons construction Algorithm

# State class - Represents a state with two arrows,
# labelled by label.
class state:
  # Note that each variable have been
  # set to none to assign no value to each.
  label = None
  edge1 = None
  edge2 = None

# Nfa class
class nfa:
  initial = None # initial nfa state
  accept = None # single accept nfa state

  # Constructor inside nfa
  def __init__(self, initial, accept): # self represents the current instance of the class
    self.initial = initial
    self.accept = accept

# Compile function - this takes the postfix
# regular expression as the argument
def compile(pofix):
  nfastack = [] # empty list

  # looping through the postfix expression
  # one character at a time
  for c in pofix:
    # If c is the 'concatenate' operator
    if c == '.':
      nfa2 = nfastack.pop() # goes to stack, modifies array and returns it back
      nfa1 = nfastack.pop() # NOTE: stacks a re L.I.F.O.

      nfa1.accept.edge1 = nfa2.initial # Merging the accept state of nfa1 to the initial state of nfa2

      newnfa = nfa(nfa1.initial, nfa2.accept) # This is now the new nfa
      nfastack.append(newnfa) # Appending the new nfa to the stack

    # If c is the 'or' operator
    elif c == '|':
      nfa2 = nfastack.pop() # Popping NFA's off the stack
      nfa1 = nfastack.pop()

      initial = state() # creates the initial state
      initial.edge1 = nfa1.initial
      initial.edge2 = nfa2.initial
      accept = state() # creates new accept state connecting the accept states

      nfa1.accept.edge1 = accept #
      nfa2.accept.edge1 = accept

      newnfa = nfa(initial, accept)
      nfastack.append(newnfa)

    # If c is the 'kleene star' operator
    elif c == '*':
      # Pop single nfa from the stack
      nfa1 = nfastack.pop()

      # Creating new initial and accept state
      initial = state()
      accept = state()

      # Join the new initial state to nfa's
      # initial state and new accept state
      initial.edge1 = nfa1.initial
      initial.edge2 = accept

      # Join old accept state to the new accept state and nfa's initial state
      nfa1.accept.edge1 = nfa1.initial
      nfa1.accept.edge2 = accept

      newnfa = nfa(initial, accept)
      nfastack.append(newnfa) # Appending new nfa to the stack

    # if c is the '?' operator
    elif c == '?':
      # Pop single nfa from the stack
      nfa1 = nfastack.pop()

      # Creating new initial and accept state
      initial = state()
      accept = state()

      # Join the new initial state to nfa's
      # initial state and new accept state
      initial.edge1 = nfa1.initial
      initial.edge2 = accept

      # Join old accept state to the new accept state and nfa's initial state
      nfa1.accept.edge1 = nfa1.initial
      nfa1.accept.edge2 = accept

      newnfa = nfa(initial, accept)
      nfastack.append(newnfa) # Appending new nfa to the stack

    # If c is the 'plus' operator
    elif c == '+':
      # Pop single nfa from the stack
      nfa1 = nfastack.pop()

      # Creating new initial and accept state
      initial = state()
      accept = state()

      # Join the new initial state to nfa's
      # initial state and new accept state
      initial.edge1 = nfa1.initial
      initial.edge2 = accept

      # Join old accept state to the new accept state and nfa's initial state
      nfa1.accept.edge1 = nfa1.initial
      nfa1.accept.edge2 = accept

      newnfa = nfa(initial, accept)
      nfastack.append(newnfa)  # Appending new nfa to the stack

    else:
      accept = state() # accept state - creating a new instance of the class
      initial = state() # initial state

      initial.label = c # joins the initial to a character
      initial.edgel = accept # edge1 is a pointer which points to the accept state

      newnfa = nfa(initial, accept)
      nfastack.append(newnfa)

  # at this point, nfastack should have a single nfa on it
  return nfastack.pop()

# Examples
print(compile("ab.cd.|"))
print(compile("aa.*"))
print(compile("a?a.c*"))
print(compile("(b.d)|(c+a*)."))


def followes(state):
  state = set()
  state.add(state)

  if state.label is None:
    if state.edge1 is not None:
      state |= followes(state.edge1)

    if state.edge2 is not None:
      state |= followes(state.edge2)

  return state

def match(infix, string):
  pofix = shunt(infix)
  nfa = compile(pofix)

  current = set()
  nexts = set()

  current |= followes(nfa.initial)

  for s in string:
    for c in current:
      if c.label == s:

        nexts |= followes(c.edge1)

    current = nexts
    nexts = set()

  return (nfa.accept in  current)

infixes = ["a.b.c*", "a.(b|d).c*", "(a.b|d))*", "a.(b.b)*.c"]
strings = ["", "abc", "abbc", "abcc", "abad", "abbbc"]

for i in infixes:
  for s in strings:
    print(match(i, s), i, s)
