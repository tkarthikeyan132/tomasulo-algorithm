from formatters import decimal_to_binary
# The main memory
class MainMemory:
    def __init__(self):
        self.list = ["0"] * 1024
    
    def print_memory(self, range_n):
        print("*******************************************************************************************************")
        print(f"************************************Memory (display upto address {range_n})******************************")
        print("*******************************************************************************************************")
        i = 0
        while (i < range_n):
            print(f"Memory[{i}] = {decimal_to_binary(int(self.list[i]))} |$| Memory[{i+1}] = {decimal_to_binary(int(self.list[i+1]))}")
            i += 2      
    # address and value are integers
    def write_memory(self, address, value):
        self.list[int(address)] = str(value)

    # address is integer
    def read_memory(self, address):
        return self.list[int(address)]
    

# A single Register
class Register:
    def __init__(self, num):
        self.num = num
        self.data = "0"
        self.busy = False
        self.tag = 0
    def print_reg(self):
        return ("|   "+str(self.num)+"  |  "+str(self.tag)+"  |  "+str(self.busy)+"  |  "+str(self.data)+" ")

# A set of registers
class Registers:
    def __init__(self):
        self.list = [Register(i) for i in range(16)]

    def print_registers(self):
        print("***************Registers**********************")
        for i in self.list:
            i.print_reg()
            # print(i.num, i.data, i.busy, i.tag)
        print("**********************************************")

    def write_register(self, idx, value):
        self.list[idx] = str(value)

    # address is integer
    def read_register(self, idx):
        return self.list[idx]