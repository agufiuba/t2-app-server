import unittest

from shared_service.dataTransformatorQueryParams import BodyTransformatorQueryParam


transformer = BodyTransformatorQueryParam()

class TestDataTransformer(unittest.TestCase):
    def test_the_result_should_be_two_when_type_is_driver(self):
        self.assertEqual(transformer.transformateTypeUser('driver'),'2')

    def test_the_result_should_be_one_when_type_is_passenger(self):
        self.assertEqual(transformer.transformateTypeUser('passenger'),'1')

    def test_the_result_should_be_equals(self):
        data = {'name':'someName','last_name':'someLastName','email':'someEmail','type':'passenger'}
        self.assertEqual(transformer.transformate(data), 'name=someName&last_name=someLastName&email=someEmail&type=1&')

    def test_the_result_shoud_be_equals_when_have_a_sub_object(self):
        data = {'name':'someName','last_name':'someLastName','email':'someEmail','card':{'number':'xx'}}
        self.assertEqual(transformer.transformate(data), 'name=someName&last_name=someLastName&email=someEmail&number=xx&')

    def test_wrong_type_returns_0(self):
        data = {'name':'someName','last_name':'someLastName','email':'someEmail','type':'pasajero'}
        self.assertEqual(transformer.transformate(data), 'name=someName&last_name=someLastName&email=someEmail&type=0&')
