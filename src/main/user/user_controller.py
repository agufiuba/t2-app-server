from flask import Blueprint

user_controller = Blueprint('controller',__name__)

@user_controller.route('/user',methods = ['POST'])
def add_user():
    return 'Add new user'


@user_controller.route('/user',methods = ['PUT'])
def update_user():
    return 'Update a user'


@user_controller.user('/user/<id>',methods = ['GET'])
def see_user(id):
    return 'See user information'id

@user_controller.user('/user/<id>',methos = ['DELETE'])
def delete_user(id):
    return 'Delete user'+id
