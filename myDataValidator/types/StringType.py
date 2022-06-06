import re

from myDataValidator.types.DataType import DataType

# All the methods that handle the validations, that is all the current or 
# future methods that will be annoted with decorator @append_queue, should 
# construct its paramters in the following signature:
#
#   def some_method (self, arg1, arg2, ..., data, kwarg1=, ,kwarg2=, ...)
# 
# By following the above signature, the partial function can properly 
# construct validation function with the given incomplete arguments.

class StringType(DataType):

    def __init__(self):
        super().__init__()
        self.string()

    # Validate string type 
    # The method will be called when initializing the instance
    @DataType.append_queue
    def string(self, data):
        if not isinstance(data, str):
            raise Exception(f"Error : not string type")

    # Validate if the number of characters are out of lower bound
    @DataType.append_queue
    def min(self, min_value, data):
        if len(data) < min_value: 
            raise Exception(f"Error : out of min bound") 

    # Validate if the number of characters are out of higher bound
    @DataType.append_queue
    def max(self, max_value, data):
        if len(data) > max_value:
            raise Exception(f"Error: out of max bound")

    # Validate if the number of characters are exact
    @DataType.append_queue
    def length(self, length, data):
        if len(data) != length:
            raise Exception(f"Error: unmatched length")

    # Validate if all the characters are uppercase
    @DataType.append_queue
    def uppercase(self, data):
        if not data.isupper():
            raise Exception(f"Error: not all uppercase")

    # Validate if all the characters are lowercase
    @DataType.append_queue
    def lowercase(self, data):
        if not data.islower():
            raise Exception(f"Error: not all lowercase")

    # Validate if all the characters are alphanumeric
    @DataType.append_queue
    def alphanum(self, data):
        if not data.isalnum():
            raise Exception(f"Error: not all alphanumeric")

    # Validate if the string is a hex string
    @DataType.append_queue
    def hex(self, data):
        hex_pattern = re.compile(r"^0x[0-9a-fA-F]+")
        if not bool(hex_pattern.match(data)):
            raise Exception(f"Error: not hex string")


    # Validate if the email address is valid    
    @DataType.append_queue
    def email(self, data):

        # Basic email pattern
        # 64 characters for username, 128 characters for domain name
        email_pattern = re.compile(r"^(\w{2,64})@(\w{2,64}\.\w{2,64})$")

        match_result = email_pattern.fullmatch(data)
        if not bool(match_result):
            raise Exception(f"Error: not email address")

        #username = match_result.group(1)
        #domain = match_result.group(2)

    # Validate the password
    @DataType.append_queue
    def password(self, data):
        password_pattern = re.compile(r"\S+")
        if not bool(password_pattern.fullmatch(data)):
            raise Exception(f"Error: illegal password")


    # Validate based on the regex
    @DataType.append_queue
    def pattern(self, data, match_all=None, match_any=None, match_none=None):
        
        # Check if match all the patterns
        if isinstance(match_all, list):
            for pattern in match_all:
                if not bool(re.compile(pattern).match(data)):
                    raise Exception(f"Error: unmatched the include pattern")
        else:
            raise Exception(f"Error: match_all argument should be a list of regex patterns")

        
        # Check if match if any the given patterns
        if isinstance(match_any, list):
            any_match = False
            for pattern in match_any:
                if bool(re.compile(pattern).match(data)):
                    any_match = True
                    break
            if not any_match:
                raise Exception(f"Error: unmatched any pattern")
        else:
            raise Exception(f"Error: match_all argument should be a list of regex patterns")

        # Check if match any of excludsive pattern
        if isinstance(match_none, list):
            for pattern in match_none:
                if bool(re.compile(pattern).match(data)):
                    raise Exception(f"Error: match the exclude pattern")
        else: 
            raise Exception(f"Error: match_all argument should be a list of regex patterns")










