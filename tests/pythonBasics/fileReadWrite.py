#open the file using the open() function
file=open("E:\\Python_Projects\\Python_Playwright_Learnings\\tests\\pythonBasics\\textFile.txt")
#print the contents of the file using the read() method
print(file.read())
# we can also use the readLine() method to read the file line by line.
#if we use the readLine() method, it will return the first line of the file and move the cursor to the next line.
# we need to use any loop to read the file line by line until the end of the file is reached.
line = file.readline() #read the first line of the file
while line!="": #check if the line is not empty
    print(line) #print the line
    line = file.readline() #read the next line of the file

#Using readLines() method to read the file line by line and store it in a list.
for line in file.readlines(): #read the file line by line and store it in a list
    print(line) #print the line
file.close() #close the file after reading it

#There is another way to open the file using with statement, which will automatically close the file after reading it.
# Also im going to perform reverese of the filecontents and write it to same file using write() method.
# the advantage of using with statement is that we can mention we are using read mode or write mode, and it will automatically close the file after reading or writing it.
with open("E:\\Python_Projects\\Python_Playwright_Learnings\\tests\\pythonBasics\\textFile.txt", "r") as reader:
    file_contents = reader.readlines() #read the file line by line and store it in a list
    reversed_contents = file_contents[::-1] #reverse the list
    with open("E:\\Python_Projects\\Python_Playwright_Learnings\\tests\\pythonBasics\\textFile.txt", "w") as writer:
        for line in reversed(file_contents): #iterate through the reversed list
            writer.write(line) #write each line to the file
        #writer.writelines(reversed_contents) #write the reversed contents to the file