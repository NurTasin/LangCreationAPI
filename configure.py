##LangCreationAPI
##Copyright 2020 Nur Mahmud Ul Alam Tasin
##You can report bug at github.com/NurTasin/LangCreationAPI
##Happy Language Creation

##----------configure file--------------
from sys import argv , exit
from os import path , mkdir
runAtEnd=True
##Errors
TagerFileNotGiven="[__COMPILER_ERROR__] plaese give a target file to execute"
IncludeNotFound="[__COMPILER_ERROR__] __HEADER__ not found in __SRC__"
#Put True if you want a single file that conatains all of your 
#LangSrc Headers
#False means you will get a file that need to be linked properly with the LangScr
StandAlone=True
#This is the folder in wich the include files will be placed
Src="/home/tasin/scratchBox/LangCreateAPI/LangSrc"
#put the files to include in the program automatically
#To add multiple files separate them using '|'
#You have to put them inside the LangSrc folder
Includes="hardLang.h"
#The command to include them into file
#put __HEADER__ where the name of headers will be put
Linker="#include \"__HEADER__\""
#The target file which will be compiled
#put __ARGV__N Here (N means the position of argument) if you want to take the first command line arg as the target file
targetFile="__ARGV__1"
#The temporary directory where the tempoeary files will be placed.
#plaese use relative directory here
tempDir="/home/tasin/scratchBox/LangCreateAPI/temp"
#put the name of the temporary files name
tempFileName="temp.cpp"
tempFile=path.join(tempDir,tempFileName)
try:
	mkdir(tempDir)
except:
	pass
#The command by which the temporary file will be executed.
#put __TEMP__ where you want to put the temporary file.
#if there are multiple commands separate them using ||&&
command="g++ -std=c++11  -c __TEMP__ -o __TEMP__.o||&&g++  -o __TEMP__.out __TEMP__.o||&&cd __TEMPDIR__ &&./__TEMPFILE__.out"
