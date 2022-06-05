import unittest
import re
from python_data_validator.validator.Validator import Validator
from python_data_validator.types.StringType import StringType

class TestStringTypeMethods(unittest.TestCase):

    def test_min(self):
        schema = {
            "min_3": StringType().min(3),
            "min_10": StringType().min(10),
            "min_20": StringType().min(20),
        }
        matched_data = {
            "min_3": "hello",
            "min_10": "hello world!",
            "min_20": "this is a very very long sentence that supposely pass"
        }

        unmatched_data = {
            "min_3": "hi",
            "min_10": "HiWorld",
            "min_20": "short phrase"
        }

        empty_errors = Validator.validate(schema, matched_data)
        errors = Validator.validate(schema, unmatched_data)

        self.assertEqual(empty_errors, {})

        self.assertTrue( isinstance(errors["min_3"][0], Exception))
        self.assertTrue( isinstance(errors["min_10"][0], Exception))
        self.assertTrue( isinstance(errors["min_20"][0], Exception))

    def test_max(self):
        schema = {
            "max_3": StringType().max(3),
            "max_10": StringType().max(10),
            "max_20": StringType().max(20),
        }

        matched_data = {
            "max_3": "hi",
            "max_10": "hi!world",
            "max_20": "lessthan20"
        }

        unmatched_data = {
            "max_3": "hello",
            "max_10": "hello world!",
            "max_20": "very very very long string to fail the test"
        }

        empty_errors = Validator.validate(schema, matched_data)
        errors = Validator.validate(schema, unmatched_data)

        self.assertEqual(empty_errors, {})

        self.assertTrue( isinstance(errors["max_3"][0], Exception))
        self.assertTrue( isinstance(errors["max_10"][0], Exception))
        self.assertTrue( isinstance(errors["max_20"][0], Exception))

    def test_length(self):
        schema = {
            "length_1": StringType().length(1),
            "length_10": StringType().length(10),
            "length_20": StringType().length(20)
        }
        matched_data = {
            "length_1": "K",
            "length_10": "helloworld",
            "length_20": "helloworldhelloworld"
        }
        unmatched_data = {
            "length_1": "HELLO",
            "length_10": "helloworld!",
            "length_20": "helloworldhello!"
        }
        empty_errors = Validator.validate(schema, matched_data)
        errors = Validator.validate(schema, unmatched_data)
        self.assertEqual(empty_errors, {})

        self.assertTrue( isinstance(errors["length_1"][0], Exception))
        self.assertTrue( isinstance(errors["length_10"][0], Exception))
        self.assertTrue( isinstance(errors["length_20"][0], Exception))

    def test_uppercase(self):
        schema = {
            "upper_str_1": StringType().uppercase(),
            "upper_str_2": StringType().uppercase()
        }
        matched_data = {
            "upper_str_1": "HELLO WORLD!",
            "upper_str_2": "KEYBOARD CAT"
        }
        unmatched_data = {
            "upper_str_1": "Hello world!",
            "upper_str_2": "Keyboard cat"
        }
        empty_errors = Validator.validate(schema, matched_data)
        errors = Validator.validate(schema, unmatched_data)
        self.assertEqual(empty_errors, {})

        self.assertIsInstance(errors["upper_str_1"][0], Exception)
        self.assertIsInstance(errors["upper_str_2"][0], Exception)

    def test_lowercase(self):
        schema = {
            "lower_str_1": StringType().uppercase(),
            "lower_str_2": StringType().uppercase()
        }
        matched_data = {
            "lower_str_1": "HELLO WORLD!",
            "lower_str_2": "KEYBOARD CAT"
        }
        unmatched_data = {
            "lower_str_1": "Hello world!",
            "lower_str_2": "Keyboard cat"
        }
        empty_errors = Validator.validate(schema, matched_data)
        errors = Validator.validate(schema, unmatched_data)
        self.assertEqual(empty_errors, {})

        self.assertIsInstance(errors["lower_str_1"][0], Exception)
        self.assertIsInstance(errors["lower_str_2"][0], Exception)

    def test_alphanum(self):
        schema = {
            "some_username": StringType().alphanum(),
            "some_nickname": StringType().alphanum()
        }
        matched_data = {
            "some_username": "someUsername2022",
            "some_nickname": "nick2022name"
        }
        unmatched_data = {
            "some_username": "$username",
            "some_nickname": "nick%name"
        }
        empty_errors = Validator.validate(schema, matched_data)
        errors = Validator.validate(schema, unmatched_data)
        self.assertEqual(empty_errors, {})

        self.assertIsInstance(errors["some_username"][0], Exception)
        self.assertIsInstance(errors["some_nickname"][0], Exception)

    def test_hex(self):
        schema = {
            "hex_str_1": StringType().hex(),
            "hex_str_2": StringType().hex()
        }
        matched_data = {
            "hex_str_1": "0xabcdf12",
            "hex_str_2": "0x73556a0b"
        }
        unmatched_data = {
            "hex_str_1": "0Xabdg",
            "hex_str_2": "ab7f",
        }
        empty_errors = Validator.validate(schema, matched_data)
        errors = Validator.validate(schema, unmatched_data)
        self.assertEqual(empty_errors, {})

        self.assertIsInstance(errors["hex_str_1"][0], Exception)
        self.assertIsInstance(errors["hex_str_2"][0], Exception)

    def test_email(self):
        schema = {
            "email_1": StringType().email(),
            "email_2": StringType().email(),
            "email_3": StringType().email(),
            "email_4": StringType().email(),
        }
        matched_data = {
            "email_1": "someUser@someDomain.com",
            "email_2": "alice2021@school.edu",
            "email_3": "bob2000@company.com",
            "email_4": "carter2022@industry.co",
 
        }
        unmatched_data = {
            "email_1": "someUser@so#meDomain.com",
            "email_2": "alice^2021@school.edu",
            "email_3": "@company.com",
            "email_4": "carter2022@industry",
        }

        empty_errors = Validator.validate(schema, matched_data)
        errors = Validator.validate(schema, unmatched_data)
        self.assertEqual(empty_errors, {})

        self.assertIsInstance(errors["email_1"][0], Exception)
        self.assertIsInstance(errors["email_2"][0], Exception)
        self.assertIsInstance(errors["email_3"][0], Exception)
        self.assertIsInstance(errors["email_4"][0], Exception)

    def test_password(self):
        schema = {
            "pass1": StringType().password(),
            "pass2": StringType().password(),
            "pass3": StringType().password(),
        }
        matched_data = {
            "pass1": "1384973214971&^(*&^",
            "pass2": "0380*&)(&123r2234*(Y",
            "pass3": "^&(adfasdfe3r234"
        }
        unmatched_data = {
            "pass1": "    passsword    ",
            "pass2": "tab\t\tpassword",
            "pass3": "pass world \n"
        }

        empty_errors = Validator.validate(schema, matched_data)
        errors = Validator.validate(schema, unmatched_data)
        self.assertEqual(empty_errors, {})

        self.assertIsInstance(errors["pass1"][0], Exception)
        self.assertIsInstance(errors["pass2"][0], Exception)
        self.assertIsInstance(errors["pass3"][0], Exception)


    def test_pattern(self):
        pass


if __name__ == "__main__":
    unittest.main()