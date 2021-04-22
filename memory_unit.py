# The main memory
class MainMemory:
    def __init__(self):
        self.list = ["0"] * 1024
    
    def print_memory(self):
        print(self.list)
    
    # address and value are integers
    def write_memory(self, address, value):
        self.list[address] = str(value)

    # address is integer
    def read_memory(self, address):
        return self.list[address]
    

# A single Register
class Register:
    def __init__(self, num):
        self.num = num
        self.data = "0" * 32
        self.busy = False
        self.tag = 0
    

# A set of registers
class Registers:
    def __init__(self):
        self.list = [Register(i) for i in range(16)]

    def print_registers(self):
        for i in self.list:
            print(i.num, i.data, i.busy, i.tag)

    def write_register(self, idx, value):
        self.list[idx] = str(value)

    # address is integer
    def read_register(self, idx):
        return self.list[idx]