import unittest


class TestSwitch(unittest.TestCase):
    def setUp(self):
        from src.switch import Switch
        self.name = "switch_name"
        self.new_switch = Switch(self.name)

    def test_attr(self):
        assert self.new_switch.name == self.name
        assert self.new_switch.cases == {}

    def test_single_case_add(self):
        def a1(): return "hey"
        self.new_switch.case_add(1, a1)
        assert self.new_switch.cases['1']['name'] == a1
        assert self.new_switch.cases['1']['parameters'] is None
        assert self.new_switch.switch(1) == "hey"

        def a2(): return 254
        self.new_switch.case_add(1, a2)
        assert self.new_switch.cases['1']['name'] == a2
        assert self.new_switch.cases['1']['parameters'] is None
        assert self.new_switch.switch(1) == 254

    def test_multi_case_add(self):
        def b1(p1, p2): return f"{p1} {p2}"
        parameters = ["Test", "Yeet"]
        self.new_switch.case_add(2, b1, parameters)
        assert self.new_switch.cases['2']['name'] == b1
        assert self.new_switch.cases['2']['parameters'] is parameters
        assert self.new_switch.switch(2) == f"{parameters[0]} {parameters[1]}"

        def b2(p1, p2): return f"{p1} -- {p2}"
        parameters = ["Name One", "Name Two"]
        self.new_switch.case_add(2, b2, parameters)
        assert self.new_switch.cases['2']['name'] == b2
        assert self.new_switch.cases['2']['parameters'] is parameters
        assert self.new_switch.switch(2) == f"{parameters[0]} -- {parameters[1]}"

