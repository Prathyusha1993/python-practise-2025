# Functions that produce a sequence lazily (on-demand) using yield. They don’t build the entire result in memory.

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(3):
    print(x)

# yield pauses and resumes the function, returning one item at a time.
# return inside a generator ends the sequence (optionally with a value captured as StopIteration.value—rarely used directly).

# generator expressions (lazy)
gen = (n*n for n in range(1_000_000))
next(gen)

# yield from (delegate to subgenerator)
def flat(iterables):
    for it in iterables:
        yield from it

list(flat[[1,2,3],[4,5]])