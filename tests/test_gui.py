import os ; os.environ["KIVY_NO_ARGS"] = "1" # hack for making tests loadable in VS Code
import unittest
from calculator.ui.gui import CalculatorApp


class CalculatorGUITestCase(unittest.TestCase):
    def setUp(self):
        self.app = CalculatorApp()
        self.app._run_prepare()

    def press_button(self, button_text):
        self.app.find_button_by(button_text).trigger_action()

    def assert_display(self, value):
        self.assertEqual(self.app.display.text, value)   

    def tearDown(self):
        self.app.stop()
    
class TestExpressions(CalculatorGUITestCase):
    express_to_be_tested = {
        "1+2": "3",
        "2-1": "1",
        "1*2": "2",
        "1/2": "0.5",
        "2**3": "8",
        "(1+3)√": "2.0",
        "(2+2)*2": "8"
    }

def test_integer_expressions(self):
    for expression, result in self.expression_to_be_tested.items():
        with self.subTest(f"express {expression} produces {result}"):
            self.press_button("C")
            for button in expression:
                self.press_button(button)
            self.press_button("=")
            self.assert_display(result)

class TestExpressions(CalculatorGUITestCase):
    def test_integer_expression(self):
        self.press_button("1")
        self.press_button("+")
        self.press_button("2")
        self.assert_display("1+2")
        self.press_button("=")
        self.assert_display("3")
        self.press_button("=")
        self.press_button("=")
        self.press_button("=")
        self.press_button("=")

    def test_float_expression(self):
        self.press_button("1")
        self.press_button(".")
        self.press_button("2")
        self.press_button("+")
        self.press_button("2")
        self.assert_display("1.2+2")
        self.press_button("=")
        self.assert_display("3.2")

    def test_sqrt_looks(self):
        self.press_button("(")
        self.press_button("1")
        self.press_button("+")
        self.press_button("3")
        self.press_button(")")
        self.press_button("√")
        self.assert_display("(1+3)√")

    def test_disposition_parenthesis_buttons(self):
        ...

class testNonFunctionalRequirements(CalculatorGUITestCase):
    list_of_buttons_supposed_to_be_present = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", ".", "C", "=", "√", "^","(",")"}
                                                       
    def test_buttons_presence(self):
        for button in self.list_of_buttons_supposed_to_be_present:
            with self.subTest("button " + button):
                #print("Pressing button: " + button)
                print(f"Pressing button: {button.encode('ascii', 'replace').decode('ascii')}")
                self.press_button(button)

    def test_button_5(self):
        self.press_button("5")
        self.assert_display("5")