#todo
# Создайте декоратор, которые переводит все текстовые аргументы функции в верхний регистр и возвращает их в виде списка текстовых аргументов.

def convert_all_args_to_upper(func):
    def _wrapper(*args, **kwargs):
        retargs = [arg.upper() for arg in args if type(arg) is str]
        func(args, kwargs)
        return retargs
    return _wrapper

@convert_all_args_to_upper
def test(*args, **kwargs):
    pass

print(test("asdsad", "dsfdswetrw", "ureut456", 123, "sdf"))