import os
import hashlib


def create_hash(size=16):
    """A varíavel size é definida com padrão 16 caracteres que é o mais utilizado pelos cenários que a consomem.
    Caso um valor não seja informado uma hash com 16 digitos será gerada"""
    random_data = os.urandom(128)
    return hashlib.md5(random_data).hexdigest()[:size]
