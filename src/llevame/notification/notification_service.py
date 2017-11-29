from session import session_service as sessionService

def notificate_user(userID):
    session_list = sessionService.getSessionsList(userID)
    for session in session_list:
        notificate(session)
    return True

def notificate(sessionID):
    return True
