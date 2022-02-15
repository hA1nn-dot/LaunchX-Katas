text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

#Primero, divide el texto en cada oración para trabajar con su contenido:
text_parts = text.split('. ')
text_parts

#Ahora, define algunas palabras clave para búsqueda que te ayudarán a determinar si una oración contiene un hecho.
## Define las palabras pista: average, temperature y distance suenan bien
key_words = ["average", "temperature", "distance"]

for sentence in text_parts:
    for key_word in key_words:
        if key_word in sentence:
            print(sentence)
            break

# Ciclo para cambiar C a Celsius
for sentence in text_parts:
    for key_word in key_words:
        if key_word in sentence:
            print(sentence.replace(' C', ' Celsius'))
            break