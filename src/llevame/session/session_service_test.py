import unittest
from session import session_service as sessionService



class TestSessionService(unittest.TestCase):
    def test_the_session_list_should_be_empty_when_the_userID_is_not(self):
        assertTrue(sessionService.getSessionsList('userIDisNot') == [])

    def test_the_session_list_should_be_not_empty_if_the_userID_was_added(self):
        sessionService.addSession('id','aSessionToken')
        assertTrue(sessionService.getSessionsList('id') == ['aSessionToken'])

    def test_the_session_list_should_be_acumulable(self):
        sessionService.addSession('id','otherSessionToken')
        assertTrue(sessionService.getSessionsList('id') == ['aSessionToken','aSessionToken'])
