from src import AnonFiles

a = AnonFiles()

up = a.upload("example.py")

print(up.status)