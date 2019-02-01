import hashlib

# 7 hex zeros 265881397
# 00000000465914b1 ...

i = 10000000000
while i<12000000000:
    preimage = 'miki8435-shki1742-'+str(i)
    string = hashlib.sha256(preimage).hexdigest()
    if string[0:8] == '00000000':
        print '-----------------------------------'
        print preimage
        print string
    elif i%100000000 == 0:
        print i
    i=i+1

#print preimage
#print string