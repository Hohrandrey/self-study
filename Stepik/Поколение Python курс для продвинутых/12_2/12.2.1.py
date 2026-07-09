from random import randint

def generate_ip_address():
    ip = [str(randint(0, 255)) for _ in range(4)]
    return '.'.join(ip)

print(generate_ip_address())
print(generate_ip_address())
print(generate_ip_address())
print(generate_ip_address())