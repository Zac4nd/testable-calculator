import unittest
from calculator import Calculator


class TestCalculatorMethods(unittest.TestCase):
    def setUp(self):
        self.sut = Calculator()

    def test_initial_expression_is_empty(self):
        self.assertEqual("", self.sut.expression)

    def test_digit(self):
        for i in range(0,10):
            self.sut.digit(i)
        self.assertEqual(self.sut.expression, "0123456789")
            
    def test_wromng_digit(self):
        try:
            self.sut.digit(11)
            self.fail()
        except ValueError as e:
            self.assertIn("Value must a digit in [0, 9]: ", str(e))

    def test_wrong_digit_better(self):
        with self.assertRaises(ValueError):
            self.sut.digit(11)  

    def test_plus(self):
        self.sut.plus()
        self.assertEqual("+", self.sut.expression)

    def test_minus(self):
        self.sut.minus()
        self.assertEqual("-", self.sut.expression)
    
    def test_multiply(self):
        self.sut.multiply()
        self.assertEqual("*", self.sut.expression)
    
    def test_divide(self):
        self.sut.divide()
        self.assertEqual("/", self.sut.expression)

    def test_dot(self):
        self.sut.dot()
        self.assertEqual(".", self.sut.expression)
    
    def test_power(self):
        self.sut.power()
        self.assertEqual("**", self.sut.expression)

    def test_sqrt(self):
        self.sut.sqrt()
        #self.assertEqual("√", self.sut.expression)
        self.assertEqual("**0.5", self.sut.expression)
        #self.assertEqual("sqrt", self.sut.expression)

    def test_opening_parenthesis(self):
        self.sut.opening_parenthesis()
        self.assertEqual("(", self.sut.expression)
    
    def test_closing_parenthesis(self):
        self.sut.closing_parenthesis()
        self.assertEqual(")", self.sut.expression)

    def test_clear(self):
        self.sut.divide()
        self.sut.clear()
        self.assertEqual("", self.sut.expression)


class TestCalculatorUsage(unittest.TestCase):
    def setUp(self):
        self.sut = Calculator()

    def test_expression_insertion(self):
        self.sut.digit(1)
        self.sut.plus()
        self.sut.digit(2)
        self.sut.plus()
        self.sut.opening_parenthesis()
        self.sut.digit(2)
        self.sut.closing_parenthesis()
        self.assertEqual("1+2+(2)", self.sut.expression)

    def test_compute_result(self):
        self.sut.expression = "1+2"
        self.assertEqual(3, self.sut.compute_result())

    def test_compute_result_with_invalid_expression(self):
        self.sut.expression = "1+"
        with self.assertRaises(ValueError) as context:
            self.sut.compute_result()
        self.assertEqual("Invalid expression: 1+", str(context.exception))
