import unittest

from python_data_validator.validator.Validator import Validator
from python_data_validator.types.NumberType import NumberType

class TestNumberTypeValidation(unittest.TestCase):
    def test_min_with_positive_integers(self):
        set_1_schema = {"test1": NumberType().min(0)}
        set_1_test_data = {"test1": -1}

        errors = Validator.validate(set_1_schema, set_1_test_data)

        self.assertEqual(errors, {})



if __name__ == "__main__":
    unittest.main()