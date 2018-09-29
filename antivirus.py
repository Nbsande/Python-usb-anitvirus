import hashlib
import os

dirName='c:\\Users\\Neil\\Desktop\\Antivirus\\Python-usb-anitvirus'

def storeCreator(hashesDict, masterHash):
    #creating the text for the enil file
    tempFiles=list(hashesDict.keys())
    print(tempFiles)
    tempHashes=list(hashesDict.values()) 
    #preparing the CSV string of files in a ciphered way
    files=""
    files=encrypter(tempFiles,files)
    files=files+"\n"
    #preparing CSV string of hashes in a ciphered way
    hashes=""
    hashes=encrypter(tempHashes,hashes)
    hashes=hashes+"\n"
    #preparing masterHash in a ciphered way
    masterHash=encrypterString(masterHash,masterHash)
    
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
            
    storeCreator(hashesDict,masterHash)
    #returns (files,hashes,masterHash) all of which are strings


def encrypter(unencryptedList,CSVstring):
 #Takes a list of strings as input and outputs a single string made up of the values of the list encrypted based on the cipherSource 
 #and the values in the string are separated by commas  
    cipherSource="abCDlm:nfcde)istuxyzv-UVWjkBghGYoEFpq+rw*1(2H89\\0.~53K LIMQ_T467RS+NOP=/AZ;"
    for fileName in unencryptedList:
        length=len(fileName)
        proxy=""
        for char in range(0,length):
            
            if fileName[char]==",":
                proxy=proxy+","
            else:    
                indexNum=cipherSource.index(str(fileName[char]))+1
                proxy=proxy+cipherSource[indexNum]
            #print(proxy)    
        CSVstring=proxy+","
    print(CSVstring)
    return CSVstring
def encrypterString(unencryptedString,CSVstring):
    cipherSource="abCDlm:nfcde)istuxyzv-UVWjkBghGYoEFpq+rw*1(2H89\\0.~53K LIMQ_T467RS+NOP=/AZ;"
    length=len(unencryptedString)
    proxy=""
    for char in range(0,length):
        indexNum=cipherSource.index(str(unencryptedString[char]))+1
        proxy=proxy+cipherSource[indexNum]
    CSVstring=proxy+","
    return CSVstring    
            #dn0Vt)wt0O)sm0l)tBuEq0Zfus-swxt0=zuGEfUxtCUbfsu-swxt0~hsu0DPQQ
            #c:\Users\Neil\Desktop\Antivirus\Python-usb-anitvirus\.git\COMMIT_EDITMSG

def decrypter(CSVstring,outputString):
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
    dictcreator(getListOfFiles(dirName))
    with open(".hashstore.enil","w") as f:
        f.write(files)
        f.write(hashes)
        f.write(masterHash)
        f.close()
    print("Hash checker 'ENIL' file did not exist previously so one has been created") 

def ENILfileFound():
    with open('.hashstore.enil','r') as f:
        sums=f.readlines()
        sums =[x.strip() for x in sums]
        f.close()
        files=sums[0]
        hashes=sums[1]
        masterHash=sums[2]
        antiModChecker(files,hashes,masterHash)

#def comparer(list_a,list_b):
    

def antiModChecker(oFiles,oHashes,oMasterHash):
    allFiles=getListOfFiles(dirName)
    cFiles,cHashes,cMasterHash=dictcreator(allFiles)
    

a,b,c=dictcreator(getListOfFiles(dirName))
print(a)