
def https_status(status):
    match(status):
        case 200:
            return "Ok"
        
        case 404:
            return "Error!"
        
        case 500:
            return "Internal check"
        
        case _:  #default case
            return "Unknown Status"
        
print(https_status(500))
print(https_status(404))
print(https_status(5000))