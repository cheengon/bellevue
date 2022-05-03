#This program creates a file and gathers inputs (name, address, phone number) from a user. 
#The program will then write these inputs to a file and print the results.

#Step 1: import required modules
import os
import readline #tab completion capability

#Step 2: Print welcome message
print ("This program will create a comma separated line with your inputs and print the results. \n")

#Step 3: Perform validation that directory used to save file exists. 
readline.parse_and_bind("tab: complete")
readline.set_completer_delims('\t')
while True:
    dirPath = input("Enter the full path of the directory where you want your file saved: \n")
    if not os.path.isdir(dirPath):
        print("The directory path does not exist. Please enter a valid path.")
        continue
    else:
        break

#Step 4: Gather user inputs
fileName = input("Please name the new file?\n")
filePath = os.path.join(dirPath, fileName)
inputName = input("Please enter your full name:\n")
inputAddress = input("Please enter your address:\n")
inputNumber = input("Please enter your phone number:\n")

#Step 5: File processing (open, write, save and print)
try:    
    with open(filePath, 'w') as fileCreate: 
        data = (inputName + ", " + inputAddress + ", " + inputNumber)
        fileCreate.write(data)
except:
    print("Error creating/writing to new file.")
    quit()
try:
    with open(filePath) as fileCreate:
        print("A file named, " + fileName + ", was created. Please verify your information is correct.")
        print(fileCreate.read())
except:
    print("Error reading file.")
    quit()

