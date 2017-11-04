from firebase import firebase_service

def login(request):
    id_token = request.form['Authorization']
    firebase_service.validate_token(id_token)
    return 'Login correct',200
