#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 16:06:49 2020

@author: skodge
"""

import argparse
parser = argparse.ArgumentParser(description='VM translator', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--file',           default='./MemoryAccess/StaticTest/StaticTest.vm',  type=str,     help='File name to be translated')

global args
args = parser.parse_args()

args.linecount=-1

## Open File
F=open(args.file,'r')
## Load all the files 
vm_code=F.readlines()

static=args.file.strip().split("/")[-1].strip().split(".")[0].strip()

def push (segment, index):
    if (segment=='constant'):
        print ("@"+index)
        print("D=A")
        print ("@SP")
        print("M=M+1")
        print("A=M-1")
        print("M=D")
        args.linecount=args.linecount+6 
    elif (segment=='static'):
        print("@"+static+"."+index)
        print("D=M")
        print ("@SP")
        print("M=M+1")
        print("A=M-1")
        print("M=D")
        args.linecount=args.linecount+6
    elif (segment=='temp'):
        print("@"+str(int(index)+5))
        print("D=M")
        print ("@SP")
        print("M=M+1")
        print("A=M-1")
        print("M=D")
        args.linecount=args.linecount+6
    elif (segment=='local'):
        print("@"+index)
        print("D=A")
        print("@LCL")
        print("A=D+M")
        print("D=M")
        print ("@SP")
        print("M=M+1")
        print("A=M-1")
        print("M=D")
        args.linecount=args.linecount+9
    elif (segment=='argument'):
        print("@"+index)
        print("D=A")
        print("@ARG")
        print("A=D+M")
        print("D=M")
        print ("@SP")
        print("M=M+1")
        print("A=M-1")
        print("M=D")
        args.linecount=args.linecount+9
    elif (segment=='this'):
        print("@"+index)
        print("D=A")
        print("@THIS")
        print("A=D+M")
        print("D=M")
        print ("@SP")
        print("M=M+1")
        print("A=M-1")
        print("M=D")
        args.linecount=args.linecount+9
    elif (segment=='that'):
        print("@"+index)
        print("D=A")
        print("@THAT")
        print("A=D+M")
        print("D=M")
        print ("@SP")
        print("M=M+1")
        print("A=M-1")
        print("M=D")
        args.linecount=args.linecount+9
    elif (segment=="pointer"):
        if(int(index)==0):        
            print("@THIS")
        elif(int(index)==1):
            print("@THAT")
        else:
            raise ValueError
        print("D=M")
        print ("@SP")
        print("M=M+1")
        print("A=M-1")
        print("M=D")
        args.linecount=args.linecount+6
    else:
        raise ValueError
        
    
    return

def pop (segment, index):
    if (segment=='static'):
        print ("@SP")
        print("M=M-1")
        print("A=M")
        print("D=M")
        print("@"+static+"."+index)
        print("M=D")        
        args.linecount=args.linecount+6 
    elif (segment=='temp'):
        print ("@SP")
        print("M=M-1")
        print("A=M")
        print("D=M")
        print("@"+str(int(index)+5))
        print("M=D")
        args.linecount=args.linecount+6
    elif (segment=='local'):
        print("@"+index)
        print("D=A")
        print("@LCL")
        print("D=D+M")
        print("@SP")
        print("M=M-1")
        print("A=M+1")
        print("M=D")
        print("A=A-1")
        print("D=M")
        print("A=A+1")
        print("A=M")
        print("M=D")
        args.linecount=args.linecount+12
    elif (segment=='argument'):
        print("@"+index)
        print("D=A")
        print("@ARG")
        print("D=D+M")
        print("@SP")
        print("M=M-1")
        print("A=M+1")
        print("M=D")
        print("A=A-1")
        print("D=M")
        print("A=A+1")
        print("A=M")
        print("M=D")
        args.linecount=args.linecount+12
    elif (segment=='this'):
        print("@"+index)
        print("D=A")
        print("@THIS")
        print("D=D+M")
        print("@SP")
        print("M=M-1")
        print("A=M+1")
        print("M=D")
        print("A=A-1")
        print("D=M")
        print("A=A+1")
        print("A=M")
        print("M=D")
        args.linecount=args.linecount+12
    elif (segment=='that'):
        print("@"+index)
        print("D=A")
        print("@THAT")
        print("D=D+M")
        print("@SP")
        print("M=M-1")
        print("A=M+1")
        print("M=D")
        print("A=A-1")
        print("D=M")
        print("A=A+1")
        print("A=M")
        print("M=D")
        args.linecount=args.linecount+12
    elif (segment=="pointer"):
        print ("@SP")
        print("M=M-1")
        print("A=M")
        print("D=M")
        if(int(index)==0):        
            print("@THIS")
        elif(int(index)==1):
            print("@THAT")
        else:
            raise ValueError
        print("M=D")
        args.linecount=args.linecount+6
        
    elif (segment=="constant"):
        pass
    else:
        raise ValueError
        
    return


def arithmetic(operation):
    print ("@SP")
    print ("A=M-1")
    args.linecount= args.linecount+2
    if (operation == 'neg'):
        print ("M=-M")
        args.linecount= args.linecount+1
    elif (operation == 'not'):
        print ("M=!M")
        args.linecount= args.linecount+1
    else:
        print("D=M")
        print("A=A-1")
        args.linecount= args.linecount+2
        if (operation =='add'):
            print("M=M+D")
            args.linecount= args.linecount+1
        elif(operation == 'sub'):
            print("M=M-D")
            args.linecount= args.linecount+1
        elif(operation == 'and'):
            print("M=M&D")
            args.linecount= args.linecount+1
        elif(operation == 'or'):
            print("M=M|D")
            args.linecount= args.linecount+1
            
        elif(operation == 'eq'):
            print("D=M-D")
            print("@"+str(args.linecount+10))
            print("D,JEQ")
            print("@SP")
            print("A=M-1")
            print("A=A-1")
            print("M=0")
            print("@"+str(args.linecount+14))
            print("0,JMP")
            print("@SP")
            print("A=M-1")
            print("A=A-1")
            print("M=-1")
            args.linecount= args.linecount+13
            
            
        elif(operation == 'lt'):
            print("D=M-D")
            print("@"+str(args.linecount+10))
            print("D,JLT")
            print("@SP")
            print("A=M-1")
            print("A=A-1")
            print("M=0")
            print("@"+str(args.linecount+14))
            print("0,JMP")
            print("@SP")
            print("A=M-1")
            print("A=A-1")
            print("M=-1")
            args.linecount= args.linecount+13
            
        elif(operation == 'gt'):
            print("D=M-D")
            print("@"+str(args.linecount+10))
            print("D,JGT")
            print("@SP")
            print("A=M-1")
            print("A=A-1")
            print("M=0")
            print("@"+str(args.linecount+14))
            print("0,JMP")
            print("@SP")
            print("A=M-1")
            print("A=A-1")
            print("M=-1")
            args.linecount= args.linecount+13
        else:
            raise ValueError
        print ("@SP")
        print ("M=M-1")
        args.linecount= args.linecount+2
        #print("//linecount:"+str(args.linecount))
    return
        
        
for line in vm_code:
    line = line.strip()
    line = line.split('//')[0].strip()
    if line == "":
        continue
    else:
        print ('\n//'+line)
        line = line.split(' ')
        if (line[0].strip()=='push'):
            push(segment=line[1].strip(), index= line[2].strip())
        elif (line[0].strip()=='pop'):
            pop(segment=line[1].strip(), index= line[2].strip())
        else:
            arithmetic(operation=line[0].strip())
        
                
        