import unittest
from calculator import Calculator


class TestCalculatorMethods(unittest.TestCase):
    def setUp(self):
        self.sut = Calculator()

    def test_initial_expression_is_empty(self):
        self.assertEqual("", self.sut.expression)

    def test_digit(self):
        expected_expression = ""
        for i in range(0,10):
            self.sut.digit(i)
            expected_expression += f"{i}" 
            
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
        self.assertEqual("1+2", self.sut.expression)

    def test_compute_result(self):
        self.sut.expression = "1+2"
        self.assertEqual(3, self.sut.compute_result())

    def test_compute_result_with_invalid_expression(self):
        self.sut.expression = "1+"
        with self.assertRaises(ValueError) as context:
            self.sut.compute_result()
        self.assertEqual("Invalid expression: 1+", str(context.exception))
