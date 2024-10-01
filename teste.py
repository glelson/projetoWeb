import os, sys
import time

path = r"\\10.0.2.52\ti"
dirs = os.listdir( path )
lista = []
for file in dirs:
   lista.append(file)


data = time.strftime('%Y/%m/%d')
print(data)