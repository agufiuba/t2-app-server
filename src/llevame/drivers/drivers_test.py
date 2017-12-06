import unittest
from app_builder import build_app
from my_firebase.firebase_dummy import FirebaseDummy
from interfaces import Interfaces
from shared_service.shared_service_dummy import SharedServiceDummy
from utils import positionTransformer

import os

from flask import json

# Los usuarios de la bdd de firebase_dummy. Son un pasajero y dos choferes.
# users = [
#     ("1", { 'id': 10, 'name': 'Abraham', 'last_name': 'Adams',
#         'mail': 'abadams@gmail.com', 'type': 1, 'saldo': '0'},
#         "lat/lng: (-34.6220855,-58.3832781)"),
#     ("2", { 'id': 11, 'name': 'Carlos', 'last_name': 'Fuentes',
#         'mail': 'cf@gmail.com', 'type': 2, 'saldo': '0'},
#         "lat/lng: (-34.6220855,-58.3832781)"),
#     ("3", { 'id': 12, 'name': 'Alberto', 'last_name': 'Gonzalez',
#         'mail': 'alberto_g@gmail.com', 'type': 2, 'saldo': '0'},
#         "lat/lng: (-34.6220855,-58.3832781)"),
# ]
#
# non_existant_user = ("4", { 'id': 13, 'name': 'Marta', 'last_name': 'Albear',
#     'mail': 'm_albear@hotmail.com', 'type': 1, 'saldo': '0'},
#     "lat/lng: (-34.6220855,-58.3832781)")
#
# def post_user(app, user):
#     rv = app.post("/drivers", headers = {"Authorization": user[0],
#         "Content-Type": "application/json", "Session": "321"})
#     return (rv.status_code, rv.data)
#
# def delete_user(app, user):
#     rv = app.delete("/drivers", headers = {"Authorization": user[0],
#         "Content-Type": "application/json", "Session": "321"})
#     return (rv.status_code, rv.data)
#
# class TestDriversService(unittest.TestCase):
#     def setUp(self):
#         fb_dummy = FirebaseDummy()
#         fb_dummy.add_user_list(users)
#         interfaces = Interfaces(\
#             firebase_service = fb_dummy, \
#             mongo_uri = os.environ['MONGO_URI'], \
#             mongo_db_name = "t2-test", \
#             shared_server_service = SharedServiceDummy())
#         app = build_app(interfaces)
#         app.testing = True
#         self.app = app.test_client()
#         self.fb = fb_dummy
#
#         # login de un driver.
#         post_user(self.app, users[1])
#
#     # Test básico.
#     def test_get(self):
#         rv = self.app.get("/drivers?pos=lat/lng:%20(-34.6220855,-58.3832781)",
#             headers = { "Authorization": "1","Content-Type": "application/json",
#                         "Session": "321"})
#     # TODO quitar hardcodeo de lat y long. Sacar a una función.
#         deberia_devolver = {"drivers": [
#             {"id": users[1][1]["id"], "pos": positionTransformer.parserStringToPosition(users[1][2])}
#         ]}
#         self.assertEqual(json.loads(rv.data), deberia_devolver)
#
#     # El usuario no existe, debería devolverse un error.
#     def test_get_nonexistant_user(self):
#         rv = self.app.get("/drivers?pos=lat/lng:%20(-34.6220855,-58.3832781)",
#             headers = { "Authorization": "5","Content-Type": "application/json",
#                         "Session": "321"})
#
#         self.assertEqual(rv.status_code, 400)
#         self.assertEqual(json.loads(rv.data),
#             {'message':'El token pasado no es valido'})
#
#     def test_logout(self):
#         (code, data) = delete_user(self.app, users[1])
#         self.assertEqual(code, 200)
#
#     def test_logout_nonexistant(self):
#         (code, data) = delete_user(self.app, non_existant_user)
#         self.assertEqual(code, 400)
#
#     # TODO que no se pueda hacer logout de uno no logueado.
#     # def test_logout_not_logged(self):
#     #     (code, data) = delete_user(self.app, user[2])
#     #     self.assertEqual(code, 400)
#
#     # TODO: Qué onda los logins múltiples?
#     def test_login(self):
#         (code, data) = post_user(self.app, users[2])
#         self.assertEqual(code, 200)
#
#     # TODO que no se pueda loguear si no está en firebase.
#     # def test_login_nonexistant(self):
#     #     (code, data) = post_user(self.app, non_existant_user)
#     #     self.assertEqual(code, 400)
#
#     # TODO: cuando ande el test_logout_not_logged, hacer un login, logout.
#
# if __name__ == '__main__':
#     unittest.main()
