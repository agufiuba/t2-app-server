from ..firebase import firebase_service as firebaseService

def login(request):
    id_token = request.form['Authorization']
    firebaseService.validate_token(id_token)
    return 'Login correct',200
