RUN_INDENTED = True

message = "running unindented"

if RUN_INDENTED:
    message = "running indented" # indent with  spaces

print(message)


def my_function():
    greet = "Hello"
    return greet


print(my_function())
