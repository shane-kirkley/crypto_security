import hashlib

f = open("preimage.txt", 'w')

# add john's identikey
identikey = 'shki1742'
number = 0

# find a string that starts with identikeys of group, followed by a number,
# that when hashed with SHA256 produces a (256-bit) number that starts with
# at least 24-bits of 0s. (6 hex-0's)

while(True):
    hashed = hashlib.sha256(identikey + str(number)).hexdigest()
    if str(hashed[:6]) == '000000':
        print "found: " + identikey + str(number) + ' ' + hashed
        f.write(identikey + str(number) + ' ' + hashed)
        f.close()
        quit()
    number = number + 1
