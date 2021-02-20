
# Función para determinar el largo de un número
def length_number():
  number = (input("Ingresa un número: "))
  def count_characters(number2):
    number2 = str(number)
    result: 0
    for char in number2:
      result += 1
    return result
  print (int(count_characters()))

#  print(f'El número: {number}','\n', 'Tiene un largo de: ', len(number))

length_number()




# NOTA:

#  if total < 10:
#    return None, 'el total es muy chico'
#  elif total <= 20:
    return None, 'el total es mediano'
#  else:
    return total, 'el total es correcto'
