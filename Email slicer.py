#take email address as input
#slice email into dimensions
#name;domain_name;extension


while True:
    print("==============================================HAWONA'S EMAIL SLICER===============================================================================")
    email=input("Enter your email address: ")
    print("======================================================================================================================================================")

    (userName,domain)=email.split("@")
    (domain,extension)=domain.split(".")

    print("Name: ",userName)
    print("Domain: ",domain)
    print("Extension: ",extension)
