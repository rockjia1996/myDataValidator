from python_data_validator.types.DataType import DataType

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
            raise Exception(f"Error: not a number")


    # Validate the min value
    @DataType.append_queue
    def min(self, min_value, data):
        if data < min_value:
            raise Exception(f"Error: out of min bound")

    # Validate the max value 
    @DataType.append_queue
    def max(self, max_value, data):
        if data > max_value:
            raise Exception(f"Error: out of max bound")


    # Validate the matched value
    @DataType.append_queue
    def exact(self, exact_value, data):
        if data != exact_value:
            raise Exception(f"Error: unmatched value")


    # Validate the positive number
    @DataType.append_queue
    def positive(self, data):
        if data < 0:
            raise Exception(f"Error: not positive value")


    # Validate the negative number
    @DataType.append_queue
    def negative(self, data):
        if data > 0:
            raise Exception(f"Error: not negative value")


    # Validate the multiple of base
    @DataType.append_queue
    def multiple(self, base, data):
        if data % base != 0:
            raise Exception(f"Error: not multiple of base {base}")