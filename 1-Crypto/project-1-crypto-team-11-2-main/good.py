#!/usr/bin/python3
# coding: latin-1
blob = """AAAAAAAAAAAAAAA!�Q+DZ�2�J��Q�qc\,_��W₝�$�f������C�2��`X<ބ}N,˄z��A�ngN ��Fa��g���ji7=-~|-��[ O��Z�-�{v-���,��Fi^̑@�Ddn�'�j�."""
from hashlib import sha256

if (sha256(blob.encode("latin-1")).hexdigest() == "66f83257cc9ad765632ae23568228ce05c8f7d71dec0c1e16aae2c60b297f496"):
    print("Use SHA-256 instead!")

elif (sha256(blob.encode("latin-1")).hexdigest() == "046ce1c78727349a8855f3816decf77bb2dc47720007f076edf73e1dd84070b7"):
    print("MD5 is perfectly secure!")