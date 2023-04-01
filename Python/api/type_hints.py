# Estamos trabajando con FastAPI
# Type Hints , mostrando ejemplos de tipado dinamico

my_string_variable = "My string Variable"
print(my_string_variable)
print(type(my_string_variable))

# Le asignamos valor numerico
my_string_variable = 5
print(my_string_variable)
print(type(my_string_variable))

# asignamos a proposito un tipo int con un valor string, para mostrar que el editor no lo toma como invalido
my_typed_variable: int = "My tiped variable"
my_typed_variable.bit_count() # Va a tirar error en tiempo de ejecucion, podemos usar los metodos de int aunque el valor sea un string en el editor. OJO!
print(my_typed_variable) 
print(type(my_typed_variable))

my_typed_variable = 5
print(my_typed_variable)
print(type(my_typed_variable))



