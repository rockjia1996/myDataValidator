import unittest

from myDataValidator.types.NumberType import NumberType
from myDataValidator.validator.Validator import Validator

class TestNumberTypeValidations(unittest.TestCase):

    def test_min_max_yield_pass(self):
        schema = {
            "1_to_10": NumberType().min(1).max(10),
            "10_to_100": NumberType().min(10).max(100),
            "-100_to_0": NumberType().min(-100).max(0),
            "-100_to_100": NumberType().min(-100).max(100)
        }

        test_data = {
            "1_to_10": 9,
            "10_to_100": 20,
            "-100_to_0": -19,
            "-100_to_100": 0
        }
        errors = Validator.validate(schema, test_data)
        self.assertEqual(errors, {})

    def test_min_max_yield_exceptions(self):
        schema = {
            "1_to_10": NumberType().min(1).max(10),
            "10_to_100": NumberType().min(10).max(100),
            "-100_to_0": NumberType().min(-100).max(0),
            "-100_to_100": NumberType().min(-100).max(100)
        }

        test_data = {
            "1_to_10": 100,
            "10_to_100": -10,
            "-100_to_0": 5,
            "-100_to_100": 400
        }
        errors = Validator.validate(schema, test_data)

        self.assertTrue(isinstance(errors["1_to_10"][0], Exception))
        self.assertTrue(isinstance(errors["10_to_100"][0], Exception))
        self.assertTrue(isinstance(errors["-100_to_0"][0], Exception))
        self.assertTrue(isinstance(errors["-100_to_100"][0], Exception))

    def test_multiple_min_max_yield_pass(self):
        schema = {
            "based_2_from_1_to_10": NumberType().min(1).max(10).multiple(2),
            "based_7_from_10_to_80": NumberType().min(10).max(80).multiple(7),
            "based_8_from_1_to_100": NumberType().min(1).max(100).multiple(8),
            "based_5_from_greater_than_100": NumberType().min(100).multiple(5),
            "based_6_from_less_than_90": NumberType().max(90).multiple(6),
        }
        test_data = {
            "based_2_from_1_to_10": 8,
            "based_7_from_10_to_80": 77,
            "based_8_from_1_to_100": 48,
            "based_5_from_greater_than_100": 550,
            "based_6_from_less_than_90": 72,
        }

        errors = Validator.validate(schema, test_data)
        self.assertEqual(errors, {})
    
    def test_multiple_min_max_yield_exception(self):
        schema = {
            "based_2_from_1_to_10": NumberType().min(1).max(10).multiple(2),
            "based_7_from_10_to_80": NumberType().min(10).max(80).multiple(7),
            "based_8_from_1_to_100": NumberType().min(1).max(100).multiple(8),
            "based_5_from_greater_than_100": NumberType().min(100).multiple(5),
            "based_6_from_less_than_90": NumberType().max(90).multiple(6),
        }
        test_data = {
            "based_2_from_1_to_10": 7,
            "based_7_from_10_to_80": 67,
            "based_8_from_1_to_100": -7,
            "based_5_from_greater_than_100": -557,
            "based_6_from_less_than_90": 37,
        }

        errors = Validator.validate(schema, test_data)

        self.assertTrue(isinstance(errors["based_2_from_1_to_10"][0], Exception))

        self.assertTrue(isinstance(errors["based_7_from_10_to_80"][0], Exception))

        self.assertTrue(isinstance(errors["based_8_from_1_to_100"][0], Exception))
        self.assertTrue(isinstance(errors["based_8_from_1_to_100"][1], Exception))
        self.assertTrue(len(errors["based_8_from_1_to_100"]) == 2)

        self.assertTrue(isinstance(errors["based_5_from_greater_than_100"][0], Exception))
        self.assertTrue(isinstance(errors["based_5_from_greater_than_100"][1], Exception))
        self.assertTrue(len(errors["based_5_from_greater_than_100"]) == 2)

        self.assertTrue(isinstance(errors["based_6_from_less_than_90"][0], Exception))
        self.assertTrue(len(errors["based_6_from_less_than_90"]) == 1) 

    def test_multiple_positive_yield_pass(self):
        schema = {
            "base_2_positive": NumberType().positive().multiple(2),
            "base_7_positive": NumberType().positive().multiple(7)
        }
        test_data = {
            "base_2_positive": 10,
            "base_7_positive": 35,
        }

        errors = Validator.validate(schema, test_data)
        self.assertEqual(errors, {})

    def test_multiple_positive_yield_exceptions(self):
        schema = {
            "base_2_positive": NumberType().positive().multiple(2),
            "base_7_positive": NumberType().positive().multiple(7)
        }
        test_data = {
            "base_2_positive": -10,
            "base_7_positive": -18,
        }

        errors = Validator.validate(schema, test_data)
        self.assertTrue( isinstance(errors["base_2_positive"][0], Exception) )

        self.assertTrue( isinstance(errors["base_7_positive"][0], Exception) )
        self.assertTrue( isinstance(errors["base_7_positive"][1], Exception) )

    def test_multiple_negative_yield_pass(self):
        schema = {
            "base_2_negative": NumberType().negative().multiple(2),
            "base_7_negative": NumberType().negative().multiple(7)
        }
        test_data = {
            "base_2_negative": -10,
            "base_7_negative": -35,
        }

        errors = Validator.validate(schema, test_data)
        self.assertEqual(errors, {})

    def test_multiple_negative_yield_exceptions(self):
        schema = {
            "base_2_negative": NumberType().negative().multiple(2),
            "base_7_negative": NumberType().negative().multiple(7)
        }
        test_data = {
            "base_2_negative": 10,
            "base_7_negative": 18,
        }

        errors = Validator.validate(schema, test_data)
        self.assertTrue( isinstance(errors["base_2_negative"][0], Exception) )

        self.assertTrue( isinstance(errors["base_7_negative"][0], Exception) )
        self.assertTrue( isinstance(errors["base_7_negative"][1], Exception) )


if __name__ == "__main__":
    unittest.main()