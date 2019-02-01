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

    # to authenticate, need copy of public key curve point (pk)
    # First, verify pk is a valid curve point
    #   - check that pk is not equal to the identity element O=nG, and it's
    #     coords are otherwise valid.
    #   - check that pk lies on the curve
    #   - check that n x pk = O = nG
    # Then,
    # 1. verify that r and s are integers in [1,n-1]. If not, sig is invalid
    # 2. calculate e = HASH(m)
    # 3. let z be the Ln leftmost bits of e
    # 4. calculate w = s^-1 mod n
    # 5. calculate u1 = zw mod n and u2 = rw mod n
    # 6. calculate the curve point (x1, y1) = u1 x G + u2 x pk. if (x1, y1) = O=nG,
    #    then the signature is invalid
    # 7. The signature is valid if r == x1 mod n, invalid otherwise

    # verify pk is not equal to identity
    identity = curve.G().mult(curve.n)
    if pk == identity:
        return False
    
    # check that pk lies on the curve
    if not curve.on_curve(pk.x, pk.y):
        return False
    
    # verify n x pk == identity
    if pk.mult(curve.n) != identity:
        return False
    
    # now we know pk is a valid curve point.
    # verify r and s are integers in [1,n-1]
    if not (r > 1 and r < curve.n-1 and s > 1 and s < curve.n-1):
        # make this prettier?
        return False
    
    # calculate e = HASH(m)


    raise Exception('Not implemented!')


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

    pub_key = '0220b6617270f57c3cd2bc3f14f5c7c37390ca790c4e30e65f77d4d9af7e6e14fb'
    pk = ecdsa.decode_pk(pub_key)
    # *******************************************************
    # TODO: Write your code for pairing messages to signatures here


    # *******************************************************
    # TODO: (Graduate students only, optional for undergrad)
    #       Write your code for extracting the private key
    #       and signing your own message here
