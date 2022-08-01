with open("ca.crt","r") as ca_cert_file:
    ca_cert = ca_cert_file.read()
    print(ca_cert)

with open("client.crt","r") as client_cert_file:
    client_cert = client_cert_file.read()
    print(client_cert)

with open("client.key","r") as client_key_file:
    client_key = client_key_file.read()
    print(client_key)

with open("client3.ovpn","r") as client3_file:
    client_conf = client3_file.read()
    client_conf =client_conf.replace("ca ca.crt", "<ca> \n" + ca_cert + "</ca>")
    client_conf =client_conf.replace("cert client.crt", "<cert> \n" + client_cert + "</cert>")
    client_conf =client_conf.replace("key client.key", "<key> \n" + client_key + "</key>")

    print(client_conf)

with open("client_patched.ovpn","w+") as final_file:
    final_file.write(client_conf)
