import re

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

class StringType(DataType):

    def __init__(self):
        super().__init__()
        self.string()

    # Validate string type 
    # The method will be called when initializing the instance
    @DataType.append_queue
    def string(self, data):
        if not isinstance(data, str):
            raise ValidationError("STRING_ERROR", "not string type")

    # Validate if the number of characters are out of lower bound
    @DataType.append_queue
    def min(self, min_value, data):
        if len(data) < min_value: 
            raise ValidationError("MIN_ERROR", "not min bound")

    # Validate if the number of characters are out of higher bound
    @DataType.append_queue
    def max(self, max_value, data):
        if len(data) > max_value:
            raise ValidationError("MAX_ERROR", "out max bound")

    # Validate if the number of characters are exact
    @DataType.append_queue
    def length(self, length, data):
        if len(data) != length:
            raise ValidationError("LENGTH_ERROR", "unmatched length")

    # Validate if all the characters are uppercase
    @DataType.append_queue
    def uppercase(self, data):
        if not data.isupper():
            raise ValidationError("UPPERCASE_ERROR", "not all uppercase")

    # Validate if all the characters are lowercase
    @DataType.append_queue
    def lowercase(self, data):
        if not data.islower():
            raise ValidationError("LOWERCASE_ERROR", "not all lowercase")

    # Validate if all the characters are alphanumeric
    @DataType.append_queue
    def alphanum(self, data):
        if not data.isalnum():
            raise ValidationError("ALPHANUM_ERROR", "not all alphanumeric")

    # Validate if the string is a hex string
    @DataType.append_queue
    def hex(self, data):
        hex_pattern = re.compile(r"^0x[0-9a-fA-F]+")
        if not bool(hex_pattern.match(data)):
            raise ValidationError("HEX_ERROR", "not hex string")


    # Validate if the email address is valid    
    @DataType.append_queue
    def email(self, data, domain_patterns=None):

        # Basic email pattern
        # 64 characters for username, 128 characters for domain name
        email_pattern = re.compile(r"^(\w{2,64})@(\w{2,64}\.\w{2,64})$")

        match_result = email_pattern.fullmatch(data)
        if not bool(match_result):
            raise ValidationError("EMAIL_ERROR", "not email address")

        #username = match_result.group(1)
        domain = match_result.group(2)

        if domain_patterns == None: return 

        if not isinstance(domain_patterns, list):
            raise ValidationError("EMAIL_ARGS_ERROR", "domain_patterns needs to be a list of regex")

        match_any = False
        for pattern in domain_patterns:
            if bool(re.compile(pattern).fullmatch(domain)):
                match_any = True
                break
        if not match_any:
            raise ValidationError("EMAIL_DOMAIN_ERRORS", "domain name missed matched")


    # Validate the password
    @DataType.append_queue
    def password(self, data):
        password_pattern = re.compile(r"\S+")
        if not bool(password_pattern.fullmatch(data)):
            raise ValidationError("PASSWORD_ERROR", "illegal password")


    # Validate based on the regex
    @DataType.append_queue
    def pattern(self, data, match_all=None, match_any=None, match_none=None):
        
        # Check if match all the patterns
        if isinstance(match_all, list):
            for pattern in match_all:
                if not bool(re.compile(pattern).match(data)):
                    raise ValidationError("PATTERN_ERROR", "unmatched the include pattern")

        if match_all == None or isinstance(match_all, list):
            raise ValidationError("PATTERN_ARGS_ERROR", "match_all argument should be a list of regex patterns")

        
        # Check if match if any the given patterns
        if isinstance(match_any, list):
            any_match = False
            for pattern in match_any:
                if bool(re.compile(pattern).match(data)):
                    any_match = True
                    break
            if not any_match:
                raise ValidationError("PATTERN_ERROR", "unmatched any pattern")

        if match_any == None or isinstance(match_any, list):
            raise ValidationError("PATTERN_ARGS_ERROR", "match_any argument should be a list of regex patterns")

        # Check if match any of excludsive pattern
        if isinstance(match_none, list):
            for pattern in match_none:
                if bool(re.compile(pattern).match(data)):
                    raise ValidationError("PATTERN_ERROR", "unmatched exclude pattern")

        if match_none == None or isinstance(match_none, list):
            raise ValidationError("PATTERN_ARGS_ERROR", "match_none argument should be a list of regex patterns")



