import hashlib
h = hashlib.new("sha1", b"1")
print(h.digest())
print(h.hexdigest())
print(type(h.hexdigest()))