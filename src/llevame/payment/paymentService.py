from shared_service import shared_server_service as sharedService



def getPaymentMethods():
    listOfPaymentMethods = sharedService.getPaymentMethods()
    return listOfPaymentMethods
