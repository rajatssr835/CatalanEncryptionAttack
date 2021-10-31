# Python 3 program to convert 
# string into binary string 
import binascii
import random
# utility function 
def strToBinary(s): 
    bin_conv = [] 
  
    for c in s: 
          
        # convert each char to 
        # ASCII value 
        ascii_val = ord(c) 
          
        # Convert ASCII value to binary 
        binary_val = bin(ascii_val) 
        bin_conv.append(str(binary_val[2:]).zfill(8)) 
         
    return (''.join(bin_conv)) 

# Function to create the
# random binary string
def rand_key(p):
    
    # Variable to store the 
    # string
    key1 = ""
  
    # Loop to find the string
    # of desired length
    for i in range(p):
          
        # randint function to generate
        # 0, 1 randomly and converting 
        # the result into str
        temp = str(random.randint(0, 1))
  
        # Concatenatin the random 0, 1
        # to the final result
        key1 += temp
          
    return(key1)
  
# Driver Code 
if __name__ == '__main__': 
    #string = ['EN', 'CR', 'YP', 'TI', 'ON']
    string = ['FU', 'LL','AT', 'TA', 'CK','ON','CA', 'TA','LA','NK','EY','EN', 'CR', 'YP', 'TI', 'ON']
    #string = ['AT', 'TA', 'CK']
    #string = ['ON']
    #string = ['CA', 'TA','LA','NK']
    #string = ['EY']
#rule= [3,4,0,0,8,10,11,0,13,0,0,15,0,16,0,0]
rule= [4,3,0,0,16,15,8,0,10,0,0,11,0,13,0,0]
i=0
#for c in range(0,15):
# print("i"+str(c)+",",end="")
#print("i15,",end="")
#for c in range(0,15):
# print("o"+str(c)+",",end="")
#print("o15")
for counter in range(0,1000):
 randchar1=chr(random.randint(ord('A'), ord('Z')))
 randchar2=chr(random.randint(ord('A'), ord('Z')))
 stob=strToBinary('AB')  
 stob2=strToBinary('CD') 
 n = 16
 str1 = rand_key(n)
 stob=str1  
 randchar1=chr(random.randint(ord('A'), ord('Z')))
 randchar2=chr(random.randint(ord('A'), ord('Z')))
 stob2=strToBinary(str(randchar1)+str(randchar2)) 
 liststob=list(stob)
 jindex=0
 for j in rule:
  #print(str(listreverse[13])+","+str(listreverse[15]))
  if (j != 0):
   #print (str(jindex)+","+str(j-1)+","+str(listreverse[jindex])+","+str(listreverse[j-1]))
   a=liststob[jindex]
   b=liststob[j-1]
   liststob[jindex]=b
   liststob[j-1]=a
   jindex=jindex+1
  else:
   jindex=jindex+1
   continue
 #print(str(stob)+","+str(''.join(liststob)))
 jindex=0
 liststob2=list(stob2)
 for j in rule:
  #print(str(listreverse[13])+","+str(listreverse[15]))
  if (j != 0):
   #print (str(jindex)+","+str(j-1)+","+str(listreverse[jindex])+","+str(listreverse[j-1]))
   a=liststob2[jindex]
   b=liststob2[j-1]
   liststob2[jindex]=b
   liststob2[j-1]=a
   jindex=jindex+1
  else:
   jindex=jindex+1
   continue
 
 i=i+1
 outputdiff= str(bin(int(str(''.join(liststob2)),2) ^ int(str(''.join(liststob)),2)))[2:].zfill(16)
 inputdiff= str(bin(int(stob2,2) ^ int(stob,2)))[2:].zfill(16)
 #print(str(stob)+","+str(stob2)+","+str(''.join(liststob))+","+str(''.join(liststob2))+","+str(inputdiff)+","+str(outputdiff))
 #print(",".join(inputdiff)+":"+",".join(outputdiff))
 print(",".join(stob)+","+",".join(liststob))
  
# This code is contributed  
# by Vikas Chitturi 
