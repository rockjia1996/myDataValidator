from StringTypeValidation import StringTypeValidation

class DataValidator():

    @staticmethod
    def validate(schema, data):
        errors = {}

        for key, validations in schema.items():
            error = DataValidator.validate_data(
                data[key], 
                validations.get_validations()
            )
            if isinstance(error, Exception):
                errors[key] = error

        return errors

    @staticmethod
    def validate_data(data, validations):
        try:
            for validation in validations:
                validation(data)
            return None
        except Exception as error:
            return error



if __name__ == "__main__":
    testSchema = {
        "test1": StringTypeValidation().min(4).max(50).email(),
        "test2": StringTypeValidation().min(4).max(32).password(),
        "test3": StringTypeValidation().alphanum().min(4).max(32).lowercase()
    }


    testData = {
        "test1": "yujia@domain.com",
        "test2": "$somePassword123@%&\\n",
        "test3": "some test string 3"
    }

    errors = DataValidator.validate(testSchema, testData)
    print(errors)