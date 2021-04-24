
# A single ReservationBank
class ReservationBank:
    def __init__(self, num):
        self.num = num       # the reservation bank number
        self.instruction_no = 0  # instruction currently being executed 
        self.tag1 = -1       
        self.source1 = 0
        self.tag2 = -1
        self.source2 = 0
        self.destination = 0
        self.finish_time = -1      
        self.is_occupied = False
        self.result = 0           # answer of computation
        self.is_executing = False
    def print_bank(self):
        return (" "+str(self.num)+"  |  "+str(self.instruction_no)+"  |   "+str(self.tag1)+"  |  "+str(self.source1)+"  |  "+str(self.tag2)+"  |  "+str(self.source2))


# A set of Reservation banks
class ReservationBanks:
    def __init__(self):
        self.FADD_available = 3
        self.FMUL_available = 2
        self.ADD_available = 3
        self.MUL_available = 2
        self.LD_available = 3
        self.ST_available = 3
        self.list = [ReservationBank(i) for i in range(17)]

    # def print_banks(self):
    #     for i in self.list:
    #         i.print_bank()
