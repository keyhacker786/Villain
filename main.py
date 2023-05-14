from pwn import *
r = process(['python3 Villain.py'], stdin=PTY, raw=False)
print(r.recv())
l = pwn.listen(8888)

while 1:
  l.wait_for_connection()
  while l:
    r.sendline(l.recvline())
    print(r.recv())
