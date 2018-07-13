

operacion1 = (4 < 10 or False) and (True and True)#true
operacion2 = not (((5 ** 5 == 2 * 2) or not False) and (True and True))#false
operacion3 = operacion1 == operacion2#true
operacion3 == False
False """#>>Aquí va el resultado de la comparación (True o False)"""



a = [2, 3, 4, 5]
b = [4, 5]
numbers = [value for value in a if value >= 4]
#numbre tiene una lista con los valores 4,5
result = numbers == b or False
#result =true
result == (not False)
#>>Aquí va el resultado de la comparación (True o False)
True

number = 10
valor = ""

if ((number * 10) / 100 + 0.2) == (24 + 24 - number - 37):
  valor = "Ok"
else:
  valor = "Wrong"

valor == "Ok"
#>> Aquí va el resultado de la comparación
False

a = 10
b = 5
valor = ""

if a + 10 <= b:
  valor = "Comparación <= | a es Menor o Igual que b!"
elif a + 10 >= b + 16:
  valor = "Comparación >= | a es Mayor o Igual que b!"
elif a + 1 == b + 6:
  valor = "Comparación == | a es IGUAL que b!"
else:
  valor = "NINGUNO!"

valor == "Comparación == | a es IGUAL que b!"
#>> Aquí va el resultado de la comparación
True
