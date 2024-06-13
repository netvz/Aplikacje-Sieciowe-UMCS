import ipaddress

user_ip = input("IP: ")

def validate(ip):

    try:
        ipaddress.ip_address(ip)
        return "Adress is valid"
    except ValueError:
        return "Adress is not valid please provide the right address"
    
print(validate(user_ip))
