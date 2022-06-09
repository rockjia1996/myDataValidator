from myDataValidator.types.DataType import DataType
from myDataValidator.exceptions.ValidationError import ValidationError

# All the methods that handle the validations, that is all the current or 
# future methods that will be annoted with decorator @append_queue, should 
# construct its paramters in the following signature:
#
#   def some_method (self, arg1, arg2, ..., data, kwarg1=, ,kwarg2=, ...)
# 
# By following the above signature, the partial function can properly 
# construct validation function with the given incomplete arguments.

class NumberType(DataType):

    def __init__(self):
        super().__init__()
        self.number()

    # Validate number type
    # The method will be called when initializing the instance
    @DataType.append_queue
    def number(self, data):
        if not (isinstance(data, int) or isinstance(data, float)):
            raise ValidationError("NUMBER_ERROR", "not number type")


    # Validate the min value
    @DataType.append_queue
    def min(self, min_value, data):
        if data < min_value:
            raise ValidationError("MIN_ERROR", "min out of bound")

    # Validate the max value 
    @DataType.append_queue
    def max(self, max_value, data):
        if data > max_value:
            raise ValidationError("MAX_ERROR", "max out of bound")


    # Validate the matched value
    @DataType.append_queue
    def exact(self, exact_value, data):
        if data != exact_value:
            raise ValidationError("EXACT_ERROR", "exact unmatched")

    # Validate the positive number
    @DataType.append_queue
    def positive(self, data):
        if data < 0:
            raise ValidationError("POSITIVE_ERROR", "not positive")

    # Validate the negative number
    @DataType.append_queue
    def negative(self, data):
        if data > 0:
            raise ValidationError("NEGATIVE_ERROR", "not negative")

    # Validate the multiple of base
    @DataType.append_queue
    def multiple(self, base, data):
        if data % base != 0:
            raise ValidationError("MULTIPLE_ERROR", "not the multiple of the base")