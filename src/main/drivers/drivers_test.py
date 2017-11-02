def init_base():
    

import request s

def test_1():
    # Tiene que hacer un request a la dirección con el coso levantado.
    return 0

def test_get():
    r = requests.get("localhost:3000")
    print(r.text)
    assert r.text == "[]"
