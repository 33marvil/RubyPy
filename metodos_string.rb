#[]
frutas = ["fresa", "durazno"]
p frutas[0]
#=>"fresa"
frutas[0]="piña"
p frutas


"carlos".capitalize #=> "C"
#chr
"ajedrez".chr  #=> "a"
#count
"cientoventicinco".count("i")
#empty?
"".empty?
#sub
p "helle".sub(/e/, '*')
#=>"h*llo"

#gsub
p "hellerto".gsub(/[e,o,l]/, '*')
#=>"h****"
#include?
p "mariofrias".include?("rio")
#index
p "automovil".index("v")
#reverse
p "boligrafo".reverse
#split
p "libreta cuaderno maleta".split

word1 = "Hello World!"
metodo1 = word1[0,4]
p metodo2 = metodo1.downcase == "hell"
#=> true

p metodo3 = word1.include?(metodo1) == true
#=> true

p metodo4 = metodo3.to_s.capitalize == "True"
#=> true
p metodo5 = metodo4.to_s.size == 4
#=> true
p metodo6 = metodo5.to_s.split(//) == ["t", "r", "u", "e"]
#=> true
metodo7 = metodo6.to_s

metodo8 = metodo7[1] = "h"
p metodo9 = metodo7 == "thue"
#=> true

p metodo10 = metodo7.include?("t") == true
#=> true
p metodo11 = metodo7.reverse.upcase == "EUHT"
#=> true














#strip
