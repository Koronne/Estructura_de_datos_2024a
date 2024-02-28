from ListaDinamicaCompleta_base import ListaDinamica
from string import ascii_lowercase as def_alph

class Caesar:
    def __init__(self, alphabet: str) -> None:
        ''' Inicializa herramienta criptográfica '''
        self.alphabet: ListaDinamica = self.set_alphabet(alphabet)

    def encrypt(self, msg: str, key: int, inverse=False) -> str:
        ''' Des/encriptar un mensaje '''
        result = ''
        for char in msg:
            if char.lower() in self.alphabet:
                idx = (self.alphabet.index(char.lower()) + key) % len(self.alphabet)
                if char.isupper():
                    result += self.alphabet[idx].upper()
                else:
                    result += self.alphabet[idx]
            else:
                result += char
        return result

    def multiple_decrypt(self, msg: str) -> str:
        ''' Herramienta interactiva para múltiples desencriptaciones '''
        decrypted_messages = []

        # Recorrer todas las claves posibles en el rango del tamaño del alfabeto
        for key in range(len(self.alphabet)):
            decrypted_messages.append(self.encrypt(msg, key, inverse=True))

        return decrypted_messages

    def set_alphabet(self, alphabet: str) -> ListaDinamica:
        ''' Definir alfabeto de la herramienta '''
        alph = ListaDinamica(len(alphabet))

        for e in alphabet:
            alph.append(e)

        return alph

if __name__ == '__main__':
    ''' Incluye aquí tus casos de prueba '''
    cesar = Caesar(def_alph)

    caso1 = 'UNE'
    caso2 = 'GuAdAlAjArA'

    print(cesar.encrypt(caso1, 2))

    mensaje_cifrado = 'Hola Don Chuy'
    mensajes_desencriptados = cesar.multiple_decrypt(mensaje_cifrado)

    # Imprimir los resultados
    for key, mensaje in enumerate(mensajes_desencriptados):
        print(f'Clave {key}: {mensaje}')