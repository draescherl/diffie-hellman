import math
from secrets import randbelow


class DiffieHellman:

    def __init__(self, g, p):
        self.g = g
        self.p = p

    def generate_private_key(self):
        self.private_key = randbelow(self.p)

    def generate_public_key(self):
        public_key = math.pow(self.g, self.private_key)
        public_key = math.fmod(public_key, self.p)
        self.public_key = public_key
        print("public key : ", self.public_key)

    def get_partner_public_key(self, pub_key):
        self.partner_public_key = pub_key

    def compute_secret(self):
        secret = math.pow(self.partner_public_key, self.private_key)
        secret = math.fmod(secret, self.p)
        self.secret = secret

    def print_secret(self):
        print("s = ", self.secret)


df = DiffieHellman(5, 23)
df.generate_private_key()
df.generate_public_key()
df.get_partner_public_key(10)
df.compute_secret()
df.print_secret()
