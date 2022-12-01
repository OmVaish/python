import os.path
import sys
def main():
    # Prompt the user to enter filenames
    f1 = input("Enter a source file: ").strip()
    f2 = input("Enter a target file: ").strip()

    # Check if target file exists
    if not(os.path.isfile(f1)):
        print(f1+" does not exist")
        sys.exit()
    # Open files for input and output
    infile = open(f1, "r")
    outfile = open(f2, "w")

    # Copy from input file to output file
    i=0
    for line in infile:
        if i%2==0 :
            outfile.write(line)
        i+=1    
    infile.close() # Close the input file
    outfile.close() # Close the output file

main() # Call the main function
