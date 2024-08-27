def test_function():
    def inner_function():
        print("Я в области видимости  функции test_function")

    inner_function()


test_function()

# inner_function не определена вне области видимости test_function
