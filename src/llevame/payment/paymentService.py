from shared_service import shared_server_service as sharedService



def getPaymentMethods():
    sharedResponse = sharedService.getPayMethods()
    return sharedResponse['items']
