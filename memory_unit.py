# The main memory
class MainMemory:
    def __init__(self):
        self.list = ["0"] * 1024
    
    def print_memory(self):
        print(self.list)
    
    # address and value are integers
    def write_memory(address, value):
        self.list[address] = str(value)

    # address is integer
    def read_memory(address):
        return self.list[address]
    

# A single Register
class Register:
    def __init__(self):
        self.data = "0" * 32
        self.busy = False
        self.tag = 0
    

# A set of registers
class Registers:
    def __init__(self):
        self.list = [Register() for i in range(16)]

    def print_registers(self):
        for i in self.list:
            print(i.data, i.busy, i.tag)

    def write_register(idx, value):
        self.list[idx] = str(value)

    # address is integer
    def read_register(idx):
        return self.list[idx]