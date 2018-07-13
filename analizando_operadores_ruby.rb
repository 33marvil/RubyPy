number = 10
valor = ""
if ((number * 10) / 100) == (24 + 24 - number - 37)
     #10*10= 100 / 100   == 48 - 10 =38 - 37
  valor = "Good"
else
  valor = "Bad"
end

valor == "Good"
#=> Resultado de la comparación (true o false)
true

comparacion1 = (10 < 70 || true) && (true || true)
#true
comparacion2 = !(((4 ** 4 == 3 * 3) || !true) && (true && true))
comparacion3 = comparacion1 == comparacion2
comparacion3 == false
#=> Resultado de la comparación (true o false)
false

operacion = '70'.to_i == 70? "true" : "false"
#operador ternario : = else
operacion == true
#=> Resultado de la comparación (true o false)
false

a = 10
b = 5
valor = ""

if a + 10 <= b
  valor = "Comparación <= | a es Menor o Igual que b!"
elsif a + 10 >= b + 16
  valor = "Comparación >= | a es Mayor o Igual que b!"
elsif a + 1 == b
  valor = "Comparación == | a es IGUAL que b!"
else
  valor = "NINGUNO!"
end

valor == "Comparación == | a es IGUAL que b!"
#=> Resultado de la comparación (true o false)
false
