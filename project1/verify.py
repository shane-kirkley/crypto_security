#!/usr/bin/python

import hashlib

def ecdsa_verify(msg, pk, (r, s), curve=None, hash_fn=hashlib.sha256):
    '''Verifies a signature on a message.
    msg is a string,
    pk is an ecdsa.ECPoint representing the public key
    (r, s) is the signature tuple (use ecdsa.decode_sig to extract from hex)
    '''
    # Boilerplate, leave this alone
    import ecdsa
    if curve is None:
        curve = ecdsa.secp256k1

    # *********************************************************
    # TODO: Remove the raise Exception() and implement your ecdsa_verify function here:
    # Refer to ecdsa.ecdsa_sign() for examples in hashing the message,
    # and doing point multiplication.
    # See https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm#Signature_verification_algorithm
    # for the algorithm.

    O = curve.G().mult(curve.n)

    if not (pk.curve.on_curve(pk.x, pk.y)):
        #print("Public key is not on curve")
        return False

    if (pk.x == O.x and pk.y == O.y):
        #print("Public key is equal to identity element")
        return False

    pkO = pk.mult(curve.n)

    if not (pkO.x == O.x and pkO.y == O.y):
        #print("Public key multiplied by n does not equal to identity element")
        return False

    if r<1 or r>=curve.n or s<1 or s>=curve.n:
        #print("r or s out of bound")
        return False
        
    e = hash_fn(msg).hexdigest()
    z = int(e, 16)

    w = ecdsa.modinv(s, curve.n) % curve.n

    u_1 = z*w % curve.n
    u_2 = r*w % curve.n
    
    U = curve.G().mult(u_1)
    xy = U.add(pk.mult(u_2))

    if (xy.x == O.x and xy.y == O.y):
        #print("(x1, y1) = O - Signature invalid")
        return False

    if r == xy.x % curve.n:
        return True
    
    #print("r != x1")
    return False

    #raise Exception('Not implemented!')


if __name__ == '__main__':
    import ecdsa

    msgs = [
    'Hello, world',
    'The Magic Words are Squeamish Ossifrage.',
    'Attack at Dawn',
    'Attack at Dusk',
    'Create nonces randomly!',
    'Create nonces deterministically!']

    sigs = [
    'e1ca8ca322e963a24e2f2899e21255f275c2889e89adc14e225de6f338d7295aa9ab4ba5ddaa4366c4b32fb2b32371d768431b9c2cd7eee487215370a1196b49',
    'a86f5a5539e9ac49311c610f120e173ce8cb45f9493fe6a27dd81a1a22b08a2ce26a64013af4a894ab6e71df3dc3b775c8805de7c802f2e43791828be31a330c',
    'e1ca8ca322e963a24e2f2899e21255f275c2889e89adc14e225de6f338d7295ae556841b91642ea868014a9616e8ae6a8ae35bacf2e85f6e556d4bda910374f1',
    '64a70a19b87fe1c418964fe1751bbe641ea3d2f1cd70e346c722b59cdac587d857974c4683faa977789a78db471fc0cc7fafd20f31d67097e77b110789593029',
    '5b1a427f8d61345b15c716203c1e15b4370a1c841a92e88d61e021b794a209962f342d6467ae8c29a7fb25619e107381b5b252df90fe8d54bc6ecd2f41d66b83',
    'd580841c6864728bcf664a62c3ed552974c252badbecc53c53fe14e1ee922fb0b5186168ffd3cc798186660d5afadab9e088ac9f3397b64c7437bf2926d871a9']

    hash_fn=hashlib.sha256
    curve = ecdsa.secp256k1

    pub_key = '0220b6617270f57c3cd2bc3f14f5c7c37390ca790c4e30e65f77d4d9af7e6e14fb'
    pk = ecdsa.decode_pk(pub_key)

    # *******************************************************
    # TODO: Write your code for pairing messages to signatures here

    sig_ordered = {}

    for msg in msgs:
        for sig in sigs:
            d_sig = ecdsa.decode_sig(sig)
            if ecdsa_verify(msg, pk, d_sig):
                sig_ordered[msg]=sig
                print(msg+' '+sig)
                sigs.remove(sig)
                break

    # *******************************************************
    # TODO: (Graduate students only, optional for undergrad)
    #       Write your code for extracting the private key
    #       and signing your own message here

    z = int(hash_fn('Create nonces randomly!').hexdigest(),16)
    z_ = int(hash_fn('Create nonces deterministically!').hexdigest(),16)

    (r,s) = ecdsa.decode_sig('e1ca8ca322e963a24e2f2899e21255f275c2889e89adc14e225de6f338d7295aa9ab4ba5ddaa4366c4b32fb2b32371d768431b9c2cd7eee487215370a1196b49')
    (r_,s_) = ecdsa.decode_sig('e1ca8ca322e963a24e2f2899e21255f275c2889e89adc14e225de6f338d7295ae556841b91642ea868014a9616e8ae6a8ae35bacf2e85f6e556d4bda910374f1')

    if not (r == r_):
        print('not same')

    print('====================================')

    # k = ((z - z_) / (s - s_)) % curve.n
    k = ((z - z_) * ecdsa.modinv(s - s_, curve.n)) % curve.n

    # d = ((s*k - z) / r) % curve.n
    d = (ecdsa.modinv(r, curve.n) * (s*k - z)) % curve.n

    pk2 = ecdsa.publickey(d)
    print 'Public_key =', pub_key
    print 'My pub_key =', ecdsa.encode_pk(pk2)
    print('====================================')
