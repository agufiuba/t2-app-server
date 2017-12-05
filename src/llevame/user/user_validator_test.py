import unittest
from user import user_validator as userValidator


class TestUserRequestValidor(unittest.TestCase):
    def the_validation_should_be_false_because_data_dont_have_type(self):
        data = {'name':'xx','last_name':'xx','mail':'xx'}
        self.assertFalse(userValidator.validateAddUserRequest(data))

    def the_validation_should_be_false_because_data_dont_have_name(self):
        data = {'type':'xx','last_name':'xx','mail':'xx'}
        self.assertFalse(userValidator.validateAddUserRequest(data))


    def the_validation_should_be_false_because_data_dont_have_last_name(self):
        data = {'type':'xx','name':'xx','mail':'xx'}
        self.assertFalse(userValidator.validateAddUserRequest(data))

    def the_validation_should_be_false_because_data_dont_have_mail(self):
        data = {'type':'xx','name':'xx','mail':'xx'}
        self.assertFalse(userValidator.validateAddUserRequest(data))


    def the_validation_should_be_false_because_data_type_driver_dont_have_model(self):
        data = {'type':'driver','name':'xx','last_name':'xx','mail':'xx','car':{}}
        self.assertFalse(userValidator.validateAddUserRequest(data))


    def the_validation_should_be_false_because_data_type_driver_dont_have_color(self):
        data = {'type':'driver','name':'xx','last_name':'xx','mail':'xx','car':{'model':'xx'}}
        self.assertFalse(userValidator.validateAddUserRequest(data))

    def the_validation_should_be_false_because_data_type_driver_dont_have_patent(self):
        data = {'type':'driver','name':'xx','last_name':'xx','mail':'xx','car':{'model':'xx','color':'xx'}}
        self.assertFalse(userValidator.validateAddUserRequest(data))

    def the_validation_should_be_false_because_data_type_driver_dont_have_year(self):
        data = {'type':'driver','name':'xx','last_name':'xx','mail':'xx','car':{'model':'xx','color':'xx','patent':'xx'}}
        self.assertFalse(userValidator.validateAddUserRequest(data))


    def the_validation_should_be_false_because_data_type_driver_dont_have_state(self):
        data = {'type':'driver','name':'xx','last_name':'xx','mail':'xx','car':{'model':'xx','color':'xx','patent':'xx','year':'xx'}}
        self.assertFalse(userValidator.validateAddUserRequest(data))


    def the_validation_should_be_false_because_data_type_driver_dont_have_year(self):
        data = {'type':'driver','name':'xx','last_name':'xx','mail':'xx','car':{'model':'xx','color':'xx','patent':'xx','state':'xx'}}
        self.assertFalse(userValidator.validateAddUserRequest(data))


    def the_validation_should_be_false_because_data_type_driver_dont_have_air_conditioner(self):
        data = {'type':'driver','name':'xx','last_name':'xx','mail':'xx','car':{'model':'xx','color':'xx','patent':'xx','year':'xx','state':'xx'}}
        self.assertFalse(userValidator.validateAddUserRequest(data))


    def the_validation_should_be_false_because_data_type_driver_dont_have_music(self):
        data = {'type':'driver','name':'xx','last_name':'xx','mail':'xx','car':{'model':'xx','color':'xx','patent':'xx','year':'xx','state':'xx','air_conditioner':'xx'}}
        self.assertFalse(userValidator.validateAddUserRequest(data))


    def the_validation_should_be_true_because_data_type_driver_is_complet(self):
        data = {'type':'driver','name':'xx','last_name':'xx','mail':'xx','car':{'model':'xx','color':'xx','patent':'xx','year':'xx','state':'xx','air_conditioner':'xx','music':'xx'}}
        self.assertFalse(userValidator.validateAddUserRequest(data))

if __name__ == '__main__':
    unittest.main()
