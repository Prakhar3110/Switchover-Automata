# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 13:30:13 2018

@author: basut
"""
import os.path
from pathlib import Path

filew = open("for_.txt","w");

r = {15}

for n in r:
    for i in range(0,n):
        for j in range(0,n):
            filer="cernychange"+str(n)+"_"+str(i)+"_"+str(j)+".txt" + "_SyncWord" + ".out";
            if os.path.exists(filer): 
                filew.write(str(n)+"_"+str(i)+"_"+str(j) + " Sync\n");
            else : 
                filew.write(str(n)+"_"+str(i)+"_"+str(j)+ " NotSync\n");
filew.close();