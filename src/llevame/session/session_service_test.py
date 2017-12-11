import unittest
from session.session_service import SessionService


class TestSessionService(unittest.TestCase):
    def setUp(self):
        self.ss = SessionService()

    def test_the_session_list_should_be_empty_when_the_userID_is_not_present(self):
        self.assertTrue(self.ss.getSessionsList('userID_not_present') == [])

    def test_the_session_list_should_be_not_empty_if_the_userID_was_added(self):
        self.ss.addSession('id1','aSessionToken')
        self.assertEqual(self.ss.getSessionsList('id1'), ['aSessionToken'])

    def test_the_session_list_should_be_acumulable(self):
        self.ss.addSession('id2','aSessionToken')
        self.ss.addSession('id2','otherSessionToken')
        self.assertEqual(self.ss.getSessionsList('id2'), ['aSessionToken', 'otherSessionToken'])
