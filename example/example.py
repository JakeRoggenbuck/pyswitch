from pyswitch import switch


# Make case functions
def a(): print("Hey")
def b(p): print(p)
def c(p1, p2): print(f"{p1} {p2}")


# Make switch
my_switch = switch.Switch()
# Add cases with key and function
my_switch.case("test", a)
my_switch.case(2, b, ["endow"])
my_switch.case("3", c, ["nala", "simba"])

# Get input
num = input("Num: ")
# Switch to input
my_switch.switch(num)
