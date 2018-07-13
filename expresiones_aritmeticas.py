
#En la expresión1 no está permitido agregar otra operación aritmética,
#ni modificar el tipo de operación (p.e. una división por una resta, etc.)

expresion1 = (2 // (10 // (2 ** 2))) + (2 * 3)
expresion2 = (expresion1 + 1) * 10 / 80 == float("1.0")
#>>True
print(expresion2)


expresion3 = True#Aquí va una expresión aritmética
expresion4 = expresion3 is expresion2
print(expresion4)

resultado = expresion4 == True
#>>True
print(resultado)

#En la expresión1 no está permitido agregar otra operación aritmética,
#ni modificar el tipo de operación (p.e. una resta por una suma, etc.)

expresion1 = ((2 + 3 - 1) * (2 ** 3) / 4) + (5 / 2)
expresion2 = expresion1-0.3 == 10.2
#print(expresion2)
#>>True
expresion3 = int(expresion1 * 5)
expresion4 = int("52")
expresion5 = expresion3 == expresion4
#=>True
print(expresion5)

expresion6 = (expresion4 // expresion4)-1 % 3
expresion7 = expresion6 is 0
expresion8 = expresion7 == True
print(expresion8)






#>>True
