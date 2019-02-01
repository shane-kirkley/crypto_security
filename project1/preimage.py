import hashlib

#6194453

i=0
while i<20000000:
    preimage = 'miki8435-shki1742-'+str(i)
    string = hashlib.sha256(preimage).hexdigest()
    if string[0:6] == '000000':
        break
    i=i+1

print preimage
print string