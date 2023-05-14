from pwn import *
print("starting server")
r = process(['python3 Villain.py'], stdin=PTY, raw=False)
print(r.recv())
l = pwn.listen(8888)

print("Listening for connections")

while 1:
  l.wait_for_connection()
  print("Got connection")
  while l:
    r.sendline(l.recvline())
    print(r.recv())
