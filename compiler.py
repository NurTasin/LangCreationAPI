#!usr/bin/env python

##LangCreationAPI
##Copyright 2020 Nur Mahmud Ul Alam Tasin
##You can report bug at github.com/NurTasin/LangCreationAPI
##Happy Language Creation

#-------------compiler file----------
from configure import *
import os
import sys
if targetFile.startswith("__ARGV__"):
	try:
		targetFile=argv[int(targetFile.replace("__ARGV__", ""))]
	except IndexError:
		print(TagerFileNotGiven.replace("__COMPILER_ERROR__","runtime error"))
		sys.exit()
incArr=[]
for i in Includes.split('|'):
	try:
		incArr.append(open(os.path.join(Src,i),'r'))
	except FileNotFoundError:
		print(((IncludeNotFound.replace("__HEADER__", i)).replace("[__COMPILER_ERROR__]", "[runtime error]")).replace("__SRC__", Src))
		sys.exit()
target=open(targetFile,'r')
output=open(tempFile,'w+')
if StandAlone:
	for file in incArr:
		readData=file.readlines()
		output.write("".join(readData))
	output.write("\n\n")
	output.write("".join(target.readlines()))
if not StandAlone:
	for file in Includes.split('|'):
		output.write(Linker.replace("__HEADER__", os.path.join(Src,file)))
	output.write("\n\n")
	output.write("".join(target.readlines()))
output.close()
target.close()
for every in incArr:
	every.close()
if runAtEnd:
	for command_ in command.split('||&&'):
		os.system(((command_.replace("__TEMP__", tempFile)).replace("__TEMPDIR__",tempDir)).replace("__TEMPFILE__", tempFileName))
