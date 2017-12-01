class Interfaces:
    def __init__(self, firebase_service, mongo_uri, mongo_db_name, shared_server_service):
        self.firebase_service = firebase_service
        self.mongo_uri = mongo_uri
        self.mongo_db_name = mongo_db_name
        self.shared_server_service = shared_server_service

    def get_firebase_service(self):
        return self.firebase_service

    def get_mongo_uri(self):
        return self.mongo_uri

    def get_mongo_db_name(self):
        return self.mongo_db_name

    def get_shared_server_service(self):
        return self.shared_server_service
