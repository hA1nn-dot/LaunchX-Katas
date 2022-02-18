#   Listas

#Lista de Strings
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print('The first planet is', planets[0])
print('The second planet is', planets[1])
print('The third planet is', planets[2])

#Longuitud de la lista
number_of_planets = len(planets)
print('There are', number_of_planets, 'planets in the solar system.')

#Agregar al final de la lista un elemento
planets.append('Pluto')
number_of_planets = len(planets)
print('There are actually', number_of_planets, 'planets in the solar system.')

#Eliminar el ultimo elemento de la lista
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print('No, there are definitely', number_of_planets, 'planets in the solar system.')

# -1 = Ultimo elemento de la lista | -2 = Penultimo elemento de la lista
print('The last planet is', planets[-1])
print('The penultimate planet is', planets[-2])

# Busca el valor del elemento y retorna el índice, si no lo encuentra : -1
jupiter_index = planets.index('Jupiter')
print('Jupiter is the', jupiter_index + 1, 'planet from the sun')

gravity_on_earth = 1.0
gravity_on_the_moon = 0.166
gravity_on_planets = [0.378, 0.907, 1, 0.379, 2.36, 0.916, 0.889, 1.12]

bus_weight = 12650 # in kilograms, on Earth

print('On Earth, a double-decker bus weighs', bus_weight, 'kg')
print('On Mercury, a double-decker bus weighs', bus_weight * gravity_on_planets[0], 'kg')

#   min() = devuelve el valor mas pequeño | max() = devuelve el valor mas grande
bus_weight = 12650 # in kilograms, on Earth

print('On Earth, a double-decker bus weighs', bus_weight, 'kg')
print('The lightest a bus would be in the solar system is', bus_weight * min(gravity_on_planets), 'kg')
print('The heaviest a bus would be in the solar system is', bus_weight * max(gravity_on_planets), 'kg')

#   Slide = separar una lista sin modificar la original
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets_before_earth = planets[0:2]
print(planets_before_earth)
print(planets)

#   Uniendo listas con +
amalthea_group = ['Metis', 'Adrastea', 'Amalthea', 'Thebe']
galilean_moons = ['Io', 'Europa', 'Ganymede', 'Callisto']

regular_satellite_moons = amalthea_group + galilean_moons
print('The regular satellite moons of Jupiter are', regular_satellite_moons)

#   Ordenar listas por orden alfabetico o por numeros
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

#   Order de forma inversa
regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
