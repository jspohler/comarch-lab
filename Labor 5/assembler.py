import sys
from os.path import exists

PATH_TO_CODE = "code_examples/"

def assemble(file_name):
    #first phase, parsing the assembler code
    try:
        path_to_file = PATH_TO_CODE + file_name
        if exists(path_to_file):
            file = open(path_to_file, "r")
            for line in file:
                #clean line of comments
                line.strip()
                if ";" in line:
                    if line.index(";") == 0:
                        continue
                    else:
                        line = line[0:line.index(";")]
                print(line)
            file.close()
    except FileNotFoundError:
        print("File not found. Please provide the correct file name.")
    except IOError:
        print("An error occurred while reading the file. Please check syntax.")

    #second phase, assembling the hex code to be executable in the cpu













if __name__=="__main__":
    assemble(str(sys.argv[1]))


def get_opcode_for_mnemonic(mnemonic):
    mnemonic.strip()
    if ("NOP" in mnemonic):
        return "00"
    elif ("INPUT" in mnemonic):
        return "02"
    elif ("OUTPUT" in mnemonic):
        return "05"
    elif ("JMP " in mnemonic):
        instruction_parts = mnemonic.split(" ")
        result = "08" + instruction_parts[1]
        return result
    elif ("LOAD A, #" in mnemonic):
        result = "0d" + mnemonic[mnemonic.index("#"):]
        return result
    elif ("LOAD A, " in mnemonic):
        return ""
    elif ("INC A" in mnemonic):
        return "11"
    elif ("MOV B," in mnemonic):
        return "14"
    elif ("ADD A," in mnemonic):
        return "17"
    elif ("HALT" in mnemonic):
        return "1a"
    elif ("SUB A," in mnemonic):
        return "18"
    elif ("AND A," in mnemonic):
        return "15"
    elif ("OR A," in mnemonic):
        return "16"
    elif ("BEQ" in mnemonic):
        instruction_parts = mnemonic.split(" ")
        result = "1b" + instruction_parts[1]
        return result
    elif ("STORE A," in mnemonic):
        instruction_parts = mnemonic.split(" ")
        result = "12" + instruction_parts[2]
        return result
    else:
        raise Exception("invalid syntax in mnemonic:" + mnemonic)