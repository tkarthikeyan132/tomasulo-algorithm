
import memory_unit
import reservation_bank
from dictionaries import (
    reservation_banks_range,
    cycles_required
)
from execution_unit import execute


time = 0
program_counter = 1

M = memory_unit.MainMemory()
Registers = memory_unit.Registers()
ReservationBanks = reservation_bank.ReservationBanks()

# sets the source1, source2 based upon status of FLR
def source_setter(bank, src1, src2):
    register1 = Registers.list[int(source1)]
    register2 = Registers.list[int(source2)]
    if(register1.busy):
        bank.tag1 = register1.tag
        register1.tag = bank.num
        bank.source1 = NULL
    else:
        bank.tag1 = 0
        bank.source1 = register1.data

    if(register2.busy):
        bank.tag2 = register2.tag
        register2.tag = bank.num
        bank.source2 = NULL
    else:
        bank.tag2 = 0
        bank.source2 = register2.data
        

# incomplete
def destination_setter(bank, destination):
    if(destination is not NULL):
        dest_register = Registers.list[int(destination[1:])]
        if(dest_register.busy):
            bank.tag1 = dest_register.tag
            dest_register.tag = bank.num
        else:
            dest_register.busy = True
            dest_register.tag = bank.num




# returns the [dest, src1, src2]
def split_instruction(instruction):
    opname = instruction[0]
    destination = NULL
    source1 = NULL
    source2 = NULL
    if (opname is 'LD' or opname is 'ST'):
        source1 = instruction[1][1:]
        source2 = instruction[2][1:]
    else:
        destination = instruction[1][1:]
        source1 = instruction[2][1:]
        source2 = instruction[3][1:]
    return destination, source1, source2

def fill_reservation_bank(reservation_bank, instruction, opname, n_bank):
    [destination, source1, source2] = split_instruction(instruction)
    reservation_bank.is_occupied = True
    setattr(ReservationBanks, opname + '_available', n_bank - 1) #decrement
    source_setter(reservation_bank, source1, source2)
    reservation_bank.instruction_no = program_counter
    reservation_bank.finish_time = time + cycles_required[opname]
    

# returns the empty reservation bank
def get_available_bank(opname):
    for i in range(reservation_banks_range[opname]):
        if(!(ReservationBanks.list[i].is_occupied)):
            return ReservationBanks.list[i] 

def main():
    instruction_file = open("Instructions.txt", "r")
    instructions_list = instruction_file.readlines()
    instructions = [line.rstrip().split(' ') for line in instructions_list]
    instructions.reverse()
    # print(instructions[3][3][1:])
    while(True):
        for _ in range(3):
            instruction = instructions.pop()
            opname = instruction[0]
            number_of_available_banks = getattr(ReservationBanks, opname + '_available') 
            if(number_of_available_banks > 0):
                current_bank = get_available_bank(opname)
                current_bank.instruction_no = program_counter
                fill_reservation_bank(current_bank, instruction, opname, number_of_available_banks)
                destination_setter(current_bank, destination)
                program_counter += 1
            else:
                instructions.append(instruction)
                break
        time += 1


    
    # Registers.print_registers()
    # ReservationBanks.print_banks()






if __name__=="__main__":
    main()