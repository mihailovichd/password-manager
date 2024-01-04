import hashlib
import requests
from config import API_URL


def encrypt(password, alg='sha256') -> str:
    h = hashlib.new(alg)
    h.update(password.encode('ascii'))
    return h.hexdigest()


def check_password(password) -> bool:
    password = encrypt(password, 'sha1').upper()

    url = API_URL + password[:5]
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError

    data = (line.split(':') for line in response.text.splitlines())
    return not any(suffix == password[5:] for suffix in data)
