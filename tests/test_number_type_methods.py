import unittest

from myDataValidator.validator.Validator import Validator
from myDataValidator.types.NumberType import NumberType

class TestNumberTypeMethods(unittest.TestCase):

    def test_min_yield_pass(self):
        schema = {
            "greater_than_0": NumberType().min(0),
            "greater_than_10": NumberType().min(10),
            "greater_than_100": NumberType().min(1000)
        }
        test_data = {
            "greater_than_0": 5,
            "greater_than_10": 20,
            "greater_than_100": 5000
        }
        errors = Validator.validate(schema, test_data)
        self.assertEqual(errors, {})

    def test_min_yield_exceptions(self):
        schema = {
            "greater_than_10": NumberType().min(10),
            "greater_than_100": NumberType().min(100),
            "greater_than_1000": NumberType().min(1000)
        }
        test_data = {
            "greater_than_10": 5,
            "greater_than_100": 20,
            "greater_than_1000": 400
        }
        errors = Validator.validate(schema, test_data)
        self.assertTrue( isinstance(errors["greater_than_10"][0], Exception))
        self.assertTrue( isinstance(errors["greater_than_100"][0], Exception))
        self.assertTrue( isinstance(errors["greater_than_1000"][0], Exception))

    def test_max_yield_pass(self):
        schema = {
            "less_than_0": NumberType().max(0),
            "less_than_10": NumberType().max(10),
            "less_than_100": NumberType().max(100),
            "less_than_1000": NumberType().max(1000),
        }
        test_data = {
            "less_than_0": -100,
            "less_than_10": 5,
            "less_than_100": 50,
            "less_than_1000": 999,
        }
        errors = Validator.validate(schema, test_data)
        self.assertEqual(errors, {})

    def test_max_yield_exceptions(self):
        schema = {
            "less_than_0": NumberType().max(0),
            "less_than_10": NumberType().max(10),
            "less_than_100": NumberType().max(100),
            "less_than_1000": NumberType().max(1000),
        }
        test_data = {
            "less_than_0": 10,
            "less_than_10": 20,
            "less_than_100": 200,
            "less_than_1000": 10000,
        }
        errors = Validator.validate(schema, test_data)
        self.assertTrue( isinstance(errors["less_than_0"][0], Exception))
        self.assertTrue( isinstance(errors["less_than_10"][0], Exception))
        self.assertTrue( isinstance(errors["less_than_100"][0], Exception))
        self.assertTrue( isinstance(errors["less_than_1000"][0], Exception))

    def test_exact_yield_pass(self):
        schema = {
            "exact_0": NumberType().exact(0),
            "exact_10": NumberType().exact(10),
            "exact_100": NumberType().exact(100),
            "exact_0.1": NumberType().exact(0.1),
            "exact_0.01": NumberType().exact(0.01),
        }

        test_data = {
            "exact_0": 0,
            "exact_10": 10,
            "exact_100": 100,
            "exact_0.1": 0.1,
            "exact_0.01": 0.01,
        }

        errors = Validator.validate(schema, test_data)
        self.assertEqual(errors, {})

    def test_exact_yield_exceptions(self):
        schema = {
            "exact_0": NumberType().exact(0),
            "exact_10": NumberType().exact(10),
            "exact_100": NumberType().exact(100),
            "exact_0.1": NumberType().exact(0.1),
            "exact_0.01": NumberType().exact(0.01),
        }

        test_data = {
            "exact_0": 1,
            "exact_10": 12,
            "exact_100": -1,
            "exact_0.1": 5,
            "exact_0.01": -0.01,
        }

        errors = Validator.validate(schema, test_data)
        self.assertTrue( isinstance(errors["exact_0"][0], Exception))
        self.assertTrue( isinstance(errors["exact_10"][0], Exception))
        self.assertTrue( isinstance(errors["exact_100"][0], Exception))
        self.assertTrue( isinstance(errors["exact_0.1"][0], Exception))
        self.assertTrue( isinstance(errors["exact_0.01"][0], Exception))

    def test_positive_yield_pass(self):
        schema = {
            "test_positive_1": NumberType().positive(),
            "test_positive_2": NumberType().positive(),
        }

        test_data = {
            "test_positive_1": 100,
            "test_positive_2": 1
        }

        errors = Validator.validate(schema, test_data)
        self.assertEqual(errors, {})

    def test_positive_yield_exceptions(self):
        schema = {
            "test_positive_1": NumberType().positive(),
            "test_positive_2": NumberType().positive(),
        }

        test_data = {
            "test_positive_1": -1,
            "test_positive_2": -0.01
        }

        errors = Validator.validate(schema, test_data)
        self.assertTrue(isinstance(errors["test_positive_1"][0], Exception))
        self.assertTrue(isinstance(errors["test_positive_2"][0], Exception))

    def test_negative_yield_pass(self):
        schema = {
            "test_negative_1": NumberType().negative(),
            "test_negative_2": NumberType().negative(),
        }

        test_data = {
            "test_negative_1": -100,
            "test_negative_2": -0.01
        }

        errors = Validator.validate(schema, test_data)
        self.assertEqual(errors, {})

    def test_negative_yield_exceptions(self):
        schema = {
            "test_negative_1": NumberType().negative(),
            "test_negative_2": NumberType().negative(),
        }

        test_data = {
            "test_negative_1": 100,
            "test_negative_2": 0.01
        }

        errors = Validator.validate(schema, test_data)
        self.assertTrue( isinstance(errors["test_negative_1"][0], Exception))
        self.assertTrue( isinstance(errors["test_negative_2"][0], Exception))

    def test_multiple_yield_pass(self):
        schema = {
            "multiple_of_2": NumberType().multiple(2),
            "multiple_of_3": NumberType().multiple(3),
            "multiple_of_8": NumberType().multiple(8),
            "multiple_of_16": NumberType().multiple(16),
            "multiple_of_-2": NumberType().multiple(-2),
        }

        test_data = {
            "multiple_of_2": 4,
            "multiple_of_3": 99,
            "multiple_of_8": 24,
            "multiple_of_16": 48,
            "multiple_of_-2": 4,
        }

        errors = Validator.validate(schema, test_data)
        self.assertEqual(errors, {})

    def test_multiple_yield_exceptions(self):
        schema = {
            "multiple_of_2": NumberType().multiple(2),
            "multiple_of_3": NumberType().multiple(3),
            "multiple_of_8": NumberType().multiple(8),
            "multiple_of_16": NumberType().multiple(16),
            "multiple_of_-2": NumberType().multiple(-2),
        }

        test_data = {
            "multiple_of_2": 3,
            "multiple_of_3": 7,
            "multiple_of_8": 28,
            "multiple_of_16": 36,
            "multiple_of_-2": 7,
        }

        errors = Validator.validate(schema, test_data)
        self.assertTrue( isinstance(errors["multiple_of_2"][0], Exception))
        self.assertTrue( isinstance(errors["multiple_of_3"][0], Exception))
        self.assertTrue( isinstance(errors["multiple_of_8"][0], Exception))
        self.assertTrue( isinstance(errors["multiple_of_16"][0], Exception))
        self.assertTrue( isinstance(errors["multiple_of_-2"][0], Exception))

if __name__ == "__main__":
    unittest.main()