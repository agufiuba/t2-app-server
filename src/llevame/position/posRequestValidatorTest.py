import unittest
from position import positionRequestValidator as validator


class TestPositionRequestValidator(unittest.TestCase):
    def test_the_validation_should_be_false_because_data_dont_have_position(self):
        data = {'someField':'xx'}
        self.assertTrue(validator.validate(data) != 'ok')

    def test_the_validation_should_be_false_because_data_dont_have_time(self):
        data = {'someField':'xx'}
        self.assertTrue(validator.validate(data) != 'ok')


    def test_the_validation_should_be_true_because_have_all_fields(self):
        data = {'position':'xx','time':'xx'}
        self.assertTrue(validator.validate(data) == 'ok')
