

class ValidationError(Exception):
    def __init__(self, tag, message):
        super().__init__()
        self.error_tag = tag
        self.error_message = message

    def get_error_tag(self):
        return self.error_tag

    def get_error_message(self):
        return self.error_message

