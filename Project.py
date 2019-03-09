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
  specials = {'*': 60, '.': 40, '|': 20}

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
      pofix = pofix + c # Appending the character read in from the infix regular expression into the pofix regualr expression

  while stack:
    pofix = pofix + stack[-1]
    stack = stack[:-1]
  stack = stack[:-1]

  # returns pofix argument
  return pofix

print(shunt("(a.b)|(c*.d)"))

# Thompsons construction Algorithm

class state:
  label = None
  edge1 = None
  edge2 = None

class nfa:
  initial = None
  accept = None

  def __init__(self, initial, accept):
    self.initial = initial
    self.accept = accept

def compile(pofix):
  nfastack = []

  for c in pofix:
    if c == '*':
      nfa1.nfastack.pop()
      initial = state()
      accept = state()
      initial.edge1 = nfa1.initial
      initial.edge2 = accept
      nfa1.accept.edge1 = nfa.initial
      nfa1.accept.edge2 = accept
      nfastack.append(nfa(initial, accept))

      newnfa = nfa(initial, accept)
      nfastack.append(newnfa)

    elif c == '.':
      nfa2 = nfastack.pop()
      nfa1 = nfastack.pop()
      nfa1.accept.edge1 = nfa2.initial
      newnfa = nfa(nfa1.initial, nfa2.accept)
      nfastack.append(newnfa)

    elif c == '|':
      nfa2 = nfastack.pop()
      nfa1 = nfastack.pop()

      initial = state()
      initial.edge1 = nfa1.initial
      initial.edge2 = nfa2.initial
      accept = state()

      nfa1.accept.edge1 = accept
      nfa2.accept.edge1 = accept

      newnfa = nfa(initial, accept)
      nfastack.append(newnfa)

    else:
      accept = state()
      initial = state()
      initial.label = c
      initial.edgel = accept
      newnfa = nfa(initial, accept)
      nfastack.append(newnfa)

  return nfastack.pop()

print(compile("ab.cd.|"))
print(compile("aa.*"))
