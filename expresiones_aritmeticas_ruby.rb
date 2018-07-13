#En la expresión1 no está permitido agregar otra operación aritmética,
#ni modificar el tipo de operación (p.e. una división por una resta, etc.)

expresion1 = (5.to_f / (4 ** 2)) + (1 * 2)#
expresion2 = (expresion1 * 10) / 23.125#0
expresion3 = 1 ** 1000
expresion4 = expresion3 == expresion2
expresion4 == true
#=> true
true


#En la expresión1 no está permitido agregar otra operación aritmética,
#ni modificar el tipo de operación (p.e. una resta por una suma, etc.)

expresion1 = ((4 * 2) + (3.to_f / 7) ** 3).round(2)
expresion2 = expresion1 == 8.08
#=> true
expresion3 = (expresion1 ** 3).to_i
expresion4 = 527
expresion5 = expresion3 == expresion4
#=> true
true
expresion6 = (expresion4 / expresion4 % 2) - 1
expresion7 = expresion6 == 0
#=> true
