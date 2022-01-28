#FILES TOPIC QA

# openedfile = open("README.md")  ##open file
# textstuff = openedfile.read()   ## for reading 
# openedfile.close()              ## close file

# uppertext = textstuff.upper()   ##uper case the file called textstuff
# print(uppertext)

# openedfile = open("README.md", "w") ## open file for writing
# openedfile.write(uppertext)         ## upper case file
# openedfile.close()                  ## close file (then press run to see if it worked)

# file = open("filesexample.txt", "r") ##read file

# outfile = ""

# for line in range(1, 10): # range 1-10
#     if line % 2 == 0:  ##if line is even
#         outfile += file.readline() #reads the current line and pushes it in outfile^(above)
#     else:
#         file.readline() #which reads the current line and then moves on to the next line.

# file = open("filesexample.txt", "w") ## once above completed ^ opens file for writing
# file.write(outfile)   ##edits and replaces file with outfile
# file.close()            ## closes file


#ex1a) Create a Python file which does the following:
# Opens a new text file called "teams.txt" and adds the names of 5 sports teams.
# Reads and displays the names of the 1st and 4th team in the file.

file = open("teamsfileexample.txt", "r")

outfile = ""

for line in range(0, 10): # range 5
    if line == 2 or line == 6:  ##if line is on index 2 or index 6
        outfile += file.readline() #reads the current line and pushes it in outfile^(above)
    else:
        file.readline() #which reads the current line and then moves on to the next line.

file = open("teamsfileexample.txt", "w") ## once above completed ^ opens file for writing
file.write(outfile)   ##edits and replaces file with outfile
file.close()            ## closes file
