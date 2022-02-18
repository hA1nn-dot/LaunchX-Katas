#   Diccionarios
planet = {
    'name': 'Earth',
    'moons': 1
}

# Muestra Earth
print(planet.get('name'))

#   Si no encuentra el valor, retorna None
#wibble = planet.get('wibble') # Regresa None
#wibble = planet['wibble'] # Arroja un KeyError

#   Modificando valores name ahora es Makemake
planet.update({'name': 'Makemake'})

#   Modificando valores:  name is now set to Makemake
planet['name'] = 'Makemake'

# Usando update: modifica multiples valores con update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

#   Añadir una clave
planet['orbital period'] = 4333
#   Quitar una clave
planet.pop('orbital period')

#   Datos complejos
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

#print(planet)
#print(f'''{planet['name']} polar diameter: {planet['diameter (km)']['polar']}''')

#   Recuperación de claves
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

# Salida:
# october: 3.5cm
# november: 4.2cm
# december: 2.1cm