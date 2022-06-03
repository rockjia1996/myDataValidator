class Validator():

    @staticmethod
    def validate(schema, data):
        errors = {}
        for key, validations in schema.items():
            error = validations.validate(data[key])
            if len(error) != 0:
                errors[key] = error
        return errors
