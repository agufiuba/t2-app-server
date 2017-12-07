import unittest
from app_builder import build_app
from interfaces import Interfaces
from utils.position import Position
from my_firebase.firebase_service import FirebaseService
from drivers.drivers_service import DriverService
import os

from flask import json

users = [
    ("1", { 'id': "10", 'name': 'Abraham', 'last_name': 'Adams',
        'mail': 'abadams@gmail.com', 'type': 1, 'saldo': '0'},
        "lat/lng: (-34.6220855,-58.3832781)"),
    ("2", { 'id': "11", 'name': 'Carlota', 'last_name': 'Fuentes',
        'mail': 'cf@gmail.com', 'type': 2, 'saldo': '0'},
        "lat/lng: (-35.2,-58.3832781)"),
    ("3", { 'id': "12", 'name': 'Alberto', 'last_name': 'Gonzalez',
        'mail': 'alberto_g@gmail.com', 'type': 2, 'saldo': '0'},
        "lat/lng: (-35.6220855,-58.3832781)"),
]

non_existant_user = ("4", { 'id': 13, 'name': 'Marta', 'last_name': 'Albear',
    'mail': 'm_albear@hotmail.com', 'type': 1, 'saldo': '0'},
    "lat/lng: (-34.6220855,-58.3832781)")

def mockGetPosFromId(driverID):
    return Position(next(user[2] for user in users if user[1]["id"] == driverID))

class TestDriversService(unittest.TestCase):
    def setUp(self):
        fb = FirebaseService()
        fb.getPositionFromId = mockGetPosFromId
        self.ds = DriverService(fb)
        self.ds.login_driver("11")
        self.ds.login_driver("12")

    def test_logout_normal_deberia_dar_true(self):
        self.assertEqual(self.ds.delete_driver("11"), True)
        self.assertEqual(self.ds.delete_driver("12"), True)

    def test_logout_inexistente_deberia_dar_false(self):
        self.assertEqual(self.ds.delete_driver("13"), False)

    def test_no_logueado_deberia_dar_false(self):
        self.assertEqual(self.ds.delete_driver("11"), True)
        self.assertEqual(self.ds.delete_driver("11"), False)

    def test_el_pasajero_esta_cerca_del_driver_11(self):
        drivers = self.ds.getDriversAroundFrom(Position(users[0][2]))
        self.assertEquals(len(drivers),1)
        self.assertEquals(drivers[0]["id"], "11")

    def test_el_pasajero_NO_esta_cerca_del_driver_12(self):
        drivers = self.ds.getDriversAroundFrom(Position(users[0][2]))
        self.assertEquals(len(drivers),1)
        self.assertNotEquals(drivers[0]["id"], "12")
