def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()

inner_function() #Вызов функции inner function в глобальном пространстве имëн невозможен,
                 # так как она существует только в локальном пространстве функции test function.
