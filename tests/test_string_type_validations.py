import unittest
from myDataValidator.validator.Validator import Validator
from myDataValidator.types.StringType import StringType
from myDataValidator.exceptions.ValidationError import ValidationError

class TestStringTypeValidations(unittest.TestCase):
    
    def test_min_max(self):
        schema = {
            'test1': StringType().min(5).max(32),
            'test2': StringType().min(10).max(128)
        }

        matched_data = {
            "test1": "hello world!",
            "test2": 'just a test string'
        }

        unmatched_data = {
            "test1": "this is an incredibly long string that fail the test!",
            "test2": "too short"
        }

        empty_errors = Validator.validate(schema, matched_data)
        errors = Validator.validate(schema, unmatched_data)

        self.assertEqual(empty_errors, {})
        
        self.assertIsInstance(errors["test1"][0], ValidationError)
        self.assertIsInstance(errors["test2"][0], ValidationError)
