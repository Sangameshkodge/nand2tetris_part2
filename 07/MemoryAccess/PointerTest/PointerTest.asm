
//push constant 3030
@3030
D=A
@SP
M=M+1
A=M-1
M=D

//pop pointer 0
@SP
M=M-1
A=M
D=M
@THIS
M=D

//push constant 3040
@3040
D=A
@SP
M=M+1
A=M-1
M=D

//pop pointer 1
@SP
M=M-1
A=M
D=M
@THAT
M=D

//push constant 32
@32
D=A
@SP
M=M+1
A=M-1
M=D

//pop this 2
@2
D=A
@THIS
D=D+M
@SP
M=M-1
A=M+1
M=D
A=A-1
D=M
A=A+1
A=M
M=D

//push constant 46
@46
D=A
@SP
M=M+1
A=M-1
M=D

//pop that 6
@6
D=A
@THAT
D=D+M
@SP
M=M-1
A=M+1
M=D
A=A-1
D=M
A=A+1
A=M
M=D

//push pointer 0
@THIS
D=M
@SP
M=M+1
A=M-1
M=D

//push pointer 1
@THAT
D=M
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

//push this 2
@2
D=A
@THIS
A=D+M
D=M
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

//push that 6
@6
D=A
@THAT
A=D+M
D=M
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
