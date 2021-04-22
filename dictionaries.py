
reservation_banks_range = {
    "FADD": (1,4),
    "FMUL": (4,6),
    "ADD" : (6,9),
    "MUL" : (9,11),
    "LD" : (11,14),
    "ST" : (14,17)
}

cycles_required = {
    "FADD": 10,
    "FMUL": 20,
    "ADD" : 7,
    "MUL" : 11,
    "LD" :  1,
    "ST" : 1
}


num_to_opcode = [
    "Invalid",
    "FADD",
    "FADD",
    "FADD",
    "FMUL",
    "FMUL",
    "ADD",
    "ADD",
    "ADD",
    "MUL",
    "MUL",
    "LD",
    "LD",
    "LD",
    "ST",
    "ST",
    "ST"
]