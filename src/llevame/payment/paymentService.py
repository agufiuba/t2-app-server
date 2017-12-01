class PaymentService:
    def __init__(self, interfaces):
        self.shared_service = interfaces.get_shared_server_service()

    def getPaymentMethods(self):
        response = self.sharedService.getPayMethods()
        return sharedResponse['items']
