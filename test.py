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
    if c == '.':
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
      nfa2.accept.edge2 = accept

      newnfa = nfa(initial, accept)
      nfastack.append(newnfa)

    elif c == '*':
      nfa1 = nfastack.pop()

      initial = state()
      accept = state()

      initial.edge1 = nfa1.initial
      initial.edge2 = accept

      nfa1.accept.edge1 = nfa1.initial
      nfa1.accept.edge2 = accept

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


##########################


def followes(state):
  states = set()
  states.add(state)

  if state.label is None:
    if state.edge1 is not None:
      states |= followes(state.edge1)

    if state.edge2 is not None:
      states |= followes(state.edge2)

  return states

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


