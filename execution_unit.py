# 
import os


# prepares the test bench file to execute (Now we have to do this all 4 operations)
def prepare_input_file(filename, a, b, cin):
    input_file = open(filename, "r")
    input_data = input_file.readlines()
    input_data[12] = "	a = 1'b" + str(a) + ";\n"
    input_data[13] = "	b = 1'b" + str(b) + ";\n"
    input_data[14] = "	cin = 1'b" + str(cin) + ";\n"
    # print(input_data)
    input_file = open(filename, "w")
    input_file.writelines(input_data)


# returns the sum after execution
def get_sum(filename, a, b, cin):
    prepare_input_file(filename, a, b, cin)
    stream = os.popen('iverilog ' + filename + ' && ./a.out')
    output = stream.readline().rstrip()
    return output


def main():
    a = 1
    b = 0
    cin = 0
    filename = 'fullAdder_tb.v'
    print(get_sum(filename, a, b, cin))  # Simply call the verilog module like this and get the result of execution as a string
    # stream = os.popen('iverilog fullAdder_tb.v && ./a.out')
    # output = stream.readline().rstrip()
    # output_file = open("output_v", "w")
    # output_file.write(output)
    # print(output)






if __name__=="__main__":
    main()