import re

class StringTypeValidation():

    def __init__(self):
        self.validation_stack = []
        self.string()

    # Get the pre-config rules 
    def get_validations(self):
        return self.validation_stack

    # Add rule to the seqence 
    def add_validation(self, func):
        self.validation_stack.append(func)


    # Validate string type 
    # The method will be called when initializing the instance
    def string(self):
        def check_string(data):
            if not isinstance(data, str):
                raise Exception(f"Error : not string type")
        self.add_validation(check_string)

    # Validate if the number of characters are out of lower bound
    def min(self, min_value):
        def check_min(data):
            if len(data) < min_value: 
                raise Exception(f"Error : out of min bound") 
        self.add_validation(check_min)
        return self

    # Validate if the number of characters are out of higher bound
    def max(self, max_value):
        def check_max(data):
            if len(data) > max_value:
                raise Exception(f"Error: out of max bound")
        self.add_validation(check_max)
        return self

    # Validate if the number of characters are exact
    def length(self, length):
        def check_length(data):
            if len(data) != length:
                raise Exception(f"Error: unmatched length")
        self.add_validation(check_length)
        return self


    # Validate if all the characters are uppercase
    def uppercase(self):
        def check_uppercase(data):
            if not data.isupper():
                raise Exception(f"Error: not all uppercase")
        self.add_validation(check_uppercase)
        return self


    # Validate if all the characters are lowercase
    def lowercase(self):
        def check_lowercase(data):
            if not data.islower():
                raise Exception(f"Error: not all lowercase")
        self.add_validation(check_lowercase)
        return self


    # Validate if all the characters are alphanumeric
    def alphanum(self):
        def check_alphanum(data):
            if not data.isalnum():
                raise Exception(f"Error: not all alphanumeric")
        self.add_validation(check_alphanum)
        return self


    # Validate if the string is a hex string
    def hex(self):
        def check_hex(data):
            hex_pattern = re.compile(r"^0x[0-9a-fA-F]+")
            if not bool(hex_pattern.match(data)):
                raise Exception(f"Error: not hex string")
        self.add_validation(check_hex)
        return self


    # Validate if the email address is valid    
    # username_constraints and domain_constraints takes a list of regex to 
    # check against.
    def email(self, username_constraints=[], domain_constraints=[]):
        def check_email(data):
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


        self.add_validation(check_email)
        return self

    # Validate the password
    def password(self):
        def check_password(data):
            password_pattern = re.compile(r"\S+")
            if not bool(password_pattern.fullmatch(data)):
                raise Exception(f"Error: illegal password")

        self.add_validation(check_password)
        return self

    # Validate based on the regex
    def pattern(self, patterns=[]):
        def check_pattern(data):
            for pattern in patterns:
                if not bool(re.compile(pattern).match(data)):
                    raise Exception(f"Error: unmatched pattern")

        self.add_validation(check_pattern)
        return self



if __name__ == "__main__":
    list(
        [
            print(m + "()") for m in dir(StringTypeValidation()) 
            if re.match(r"^[a-zA-Z]+", m)
        ])