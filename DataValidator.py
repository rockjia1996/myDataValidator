from StringTypeValidation import StringTypeValidation
from NumberTypeValidation import NumberTypeValidation

class DataValidator():

    @staticmethod
    def validate(schema, data):
        errors = {}
        for key, validations in schema.items():
            error = validations.validate(data[key])
            if len(error) != 0:
                errors[key] = error
        return errors



if __name__ == "__main__":
    string_test_schema = {
        "test1": StringTypeValidation().min(7).max(50).email(),
        "test2": StringTypeValidation().min(4).max(32).password(),
        "test3": StringTypeValidation().alphanum().min(4).max(32).lowercase()
    }

    string_test_data = {
        "test1": "yujia@domain.com",
        "test2": "$somePassword123@%&\\n",
        "test3": "someteststring"
    }

    errors = DataValidator.validate(string_test_schema, string_test_data)
    for key, val in errors.items():
        print(f"key: {key}, val: {val}")


    number_test_schema = {
        "test1": NumberTypeValidation().min(10).max(100),
        "test2": NumberTypeValidation().positive().min(100),
        "test3": NumberTypeValidation().min(10).max(10000).multiple(2)
    }

    number_test_data = {
        "test1": 23,
        "test2": 150,
        "test3": 222
    }


    errors = DataValidator.validate(number_test_schema, number_test_data)
    for key, val in errors.items():
        print(f"key: {key}, val: {val}")

