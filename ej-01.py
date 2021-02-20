
# Función para determinar el largo de un número

def count_characters(number):
  assert number >= 0
  if number == int(number):
    pass
  else:
    return None, 'el valor no es un número entero mayor a 0'
  def count_char(number):
    number2 = str(number)
    result = 1
    for char in number2:
      result += 1
    return result
  print(result)
  count_char(number)

count_characters(4321)

#  print(f'El número: {number}','\n', 'Tiene un largo de: ', len(number))




# NOTA:

#  if total < 10:
#    return None, 'el total es muy chico'
#  elif total <= 20:
    return None, 'el total es mediano'
#  else:
    return total, 'el total es correcto'
