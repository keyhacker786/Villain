from pwn import *
print("starting server")

l = listen(4444)

l.wait_for_connection()

print(l.recv())




# r = process(['python3'], stdin=PTY, raw=False)
# print(r.recv())
# l = listen(8888)

# print("Listening for connections")

# while 1:
#   l.wait_for_connection()
#   print("Got connection")
#   while l:
#     r.sendline(l.recvline())
#     print(r.recv())
