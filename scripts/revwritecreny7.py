# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 00:39:56 2018

@author: basut
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 00:25:39 2018

@author: basut
"""

a = 2;

for n in range(2,14):
  for i in range(0,n-1):
      for j in range(0,n):
        file = open("cernychange"+str(n)+"_"+str(i)+"_"+str(j)+".txt","w");
        file.write(str(a)+" "+str(n)+" ");
        for k in range(0,n-1):
          if k == i : 
            file.write(str((k+1)%n)+" "+str(j)+" ");
          else :
            file.write(str((k+1)%n)+" "+str(k)+" ");
        file.write(str(0)+" "+str(0));
        file.close();
  i=n-1;
  for j in range(0,n):
    file = open("cernychange"+str(n)+"_"+str(i)+"_"+str(j)+".txt","w");
    file.write(str(a)+" "+str(n)+" ");
    for k in range(0,n):
      if k == i : 
        file.write(str((k+1)%n)+" "+str(j)+" ");
      else :
        file.write(str((k+1)%n)+" "+str(k)+" ");
		#file.write(str(0)+" "+str(0))
    file.close();