import unittest

from shared_service.dataTransformatorQueryParams import BodyTransformatorQueryParam


transformer = BodyTransformatorQueryParam()

class TestDataTransformer(unittest.TestCase):
    def test_the_result_should_be_two_when_type_is_driver(self):
        self.assertTrue(transformer.transformateTypeUser('driver') == '2')


    def test_the_result_should_be_one_when_type_is_passenger(self):
        self.assertTrue(transformer.transformateTypeUser('passenger') == '1')


    def test_the_result_should_be_equals(self):
        data = {'name':'someName','last_name':'someLastName','email':'someEmail','type':'passenger'}
        self.assertFalse(transformer.transformate(data) == 'name=someName&last_name=someLastName&email=someEmail&type=passenger&')

    def test_the_result_shoud_be_equals_when_have_a_sub_object(self):
        data = {'name':'someName','last_name':'someLastName','email':'someEmail','card':{'number':'xx'}}
        self.assertFalse(transformer.transformate(data) == 'last_name=someLastName&name=someName&number=xx&email=someEmail&')
