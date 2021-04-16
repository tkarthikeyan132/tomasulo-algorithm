
def fp_exec_input(a, b, cin, fpname):
    input_file = open(filename, "r")
    input_data = input_file.readlines()
    input_data[8] = "fpa F_0 (a, b, sum);\n"
    if(fpname == 'fpm'):
        input_data[8] = "fpm F_0 (a, b, sum);\n"
    input_data[12] = "	a = 1'b" + str(a) + ";\n"
    input_data[13] = "	b = 1'b" + str(b) + ";\n"
    input_data[14] = "//" + input_data[14]
    input_file = open(filename, "w")
    input_file.writelines(input_data)

def exec_input(a, b, cin, opname):
    input_file = open(filename, "r")
    input_data = input_file.readlines()
    # input_data[8] = "fpa F_0 (a, b, sum);\n"
    # if(fpname == 'fpm'):
    #     input_data[8] = "fpm F_0 (a, b, sum);\n"
    # input_data[12] = "	a = 1'b" + str(a) + ";\n"
    # input_data[13] = "	b = 1'b" + str(b) + ";\n"
    # input_data[14] = "//" + input_data[14]
    input_file = open(filename, "w")
    input_file.writelines(input_data)