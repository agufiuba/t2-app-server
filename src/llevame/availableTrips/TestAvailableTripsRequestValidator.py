import unittest


from availaleTrips.availaleTripsRequestValidator import RequestValidator

validator = RequestValidator()

class TestUserService(unittest.TestCase):
    def the_validate_should_return_false_because_is_not_from(self):
        assertTrue(validator.validate({'no':'xx'}) != 'ok')

    def the_validate_should_return_false_because_is_not_to(self):
        assertTrue(validator.validate({'from':'xx'}) != 'ok')

    def the_validate_should_return_true_because_is_complet(self):
        assertTrue(validator.validate({'from':'xx','to':'xx'}) == 'ok')
