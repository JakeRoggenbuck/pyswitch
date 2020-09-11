from pyswitch import switch


# Make test cases
def a(): print("Hey")
def b(p): print(p)
def c(p1, p2): print(f"{p1} {p2}")


# Make switch
my_switch = switch.Switch()
# Add cases with key and function
my_switch.case(1, a)
my_switch.case(2, b)
my_switch.case(3, c)

# Get input
num = input("Num: ")
# Switch to input
my_switch.switch(num)
