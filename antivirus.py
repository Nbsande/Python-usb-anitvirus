import hashlib
import os
def checkSumFounds():
#If hashchecker.enil file found it will check that the hash of files is same as that in ENIL file
    files.remove('hashchecker.enil')
    singleHash=""""""
    allHash=[]
    sha256_hash = hashlib.sha256()
    print(1)
    for filename in files:
        with open(filename,"rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)
                g=sha256_hash.hexdigest()
            allHash.append(sha256_hash.hexdigest())
                
            singleHash=singleHash+str(sha256_hash.hexdigest())
    singleHash.encode('ascii')
    singleHash=bytes(singleHash,'ascii')
    hash_object = hashlib.sha256(singleHash)
    singleHash = hash_object.hexdigest()
    print(singleHash)
    with open('hashchecker.enil','r') as f:
        sums=f.readlines()
        sums = [x.strip() for x in sums]
        f.close()

def checkSumFound():
#If hashchecker.enil file found it will check that the hash of files is same as that in ENIL file
    files.remove('hashchecker.enil')
    singleHash=""""""
    allHash=[]
    sha256_hash = hashlib.sha256()
    print(1)
    for filename in files:
        with open(filename,"rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)
                g=sha256_hash.hexdigest()
            allHash.append(sha256_hash.hexdigest())
                
            singleHash=singleHash+str(sha256_hash.hexdigest())
    singleHash.encode('ascii')
    singleHash=bytes(singleHash,'ascii')
    hash_object = hashlib.sha256(singleHash)
    singleHash = hash_object.hexdigest()
    
    with open('hashchecker.enil','r') as f:
        sums=f.readlines()
        sums = [x.strip() for x in sums]
        f.close()
    sums.pop(0)
    if sums[0]==allHash[0]:
        print("Checksums match")
    else:
        if len(sums)==(len(allHash)):
            for n in range(0,len(allHash)):
            
                if sums[n]==allHash[n]:
                    print("continue")
                    
                else:
                    print(3)
                    print("The "+str(files[n])+" file has been modified")
        else:
            print(sums)
            print("\n")
            print(allHash)
                    
def noCheckSum():
#If ENIL file not found then it will create one
    singleHash=""""""
    allHash=[]
    sha256_hash = hashlib.sha256()
    for filename in files:
        with open(filename,"rb") as f:
             # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)
                g=sha256_hash.hexdigest()
            allHash.append(sha256_hash.hexdigest())
                
            singleHash=singleHash+str(sha256_hash.hexdigest())
    singleHash.encode('ascii')
    singleHash=bytes(singleHash,'ascii')
    hash_object = hashlib.sha256(singleHash)
    singleHash = hash_object.hexdigest()
    with open("hashchecker.enil","w") as f:
        f.write(singleHash)
        f.write("\n")
        for n in allHash:
            f.write(n)
            f.write("\n")
        f.close()
    print("Hash checker 'ENIL' file did not exist previously so one has been created")

files=[]
for entry in os.scandir('.'):
    if entry.is_file():
        files.append(entry.name)
if "hashchecker.enil" in files:
                              checkSumFound()
else:
                              noCheckSum()

