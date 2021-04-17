# 
import os
import preparator

# returns the output after execution
def execute(a, b, opname):
    filename = 'testbench.v'
    preparator.prepare_file(filename, a, b, opname=opname)
    stream = os.popen('iverilog ' + filename + ' && ./a.out')
    output = stream.readline().rstrip()
    return output


def main():
    a = '01000100100110100000101011111010'
    b = '01000111101110110110011000010001'
    cin = 0
    print(execute(a, b, opname='FADD'))

if __name__=="__main__":
    main()