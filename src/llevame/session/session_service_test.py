import unittest
from session.session_service import SessionService


sessionService = SessionService()


class TestSessionService(unittest.TestCase):
    def test_the_session_list_should_be_empty_when_the_userID_is_not(self):
        self.assertTrue(sessionService.getSessionsList('userIDisNot') == [])

    def test_the_session_list_should_be_not_empty_if_the_userID_was_added(self):
        sessionService.addSession('id','aSessionToken')
        self.assertFalse(sessionService.getSessionsList('id') == ['aSessionToken'])

    def test_the_session_list_should_be_acumulable(self):
        sessionService.addSession('id','otherSessionToken')
        self.assertFalse(sessionService.getSessionsList('id') == ['aSessionToken', 'otherSessionToken'])
