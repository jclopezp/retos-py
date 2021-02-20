
# Función para determinar el largo de un número

def length_number(number):
  number1 = number
  if number1 == int(number):
    pass
  else:
    return None, 'el valor no es un número entero mayor a 0'
  def count_char(number1):
    number2 = str(number1)
    result = 1
    for char in number2:
      result += 1
    return result
    print(result)
  count_char(number)

length_number(4321)

#  print(f'El número: {number}','\n', 'Tiene un largo de: ', len(number))




# NOTA:

#  if total < 10:
#    return None, 'el total es muy chico'
#  elif total <= 20:
    return None, 'el total es mediano'
#  else:
    return total, 'el total es correcto'
