# Python-USB-antivirus

## Goal:
To make a basic program that can check if there is a virus on a computer that might infect your USB if you insert it into that computer.


## How it Works:
On running for the first time in a directory, the utility makes a list of all files in the current directory and all sub-directories and calculates a hash on each of these files. These hashes are stored in a file (named hash store.enil) along with the list of filenames(with the letters jumbled). When running again the utility will detect that a .enil file already exists and will again calculate the hashes of all files and check those hashes against the hashes previously stored in the .enil file. The utility will report the names of modified files, deleted files and newly added files and will ask the user whether they would like to add newly added files to the hash store.


## How to Use this program:
This program is meant to be used as a utility to quickly and safely check whether a particular computer is affected by a virus that infects storage drives that connect to it. To do this we will put some files like the ones included in this repository onto a USB drive along with this Malware Utility and run the Utility on a computer we know to be safe(for example your home computer). To test whether a computer will infect a USB drive with malware we simply insert the USB drive into that computer, perform some file transfers(like moving a file from the computer to the pen drive and back), remove the USB, re-insert the USB and run the utility again. If any of our original files have been modified we know that the computer has a virus that infects USB's inserted into it


## Note:
This program is not meant to be used as a general-purpose antivirus as it can only tell you if your files have been modified since the last time you ran it.


## Options for using the program: 
The program is available as both a .py file and as a .exe. The only difference between these files is that the .py file requires Python to be installed on the user's computer and the .exe file already contains a frozen python interpreter and hence doesn't require Python to be installed on the user's computer. 

You can explore the contents and exact workings of the file by going through the .py file
