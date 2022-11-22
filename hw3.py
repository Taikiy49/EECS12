def main():
#imports operating sytem
    import os

#user inputs the file name
    fileName = input("What file are the numbers in? ")
    if os.path.isfile(fileName):
        print()
#if user inputs an invalid input file, reruns program
    else:
        print("Cannot find the input file")
        main()
#opens the file and reads
    file = open(fileName, 'r')
#counts the total number of lines in the file
    with open(fileName, 'r') as taiki:
        lines = sum(1 for line in taiki)
#sets the output file name and opens the output file to write
    x = str(fileName)
    outputfilename = x.split(".")
    outputfilename = str(outputfilename[0:-1])
    output = (outputfilename) + "-out.txt"
    output = output.replace("['","")
    output = output.replace("']","")
  
    outputfile = open(output, 'w')
#for loop to split each line by semi-colons
    for i in range(0,lines):
        l = file.readline()
        l = l.split(" ; ")
#for loop inside the for loop to convert major to numbers
        for i in range(1,len(l)):
            if l[i] == "Civil Engineering" or l[i] == "Civil Engineering\n":
                l[i] = "1"
            elif l[i] == "Computer Engineering" or l[i] == "Computer Engineering\n":
                l[i] = "2"
            elif l[i] == "Electrical Engineering" or l[i] == "Electrical Engineering\n":
                l[i] = "3"
            elif l[i] == "Mechanical Engineering" or l[i] == "Mechanical Engineering\n":
                l[i] = "4"
            else:
                l[i] = "0"
#joins elements with one space
        nameline = " ".join(l)
#writes all names and major numbers into output file
        outputfile.write(nameline)
        outputfile.write("\n")

#opening output with append
    outputfile = open(output, 'a')

#opening file and reading to count recurrence of majors
    file = open(fileName, 'r')
    text = file.read()
    civ = text.count("Civil Engineering")
    civ = str(civ)
    com = text.count('Computer Engineering')
    com = str(com)
    ele = text.count('Electrical Engineering')
    ele = str(ele)
    mec = text.count('Mechanical Engineering')
    mec = str(mec)
#writing the number of students in each major in output file
    outputfile.write("The number of Civil Engineering students: ")
    outputfile.write(str(civ))
    outputfile.write("\n")
    
    outputfile.write("The number of Computer Engineering students: ")
    outputfile.write(str(civ))
    outputfile.write("\n")
    
    outputfile.write("The number of Electrical Engineering students: ")
    outputfile.write(str(ele))
    outputfile.write("\n")

    
    outputfile.write("The number of Mechanical Engineering students: ")
    outputfile.write(str(mec))
    
#running main function
main()
