import os
import hashlib
dirName='c:\\Users\\Neil\\Desktop\\Antivirus\\Python-usb-anitvirus'

def storeCreator(hashesDict, masterHash):
    #creating the text for the enil file
    tempFiles=list(hashesDict.keys())
    
    tempHashes=list(hashesDict.values()) 
    #preparing the CSV string of files in a ciphered way
    files=""
    files=encrypterList(tempFiles)
    files=files+"\n"
    #preparing CSV string of hashes in a ciphered way
    hashes=""
    hashes=encrypterList(tempHashes)
    hashes=hashes+"\n"
    #preparing masterHash in a ciphered way
    masterHash=encrypterString(masterHash)
    
    return(files,hashes,masterHash)

def dictcreator(allFiles):
    hashesDict={}
    masterHash=""
    sha256_hash = hashlib.sha256()
    for filename in allFiles:
        with open(filename,"rb") as f:
             # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)
                g=sha256_hash.hexdigest()
            hashesDict[filename]=g
            masterHash=masterHash+g   
            hash_object=hashlib.sha256(masterHash.encode())
            masterHash=hash_object.hexdigest()
            
    return(hashesDict,masterHash)
    #returns (files,hashes,masterHash) all of which are strings


def encrypterString(unencryptedString):
    CSVstring=''
    cipherSource="abCDlm:nfcde)istuxyzv-UVWjkBghGYoEFpq+rw*1(2H89\\0.~53K LIMQ_T467RS+NOP=/AZ;"
    length=len(unencryptedString)
    proxy=""
    for char in range(0,length):
        indexNum=cipherSource.index(str(unencryptedString[char]))+1
        proxy=proxy+cipherSource[indexNum]
    CSVstring=proxy+","
    correctedCSVstring=CSVstring[0:-1]
    return correctedCSVstring    

def encrypterList(unencryptedList):
    
    outputCSVstring=''
    for file_name in unencryptedList:
        proxy=encrypterString(file_name)
        outputCSVstring=outputCSVstring+','+proxy
    correctedOutputCSVstring=outputCSVstring[1:]
    return(correctedOutputCSVstring)

def decrypterString(CSVstring):
    outputString=''
    cipherSource="abCDlm:nfcde)istuxyzv-UVWjkBghGYoEFpq+rw*1(2H89\\0.~53K LIMQ_T467RS+NOP=/AZ;"
    length=len(CSVstring)
    proxy=""
    for char in range(0,length):
        if CSVstring[char]==",":
            proxy=proxy+","
        else:
            indexNum=cipherSource.index(str(CSVstring[char]))-1
            proxy=proxy+cipherSource[indexNum]
    outputString=proxy+","
    return outputString

def decrypterList(encryptedList):
    outputString=''
    for encrypted_item in encryptedList:
        proxy=decrypterString(encrypted_item)
        outputString=outputString+','+proxy
    correctedOutputCSVstring=outputString[1:]
    return(correctedOutputCSVstring)

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

def noENILfile():
    allFiles=getListOfFiles(dirName)
    hashesDict,masterHash=dictcreator(allFiles)
    files,hashes,masterHash=storeCreator(hashesDict,masterHash)
    print(files)
    print(hashes)
    print(masterHash)
    with open("hashstore.enil","w") as f:
        f.write(files)
        f.write(hashes)
        f.write(masterHash)
        f.close()
    print("Hash checker 'ENIL' file did not exist previously so one has been created")
def ENILfileFound():
    with open('hashstore.enil','r') as f:
        sums=f.readlines()
        sums =[x.strip() for x in sums]
        f.close()
        files=sums[0]
        hashes=sums[1]
        masterHash=sums[2]
        files=str(decrypterString(files))[0:-1]
        files=files.split(',')
        hashes=str(decrypterString(hashes))[0:-1]
        hashes=hashes.split(',')
        masterHash=decrypterString(masterHash)
        hashesDict={}
        if len(files)==len(hashes):    
            for n in range(len(files)):
                hashesDict[files[n]]=hashes[n]
        return(hashesDict,masterHash)
n="""
        antiModChecker(files,hashes,masterHash)

#def comparer(list_a,list_b):
   

def antiModChecker(oFiles,oHashes,oMasterHash):
    allFiles=getListOfFiles(dirName)
    cFiles,cHashes,cMasterHash=dictcreator(allFiles)
"""
noENILfile()