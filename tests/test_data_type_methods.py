import unittest
from myDataValidator.types.DataType import DataType
from myDataValidator.types.StringType import StringType

class TestDataTypeMethods(unittest.TestCase):
    def test_get_default_arguments(self):

        myDataType = DataType()

        def test_func1(x, y, z):
            print("doing nothing")

        def test_func2(x, y=2, z=3):
            print("doing nothing")

        def test_func3(x, y, z=3):
            print("doing nothing")

        def test_func4(x=1, y=2, z=3):
            print("doing nothing")


        test_func1_args = myDataType.get_default_arguments(test_func1)
        test_func2_args = myDataType.get_default_arguments(test_func2)
        test_func3_args = myDataType.get_default_arguments(test_func3)
        test_func4_args = myDataType.get_default_arguments(test_func4)
        
        self.assertEqual(test_func1_args, {})
        self.assertEqual(test_func2_args, {"y":2, "z": 3})
        self.assertEqual(test_func3_args, {"z":3})
        self.assertEqual(test_func4_args, {"x":1, "y":2, "z":3})


    def test_get_default_arguments_with_subclasses(self):

        class SomeType(DataType):
            def __init__(self):
                super().__init__()

            @DataType.append_queue
            def sum(self, data, x=1, y=2, z=3):
                return x + y + z + data

            @DataType.append_queue
            def multiple(self, data, x=10):
                return x * data

        someType = SomeType()
        someType.sum()
        someType.multiple()

        queue = someType.validation_queue

        self.assertEqual(len(queue), 2)
        self.assertTrue(callable(queue[0]))
        self.assertTrue(callable(queue[1]))
        self.assertEqual(queue[0](10), 16 )
        self.assertEqual(queue[1](10), 100)


    def test_validate(self):
        myDataType = DataType()

        def sum3(y):
            return 3 + y

        def power2(exp):
            return 2 ** exp

        myDataType.validation_queue.append(lambda x: x + 10)
        myDataType.validation_queue.append(lambda x: x - 10)
        myDataType.validation_queue.append(sum3)
        myDataType.validation_queue.append(power2)


        empty_errors = myDataType.validate(10)
        self.assertEqual(empty_errors, [])

        myDataType.errors = []
        errors = myDataType.validate("x")
        self.assertIsInstance(errors[0], TypeError)
        self.assertIsInstance(errors[1], TypeError)
        self.assertIsInstance(errors[2], TypeError)
        self.assertIsInstance(errors[3], TypeError)



