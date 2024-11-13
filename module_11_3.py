class Info:
    def __init__(self, obj):
        self.obj = obj

    def introspection_info(self):
        return {
            'TYPE': type(self.obj).__name__,
            'ATTRIBUTES': dir(self.obj),
            'METHODS': [method for method in dir(self.obj) if callable(getattr(self.obj, method))],
            'MODULE': getattr(obj, '__module__')}


obj = Info(42)
print(obj.introspection_info())
