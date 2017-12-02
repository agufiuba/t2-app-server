import unittest
from app_builder import build_app
from my_firebase.firebase_dummy import FirebaseDummy
from interfaces import Interfaces
from shared_service.shared_service_dummy import SharedServiceDummy
import os

from flask import json

class TestDriversService(unittest.TestCase):
    def setUp(self):
        datos = {
            'id': 10,
            'name': 'Abraham',
            'last_name': 'Adams',
            'mail': 'abadams@gmail.com',
            'type': 1,
            'saldo': '0'}

        fb_dummy = FirebaseDummy()
        fb_dummy.add_user("123", datos)

        interfaces = Interfaces(\
            firebase_service = fb_dummy, \
            mongo_uri = os.environ['MONGO_URI'], \
            mongo_db_name = "t2-test", \
            shared_server_service = SharedServiceDummy())
        app = build_app(interfaces)
        app.testing = True
        self.app = app.test_client()

# TODO podría evaluarse un token erróneo.

    def test_get(self):
        rv = self.app.get("/drivers?pos=lat/lng:%20(-34.6220855,-58.3832781)", headers = {
            "Authorization": "123",
            "Content-Type": "application/json",
            "Session": 321
        })
        self.assertEqual(json.loads(rv.data), {"drivers": []})

if __name__ == '__main__':
    unittest.main()
