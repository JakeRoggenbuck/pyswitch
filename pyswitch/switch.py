class Switch:
    def __init__(self):
        self.cases = {}

    def case(self, case, function, parameters=None):
        self.cases[str(case)] = {"name": function, "parameters": parameters}

    def switch(self, case):
        if self.cases.get(str(case)):
            func = self.cases[str(case)]
            func_name = func['name']
            if func["parameters"] is not None:
                return func_name(*func["parameters"])
            else:
                return func_name()
