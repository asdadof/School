from pwn import *
io = remote("helsectf2025-42694257c6fdb3976dd6-remote.chals.io", 443, ssl=True)
io.interactive()