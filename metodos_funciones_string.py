"""
Métodos y funciones de string en Python
Python tiene métodos que pueden ser aplicados para desarrollar una tarea sobre un string,
asimismo tiene también funciones que pueden tomar como parámetro un string y desarrollar cierta tarea.
Algunos métodos y funciones de string
"""
#count
frutas = ['naranja', 'manzana', 'pera', 'banana', 'kiwi', 'manzana', 'banana']
frutas.count('manzana')
#index
frutas.index('banana')
#isdecimal
medida = "2345678"
print(medida.isdecimal())
#=>true
#center
auto = "el carro rojo"
new_auto = auto.center(20)
print("Este es el mio:", new_auto)
#capitalize
letrero = "leyenda de venta"
print(letrero.capitalize())
#find
quote = 'Let it be, let it be, let it be'

result = quote.find('let it')
print("Substring 'let it':", result)
#len
libret = "esta libreta esta llena"
print("tirar", len(libret))
#lower
alto = "TODAS ES MINUSCULAS"
print(alto.lower())
#upper
bajas = "todas son altas"
print(bajas.upper())
#strip
separado = "  esto esta separado  "
print(separado.strip())
#split
malteada = "leche fruta cereal"
print(malteada.split())
#startswith
responsable = "Carlos es el reponsable de "
print(responsable.startswith("Carlos"))
#max
lista1 = ["perros", "gatos", "elefantes"]#devuelve el maximo valor a = <  z=>
lista2 = [123, 546, 0.34568976]
print(max(lista1))

print(max(["abc", "dfg", "w"]))

print(max(2, 3))
max('a', 'b', 'c')

"""
print(max(lista2))

list1, list2 = ['C++','Java', 'Python'], [456, 700, 200]
print ("Max value element : ", max(list1))
print ("Max value element : ", max(list2))
"""
hola = "bienvenido"
hola2 = "al curso"
string_result = (hola + hola2.center(15))#¿Qué se asignaría a esta variable para que la siguiente expresión sea True
print(string_result.upper() == 'BIENVENIDO    AL CURSO   ')
#True

string_result.capitalize().strip() == 'Bienvenido    al curso'
#True

print(len(string_result) == 25)
#True

print(string_result.count("e") == 2)
#True

print(string_result.replace('al curso', "este sabado").lower().split() == ['bienvenido', 'este', 'sabado'])
#true

variable = ["coca", "cola", "soda"]#¿Qué se asignaría a esta variable para que la última expresión sea True
print(len(variable) == 3)
#True















#min
