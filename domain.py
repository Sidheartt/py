 Create a function that grabs the email website domain from a string in the form
 So for example, passing "user@domain.com" would return: domain.com

def domainGet(var):
    return var.split('@')[1]
	
domainGet('user@domain.com')