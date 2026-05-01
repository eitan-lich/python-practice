import paramiko

# from classes import Animal
#
# zebra = Animal("mammal", 1.30, 350)
#
# print(zebra)
# print(zebra.get_type())
# type(zebra)

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect("localhost",username="eitan",password="emoky94")
ssh_client.exec_command("touch created_from_python")
stdin, stdout, stderr = ssh_client.exec_command("ls -la")
stdin, stdout, stderr = ssh_client.exec_command("ethtool eth0")
print(stdout.read().decode())
ssh_client.close()
