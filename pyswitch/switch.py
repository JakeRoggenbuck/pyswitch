class Switch:
    def __init__(self):
        self.cases = {}

    def case(self, case, function, parameters=None):
        self.cases[str(case)] = {"name": function, "parameters": parameters}

    def switch(self, case):
        if (func := self.cases.get(str(case))):
            name = func['name']
            if func["parameters"] is not None:
                return name(*func["parameters"])
            else:
                return name()
