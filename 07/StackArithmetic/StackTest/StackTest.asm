
//push constant 17
@17
D=A
@SP
M=M+1
A=M-1
M=D

//push constant 17
@17
D=A
@SP
M=M+1
A=M-1
M=D

//eq
@SP
A=M-1
D=M
A=A-1
D=M-D
@25
D,JEQ
@SP
A=M-1
A=A-1
M=0
@29
0,JMP
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1

//push constant 17
@17
D=A
@SP
M=M+1
A=M-1
M=D

//push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D

//eq
@SP
A=M-1
D=M
A=A-1
D=M-D
@56
D,JEQ
@SP
A=M-1
A=A-1
M=0
@60
0,JMP
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1

//push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D

//push constant 17
@17
D=A
@SP
M=M+1
A=M-1
M=D

//eq
@SP
A=M-1
D=M
A=A-1
D=M-D
@87
D,JEQ
@SP
A=M-1
A=A-1
M=0
@91
0,JMP
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1

//push constant 892
@892
D=A
@SP
M=M+1
A=M-1
M=D

//push constant 891
@891
D=A
@SP
M=M+1
A=M-1
M=D

//lt
@SP
A=M-1
D=M
A=A-1
D=M-D
@118
D,JLT
@SP
A=M-1
A=A-1
M=0
@122
0,JMP
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1

//push constant 891
@891
D=A
@SP
M=M+1
A=M-1
M=D

//push constant 892
@892
D=A
@SP
M=M+1
A=M-1
M=D

//lt
@SP
A=M-1
D=M
A=A-1
D=M-D
@149
D,JLT
@SP
A=M-1
A=A-1
M=0
@153
0,JMP
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1

//push constant 891
@891
D=A
@SP
M=M+1
A=M-1
M=D

//push constant 891
@891
D=A
@SP
M=M+1
A=M-1
M=D

//lt
@SP
A=M-1
D=M
A=A-1
D=M-D
@180
D,JLT
@SP
A=M-1
A=A-1
M=0
@184
0,JMP
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1

//push constant 32767
@32767
D=A
@SP
M=M+1
A=M-1
M=D

//push constant 32766
@32766
D=A
@SP
M=M+1
A=M-1
M=D

//gt
@SP
A=M-1
D=M
A=A-1
D=M-D
@211
D,JGT
@SP
A=M-1
A=A-1
M=0
@215
0,JMP
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1

//push constant 32766
@32766
D=A
@SP
M=M+1
A=M-1
M=D

//push constant 32767
@32767
D=A
@SP
M=M+1
A=M-1
M=D

//gt
@SP
A=M-1
D=M
A=A-1
D=M-D
@242
D,JGT
@SP
A=M-1
A=A-1
M=0
@246
0,JMP
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1

//push constant 32766
@32766
D=A
@SP
M=M+1
A=M-1
M=D

//push constant 32766
@32766
D=A
@SP
M=M+1
A=M-1
M=D

//gt
@SP
A=M-1
D=M
A=A-1
D=M-D
@273
D,JGT
@SP
A=M-1
A=A-1
M=0
@277
0,JMP
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1

//push constant 57
@57
D=A
@SP
M=M+1
A=M-1
M=D

//push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D

//push constant 53
@53
D=A
@SP
M=M+1
A=M-1
M=D

//add
@SP
A=M-1
D=M
A=A-1
M=M+D
@SP
M=M-1

//push constant 112
@112
D=A
@SP
M=M+1
A=M-1
M=D

//sub
@SP
A=M-1
D=M
A=A-1
M=M-D
@SP
M=M-1

//neg
@SP
A=M-1
M=-M

//and
@SP
A=M-1
D=M
A=A-1
M=M&D
@SP
M=M-1

//push constant 82
@82
D=A
@SP
M=M+1
A=M-1
M=D

//or
@SP
A=M-1
D=M
A=A-1
M=M|D
@SP
M=M-1

//not
@SP
A=M-1
M=!M
