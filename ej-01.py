
# Función para determinar el largo de un número

def count_characters(number):
  assert number >= 0
  if number == int(number):
    number2 = str(number)
    result = 1
    for char in number2:
      result += 1
      return result
  else:
    return None, 'el valor no es un número mayor entero mayor a 0'

count_characters(4321)

#  print(f'El número: {number}','\n', 'Tiene un largo de: ', len(number))

length_number(45)




# NOTA:

#  if total < 10:
#    return None, 'el total es muy chico'
#  elif total <= 20:
    return None, 'el total es mediano'
#  else:
    return total, 'el total es correcto'
