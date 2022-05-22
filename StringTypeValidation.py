import re
from functools import partial

# All the methods that handle the validations, that is all the current or 
# future methods that will be annoted with decorator @append_queue, should 
# construct its paramters in the following signature:
#
#   def some_method (self, arg1, arg2, ..., data, kwarg1=, ,kwarg2=, ...)
# 
# By following the above signature, the partial function can properly 
# construct validation function with the given incomplete arguments.

class StringTypeValidation():

    def __init__(self):
        self.errors = []
        self.validation_queue = []
        self.string()

    def validate(self, data):
        for func in self.validation_queue:
            try:
                func(data)
            except Exception as error:
                self.errors.append(error)
        return self.errors

    # wrapper function for contructing validations and appending to the queue
    def append_queue(func):
        def callable(self, *args, **kwargs):
            validation_func = partial(func, self, *args, **kwargs)
            self.validation_queue.append(validation_func)
            return self
        return callable


    # Validate string type 
    # The method will be called when initializing the instance
    @append_queue
    def string(self, data):
        if not isinstance(data, str):
            raise Exception(f"Error : not string type")

    # Validate if the number of characters are out of lower bound
    @append_queue
    def min(self, min_value, data):
        if len(data) < min_value: 
            raise Exception(f"Error : out of min bound") 

    # Validate if the number of characters are out of higher bound
    @append_queue
    def max(self, max_value, data):
        if len(data) > max_value:
            raise Exception(f"Error: out of max bound")

    # Validate if the number of characters are exact
    @append_queue
    def length(self, length, data):
        if len(data) != length:
            raise Exception(f"Error: unmatched length")

    # Validate if all the characters are uppercase
    @append_queue
    def uppercase(self, data):
        if not data.isupper():
            raise Exception(f"Error: not all uppercase")

    # Validate if all the characters are lowercase
    @append_queue
    def lowercase(self, data):
        if not data.islower():
            raise Exception(f"Error: not all lowercase")

    # Validate if all the characters are alphanumeric
    @append_queue
    def alphanum(self, data):
        if not data.isalnum():
            raise Exception(f"Error: not all alphanumeric")

    # Validate if the string is a hex string
    @append_queue
    def hex(self, data):
        hex_pattern = re.compile(r"^0x[0-9a-fA-F]+")
        if not bool(hex_pattern.match(data)):
            raise Exception(f"Error: not hex string")


    # Validate if the email address is valid    
    # username_constraints and domain_constraints takes a list of regex to 
    # check against.
    @append_queue
    def email(self, data, username_constraints=[], domain_constraints=[]):
        # Basic email pattern
        # 64 characters for username, 128 characters for domain name
        email_pattern = re.compile(r"^(\w{2,64})@(\w{2,64}\.\w{2,64})$")

        match_result = email_pattern.fullmatch(data)
        if not bool(match_result):
            raise Exception(f"Error: not email address")

        username = match_result.group(1)
        domain = match_result.group(2)

        # Validate username against given username constraints
        for constraint in username_constraints:
            if not bool(re.compile(constraint).match(username)):
                raise Exception(f"Error: illegal username in email")
                
        # Validate domain against given domain constraints
        for constraint in domain_constraints:
            if not bool(re.compile(constraint).match(domain)):
                raise Exception(f"Error: illegal domain in email")


    # Validate the password
    @append_queue
    def password(self, data):
        password_pattern = re.compile(r"\S+")
        if not bool(password_pattern.fullmatch(data)):
            raise Exception(f"Error: illegal password")


    # Validate based on the regex
    @append_queue
    def pattern(self, data, patterns=[]):
        for pattern in patterns:
            if not bool(re.compile(pattern).match(data)):
                raise Exception(f"Error: unmatched pattern")

