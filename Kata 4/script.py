text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

#Primero, divide el texto en cada oración para trabajar con su contenido:
text_parts = text.split('. ')
#text_parts

#Ahora, define algunas palabras clave para búsqueda que te ayudarán a determinar si una oración contiene un hecho.
## Define las palabras pista: average, temperature y distance suenan bien
key_words = ["average", "temperature", "distance"]

for sentence in text_parts:
    for key_word in key_words:
        if key_word in sentence:
            #print(sentence)
            break

# Ciclo para cambiar C a Celsius
for sentence in text_parts:
    for key_word in key_words:
        if key_word in sentence:
            #print(sentence.replace(' C', ' Celsius'))
            break

#Ejercicio 2

planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'
title = f'datos de gravedad sobre {nombre}'


# Creamos la plantilla
hechos = f"""{'-'*80} 
Nombre del planeta: {planeta} 
Gravedad en {nombre}: {gravedad * 1000} m/s2 
"""

#print(hechos)

template = f"""{title.title()} 
{hechos} 
""" 


# Nuevos datos muestra
planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'

#print(hechos)

new_template = """
Datos de Gravedad sobre: {nombre}
-------------------------------------------------------------------------------
Nombre del planeta: {planeta}
Gravedad en {nombre}: {gravedad} m/s2
"""
#print(new_template.format(nombre=nombre, planeta=planeta, gravedad=gravedad))

# Pista: print(nueva_plantilla.format(variables))
print(new_template.format(nombre=nombre, planeta=planeta, gravedad=gravedad*1000))