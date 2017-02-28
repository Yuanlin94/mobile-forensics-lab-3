import hashlib
 
hasher = hashlib.md5()
with open('MDF-SF1.docx', 'rb') as afile:
    buf = afile.read()
    hasher.update(buf)
print('The hash code of MDF-SF1.docx is ' + hasher.hexdigest())

hasher = hashlib.md5()
with open('MDF-SF2.docx', 'rb') as afile:
    buf = afile.read()
    hasher.update(buf)
print('The hash code of MDF-SF2.docx is ' + hasher.hexdigest())