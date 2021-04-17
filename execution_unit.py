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
    # filename = 'fullAdder_tb.v'
    # print(get_sum(filename, a, b, cin))  # Simply call the verilog module like this and get the result of execution as a string
    # stream = os.popen('iverilog fullAdder_tb.v && ./a.out')
    # output = stream.readline().rstrip()
    # output_file = open("output_v", "w")
    # output_file.write(output)
    # print(output)
    print(execute(a, b, opname='FADD'))







if __name__=="__main__":
    main()