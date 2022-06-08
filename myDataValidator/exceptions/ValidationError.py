

class ValidationError(Exception):
    def __init__(self):
        super().__init__()
        self.error_tag = "VALIATION_ERROR"
        self.error_message = "validation error"

    def get_error_tag(self):
        return self.error_tag

    def get_error_message(self):
        return self.error_message