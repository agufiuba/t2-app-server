import unittest
from trips_request_validator import validate

class Req:
    def __init__(self, json_dict):
        self.json = json_dict

    def get_json(self):
        return self.json

class TestTripsRequestValidator(unittest.TestCase):

    def test_deberia_dar_ok_si_estan_todos_los_parametros(self):
        r = Req( { "driverID": "id", "from": "from", "to": "to", "paymentMethod": "cash" } )
        self.assertEqual(validate(r), "ok")
        r = Req( { "driverID": "id", "from": "from", "to": "to", "paymentMethod": "card" } )
        self.assertEqual(validate(r), "ok")

    def test_deberia_fallar_si_falta_id(self):
        r = Req( {"from": "from", "to": "to", "paymentMethod": "cash" } )
        self.assertEqual(validate(r), 'El ID del chofer no se encuentra, por favor verifique eso')

    def test_deberia_fallar_si_falta_from(self):
        r = Req( { "driverID": "id", "to": "to", "paymentMethod": "cash" } )
        self.assertEqual(validate(r), 'El <from> no se encuentra, por favor verifique eso')

    def test_deberia_fallar_si_falta_to(self):
        r = Req( { "driverID": "id", "from": "from", "paymentMethod": "cash"} )
        self.assertEqual(validate(r), 'El <to> no se encuentra, por favor verifique eso')

    def test_deberia_fallar_si_falta_payment(self):
        r = Req( { "driverID": "id", "from": "from", "to": "to" } )
        self.assertEqual(validate(r), 'El <paymentMethod> no se encuentra, por favor verifique eso')

    def test_deberia_fallar_si_no_es_cash_ni_card(self):
        r = Req( { "driverID": "id", "from": "from", "to": "to", "paymentMethod": "debit" } )
        self.assertEqual(validate(r), 'El método de pago "debit" no es válido. Debe ser "cash" o "card").')
