import unittest
from app import build_app
import json

class TestDriversService(unittest.TestCase):
    def setUp(self):
        app = build_app(db = "t2-test")
        app.testing = True
        self.app = app.test_client()
        # Acciones de db?

    def test_get(self):
        rv = self.app.get("/drivers")
        self.assertEqual(str(rv.data,'utf-8'), "[]")

if __name__ == '__main__':
    unittest.main()
