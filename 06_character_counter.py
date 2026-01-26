# Contador de longitud de la cadena
def count_long(text):
    return len(text)

result_1 = count_long("luis")
print (result_1)


# Contador de caracter especifico
def count_character(text, character):
    return text.count(character)

result_2 = count_character("luis", "s")
print(result_2)

# Contador de caracteres general
def count_character_automatic(text):
    result_3 = {}
    for character in text:
        result_3[character] = text.count(character)
    return result_3
    
print(count_character_automatic("papa"))

    
    





