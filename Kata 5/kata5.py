answer = 30 + 12
print(answer)

difference = 30 - 12
print(difference)

product = 30 * 12
print(product)

quotient = 30 / 12
print(quotient)

seconds = 1042
minutes = seconds // 60
print(minutes)

seconds = 1042
display_minutes = 1042 // 60
display_seconds = 1042 % 60

print(display_minutes)
print(display_seconds)

#Igual resultado    
result_1 = 1032 + 26 * 2
result_2 = 1032 + (26 * 2)

#Cast de string a int
demo_int = int('215')
print(demo_int)

#Valores absolutos
print(abs(39 - 16))
print(abs(16 - 39))

#Redondeo al valor mas cercano
#Si es .5 redondea hacia arriba
print(round(14.5))

#Bibleoteca math
from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)