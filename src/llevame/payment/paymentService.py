from shared_service import shared_server_service as sharedService



def getPaymentMethods():
    response = sharedService.getPayMethods()
    return sharedResponse['items']
