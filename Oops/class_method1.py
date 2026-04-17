class MyClass:
    class_variable="Hello"

    @classmethod
    def my_class_method(cls):
        return f"Class variable is :{cls.class_variable}"



print(MyClass.my_class_method())