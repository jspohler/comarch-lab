# COMARCH LAB

## Description
In my study program in the module computer architecture we had a lab assignment to build our own cpu, write its microcode, and also write an assembler to assemble the assembler code into machine code to execute it on the cpu. You can find the instruction how to assemble your written code for the cpu below. Documentation about the mnemonics and its meaning etc you can find in the two excel sheets in the repo.

## Usage
To translate an assembler code into hex code, you need to:

1. Place the file containing the assembler code in the 'code_examples' folder.
2. Open a terminal in the directory where the 'assembler.py' file is located.
3. Have Python 3 installed.
4. Then, in the terminal, execute the command `python3 assembler.py <yourFileNameWithExtension>`.
5. We recommend using the file `exampleFinal.txt` as a sample program; it utilizes all the instructions.
6. In the same folder, you will now find your assembled result in the file named `code_assembled_to_hex`.
7. The assembler assembles for our custom CPU, which differs from the one provided. The distinction to consider while writing assembler code is that our `BEQ` instruction performs its own subtraction. Therefore, the two numbers to be compared should be present in registers A and B beforehand. Consequently, it cannot be directly compared with other operations such as AND, OR, or ADD.
8. To execute the assembled code, open our CPU in Logisim Evolution and load the assembled code into the program memory.

## Authors and acknowledgment
Thanks to Professor Alexander Förster for his guidance through this very interesting module

## Project status
Submitted
