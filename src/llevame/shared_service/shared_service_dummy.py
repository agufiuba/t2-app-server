class SharedServiceDummy:
    def __init__(self):
        self.lista_usuarios=[]

    def getToken(self):
        return 12345

    def addUser(self, user):
        #TODO me tengo que fijar si está?
        self.lista_usuarios.append(user)
        return true

    def getUserFromEmail(self, email):
        return next((user for user in self.lista_usuarios if user["mail"] == email), None)

    def deleteUser(self, id):
        return 'deleteUser'

    def getCostFromDistanceInKM(self, userEmail,distanceInKM):
        return {'costo': 5*distanceInKM}

    def getPayMethods(self):
        # TODO si se testea, implementar esta parte del dummy.
        return None
