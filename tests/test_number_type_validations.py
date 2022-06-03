import unittest

from python_data_validator.types.NumberType import NumberType
from python_data_validator.validator.Validator import Validator

class TestNumberTypeValidations(unittest.TestCase):
    def test_min_max(self):
        schema = {
            "1_to_10": NumberType().min(1).max(10)
        }

        test_data = {
            "1_to_10": 9
        }
        errors = Validator.validate(schema, test_data)
        self.assertEqual(errors, {})

if __name__ == "__main__":
    unittest.main()