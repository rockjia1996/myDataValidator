from functools import partial
import inspect

class DataType():

    def __init__(self):
        self.errors = []
        self.validation_queue = []

    def validate(self, data):
        for func in self.validation_queue:
            try:
                func(data)
            except Exception as error:
                self.errors.append(error)
        return self.errors


    # Credit: https://stackoverflow.com/questions/31728346/passing-default-arguments-to-a-decorator-in-python
    def get_default_arguments(self, func):
        signature = inspect.signature(func)
        return {
            k: v.default 
            for k, v in signature.parameters.items()
            if v.default is not inspect.Parameter.empty
        }

    # wrapper function for contructing validations and appending to the queue
    def append_queue(func):
        def callable(self, *args, **kwargs):
            # Get the default keyword arguments
            kw_args = self.get_default_arguments(func)
            # Update the default keyworad arguments with the provided 
            # keyword arguments
            kw_args.update(kwargs)

            # Construct the partial function that ONLY missing the data argument
            validation_func = partial(func, self, *args, **kw_args)
            self.validation_queue.append(validation_func)
            return self
        return callable