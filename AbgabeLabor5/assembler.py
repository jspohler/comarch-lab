import sys
from os.path import exists
from collections import deque

PATH_TO_CODE = "code_examples/"
addresses = {}
constants = {}
hex_file_name = "code_assembled_to_hex"
clean_code_lines = deque([])

def assemble(file_name):
    #first phase, parsing the assembler code
    try:
        instruction_location_counter = 1
        path_to_file = PATH_TO_CODE + file_name
        if exists(path_to_file):
            file = open(path_to_file, "r")
            for line in file:
                #clean line of comments
                line = line.replace("\n", "").replace("\r", "")
                line.strip()
                if line == "":
                    continue
                if ";" in line:
                    if line.index(";") == 0:
                        continue
                    else:
                        line = line[0:line.index(";")]
                #add line for later
                clean_code_lines.append(line.strip())
                #check if line contains address marker definition
                if ":" in line and "EQU" not in line:
                    line_parts = line.split(" ")
                    for part in line_parts:
                        if ":" in part:
                            part.strip()
                            marker = part.replace(":","")
                            #save marker with its address in a dict
                            addr = str(instruction_location_counter)
                            addr = str(hex(int(addr))[2:])
                            if len(addr) == 1:
                                addr = "0" + addr
                            addresses.update({marker : addr})
                #increase instruction location counter
                instruction_location_counter += get_info_for_mnemonic(line, True)
            file.close()

    except FileNotFoundError:
        print("File not found. Please provide the correct file name.")
    except IOError:
        print("An error occurred while reading the file. Please check syntax.")

    #second phase, assembling the hex code to be executable in the cpu
    result_file = open(hex_file_name, "w")
    result_file.write("v3.0 hex words addressed" + "\n")
    #the hex file has 16 lines of hex numbers
    hex_carry = ""
    for row in range(16):
        line_index_counter = 0
        line = str(hex(row)[2:])
        if len(line) == 1:
            line = line + "0" 
        line = line + ": "
        #add a nop as a starter in the first row
        if row == 0:
            line_index_counter = 1
            line = line + "00 "
        if len(hex_carry) != 0:
            line = line + hex_carry
            hex_carry = ""
        #if hex numbers per line is reached, new 
        while line_index_counter < 16:
            instruction = ""
            if len(clean_code_lines) > 0:
                instruction = clean_code_lines.popleft()
            if instruction != "" :
                if (line_index_counter + get_info_for_mnemonic(instruction, True)) < 17:
                    line = line + get_info_for_mnemonic(instruction, False)
                    line_index_counter += get_info_for_mnemonic(instruction, True)
                else:
                    parts = get_info_for_mnemonic(instruction, False).strip().split(" ")
                    line = line + parts[0]
                    for hex_part in parts[1:]:
                        hex_carry = hex_carry + hex_part + " "
                    line_index_counter += 1
            else:
                #fill rest with 00
                line = line + "00 "
                line_index_counter += 1

        #write line and add a new line
        result_file.write(line.strip() + "\n")



def get_info_for_mnemonic(mnemonic, get_length):
    mnemonic.strip()
    if ("NOP" in mnemonic):
        if get_length:
            return 1
        else:
            return "00 "
    elif ("INPUT" in mnemonic):
        if get_length:
            return 1
        else:
            return "02 "
    elif ("OUTPUT" in mnemonic):
        if get_length:
            return 1
        else:
            return "05 "
    elif ("JMP " in mnemonic):
        if get_length:
            return 2
        else:
            instruction_parts = mnemonic.split(" ")
            result = "08 " + addresses[instruction_parts[len(instruction_parts)-1]]+ " "
            return result
    elif ("LOAD A, #" in mnemonic):
        if get_length:
            return 2
        else:
            result = mnemonic[mnemonic.index("#") + 1:]
            result = str(hex(int(result))[2:])
            if len(result) == 1:
                result = "0" + result
            result = "0d " + result + " "
            return result
    elif ("LOAD A, " in mnemonic):
        if get_length:
            return 2
        else:
            instruction_parts = mnemonic.split(" ")
            result = "03 " + addresses[instruction_parts[len(instruction_parts)-1]] + " "
            return result
    elif ("INC A" in mnemonic):
        if get_length:
            return 1
        else:
            return "11 "
    elif ("MOV B," in mnemonic):
        if get_length:
            return 1
        else:
            return "14 "
    elif ("ADD A," in mnemonic):
        if get_length:
            return 1
        else:
            return "17 "
    elif ("HALT" in mnemonic):
        if get_length:
            return 1
        else:
            return "1a "
    elif ("SUB A," in mnemonic):
        if get_length:
            return 1
        else:
            return "18 "
    elif ("AND A," in mnemonic):
        if get_length:
            return 1
        else:
            return "15 "
    elif ("OR A," in mnemonic):
        if get_length:
            return 1
        else:
            return "16 "
    elif ("BEQ" in mnemonic):
        if get_length:
            return 2
        else:
            instruction_parts = mnemonic.split(" ")
            result = "1b " + addresses[instruction_parts[len(instruction_parts)-1]] + " "
            return result
    elif ("STORE A," in mnemonic):
        if get_length:
            return 2
        else:
            instruction_parts = mnemonic.split(" ")
            result = "12 " + addresses[instruction_parts[len(instruction_parts)-1]] + " "
            return result
    elif ("DB" in mnemonic):
        if get_length:
            return 1
        else:
            instruction_parts = mnemonic.split(" ")
            result = instruction_parts[len(instruction_parts)-1]
            result = str(hex(int(result))[2:])
            if len(result) == 1:
                result = "0" + result
            result = result + " "
            return result
    elif ("EQU" in mnemonic):
        if get_length:
            instruction_parts = mnemonic.split(" ")
            constants.update({instruction_parts[0].replace(":",""): instruction_parts[len(instruction_parts)-1]})
            return 0
        else:
            print("EQU not implemented yet")
    elif ("RESB" in mnemonic):
        if get_length:
            return int(mnemonic[mnemonic.index(" "):])
        else:
            print("RESB not implemented yet")
    else:
        raise Exception("invalid syntax in mnemonic:" + mnemonic)
    

if __name__=="__main__":
    assemble(str(sys.argv[1]))