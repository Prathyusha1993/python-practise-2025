# an inner function that captures varibales from its enclosing scope.
def make_multiplier(k):
    def mul(x):
        return k * x
    return  mul

double = make_multiplier(2)
print(double(20))

# late binding gotcha (common interview trap)
funcs =[]
for i in range(3):
    funcs.append(lambda: i)   #all capture same i
[f() for f in funcs]    #[2,2,2]

#fix with defaultt arg(early binding)
# funcs = []
# for i in range(3):
    # funcs.append(lambda i=i: i)
# [f() for f in funcs]