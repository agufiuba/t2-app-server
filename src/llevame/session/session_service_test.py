import unittest
from session.session_service import SessionService


class TestSessionService(unittest.TestCase):
    def setUp(self):
        self.ss = SessionService()

    def test_the_session_list_should_be_empty_when_the_userID_is_not(self):
        self.assertTrue(self.ss.getSessionsList('userIDisNot') == [])

    def test_the_session_list_should_be_not_empty_if_the_userID_was_added(self):
        self.ss.addSession('id','aSessionToken')
        self.assertEqual(self.ss.getSessionsList('id'), ['aSessionToken'])

    def test_the_session_list_should_be_acumulable(self):
        self.ss.addSession('id','aSessionToken')
        self.ss.addSession('id','otherSessionToken')
        self.assertEqual(self.ss.getSessionsList('id'), ['aSessionToken', 'otherSessionToken'])
