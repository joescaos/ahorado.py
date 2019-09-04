import random  #SE IMPORTA RANDOM CON EL OBJETIVO DE USAR SUS METODOS
# SE CREA UNA LISTA CON LA INTERFAZ PARA EL JUEGO
IMAGES = ['''  

    +---+
    |   |
        |
        |
        |
        |
        ========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
        ========''', '''  
    +---+
    |   |
    O   |
    |   |
        |
        |
        ========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
        ========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
        ========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        ========''','''
    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        ========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        ========''','''
    ''']  #FINALIZACION DE LA INTERFAZ DEL JUEGO

# SE CREAN LAS PALABRAS LAS CUALES SE VAN A OBTENER ALEATOREAMENTE

WORDS = [
    'programador',
    'ingeniero',
    'arquitecto',
    'abogado',
    'militar',
    'politico',
    'presidente',
    'senador',
    'desarrollador'
]
def random_word():  # DEFINIMOS UNA FUNCION PARA OBTENER UNA PALABRA DE FORMA ALEATORIA DE LA LISTA WORDS
    index = random.randint(0, len(WORDS) - 1)  # VAMOS A ACCEDER A TRAVES DE UN INDICE DE LA LISTA LA CUAL
                                            # OBTENEMOS DE MANERA ALEATORIA DESDE O HASTA LA ULTIMA PALABRA
    return WORDS[index]  # RETORNAMOS UN INDICE DE LA LISTA WORDS

def display_board(hidden_word, tries):  # MOSTRAR LA PRIMER IMAGEN DEL JUEGO Y EL INTENTO
    print(IMAGES[tries])  # COMO EL INDICE INICIAL ES 0 IMPRIME LA PRIMER IMAGEN
    print('')  # UN ESPACIO 
    print(hidden_word) # IMPRIME LA PALABRA ESCONDIDA
    print('---* ---* ---* ---* ---* ---* ---* ---* ---* ---*') 


def run():  # FUNCION CON LA CUAL VAMOS A CORRER EL PROGRAMA
    word = random_word()  # CREAMOS UNA PALABRA ALEATORIA DE NUESTRA LISTA 
    hidden_word = ['_'] * len(word)  # LA VARIABLE HIDDENWORD CONTIENE EL TAMAÑO DE INDEX WORDS EN ESPACIOS VACIOS
    tries = 0

    while True:  #MIENTRAS SEA VERDADERO
        display_board(hidden_word, tries)  # SE MOSTRARA EN PANTALLA LA PALABRA ESCONDIDA Y EL INTENTO
        current_letter = input('Ingresa una letra: ')  # MENSAJE PARA QUE EL USUARIO INGRESE UNA LETRA

        letter_indexes = []

        for i in range (len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)

        if len(letter_indexes) == 0:
                tries += 1

                if tries == 7:
                    display_board(hidden_word, tries)
                    print('')
                    print('Perdiste! La palabra correcta era {}'.format(word))
                    break
        else:
            for index in letter_indexes:
                hidden_word[index] = current_letter
                
        letter_indexes = []

        if not '_' in hidden_word:
            display_board(hidden_word, tries)
            print('')
            print('Felicidades! Ganaste, la palabra era : {}'.format(word))
            break

if __name__ == "__main__":
    print('BIENVENIDO A EL JUEGO DE AHORCADOS')
    run()
