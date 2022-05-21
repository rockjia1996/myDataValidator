import re

class NumberTypeValidation():
    def __init__(self):
        self.validate_stack = []

    # Get the pre-config rules
    def get_validations(self):
        return self.validate_stack

    # Add rule to the sequnce    
    def add_validation(self, func):
        self.validate_stack.append(func)

    # Validate number type
    # The method will be called when initializing the instance
    def number(self):
        def check_number(data):
            if not isinstance(data, int) or not isinstance(data, float):
                raise Exception(f"Error: not a number")
        self.add_validation(check_number)


    # Validate the min value
    def min(self, min_value):
        def check_min(data):
            if data < min_value:
                raise Exception(f"Error: out of min bound")
        self.add_validation(check_min)
        return self

    # Validate the max value 
    def max(self, max_value):
        def check_max(data):
            if data > max_value:
                raise Exception(f"Error: out of max bound")
        self.add_validation(max_value)
        return self


    # Validate the matched value
    def exact(self, exact_value):
        def check_exact(data):
            if data != exact_value:
                raise Exception(f"Error: unmatched value")
        self.add_validation(exact_value)
        return self


    # Validate the positive number
    def positive(self):
        def check_positive(data):
            if data < 0:
                raise Exception(f"Error: not positive value")
        self.add_validation(check_positive)
        return self


    # Validate the negative number
    def negative(self):
        def check_negative(data):
            if data > 0:
                raise Exception(f"Error: not negative value")
        self.add_validation(check_negative)
        return self


    # Validate the multiple of base
    def multiple(self, base):
        def check_multiple(data):
            if data % base != 0:
                raise Exception(f"Error: not multiple of base {base}")
        self.add_validation(check_multiple)
        return self


















