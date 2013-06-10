#Es pycrypto de PyPI
from Crypto.Cipher import AES

# modulos de la biblioteca estandar
import base64
import hashlib

BLOQUE =  32
PADDING = '{'

def completar(cadena):
    """Completa una cadena para que sea multiplo de BLOQUE"""
    return cadena + (BLOQUE - len(cadena) % BLOQUE) * PADDING

clave = "mami te quiero"

key = hashlib.sha256(clave).digest()
print "Clave como sha: %s" % key
print len(key)

cifrador = AES.new(key)
#texto = pickle.dumps(mi_objeto)
texto = 'Mi texto a encriptar{'
en_base_64 = base64.b64encode(texto)
print "cadena como base 64: %s" % en_base_64

resultado = cifrador.encrypt(completar(en_base_64))

print "Cadena encriptada: %s" % resultado

descifrado = cifrador.decrypt(resultado)

print descifrado

print base64.b64decode(descifrado.rstrip(PADDING))
