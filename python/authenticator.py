import hmac, base64, struct, hashlib, time

def get_hotp_token(secret, intervals_no):
    key = base64.b32decode(secret, True)
    h = struct.pack(">Q", intervals_no)
    o = hmac.new(key, h, hashlib.sha1).digest()
    t = ord(o[19]) & 15
    p = (struct.unpack(">I", o[t:t+4])[0] & 0x7fffffff) % 1000000
    return p

def get_token(secret):
    return get_hotp_token(secret, intervals_no=int(time.time())//30)
