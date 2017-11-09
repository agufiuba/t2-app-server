from shared_service import shared_server_service as sharedService



def getPaymentMethods():
    listOfPaymentMethods = sharedService.getPayMethods()
    return listOfPaymentMethods
