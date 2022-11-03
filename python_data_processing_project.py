"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    if(len(line1) >= len(line2)):
        longer_line = line1 # Length of the longer of the two lists
        shorter_line = line2 # Length of the shorter of the two lists
        length1 = len(longer_line)
        length2 = len(shorter_line)
    else :
        longer_line = line2
        shorter_line = line1
        length1 = len(longer_line)
        length2 = len(shorter_line)

    if (longer_line == shorter_line):
        return IDENTICAL
    elif((longer_line > shorter_line) and (longer_line[:length2] == shorter_line[:length2]) ):
        return length2
    else:
        for char in range(len(longer_line)):
            if (longer_line[char] != shorter_line[char]):
                return char



#print(singleline_diff("Olawale","Olawan"))

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """

    if(len(line1) >= len(line2)):
        longer_line = line1 # Length of the longer of the two liness
        shorter_line = line2 # Length of the shorter of the two lists
        length1 = len(longer_line)
        length2 = len(shorter_line)
    else :
        longer_line = line2
        shorter_line = line1
        length1 = len(longer_line)
        length2 = len(shorter_line)

    if(("\n" in line1 or "\r" in line1) or ("\n" in line2 or "\r" in line2)  or idx > length2):
        return ""
    else:
        
        print(longer_line)
        for char in range(idx+1):
            if (char < idx):
                print("=",end="")
            else:
                print("^")
        print(shorter_line)

#singleline_diff_format("Olawale\n","Olawan",5)



def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.
      
      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    if(len(lines1) >= len(lines2)):
        longer_list = lines1
        shorter_list = lines2
        length1 = len(longer_list)
        length2 = len(shorter_list)
    else :
        longer_list = lines2 
        shorter_list = lines1
        length1 = len(longer_list) # Length of the longer of the two lists
        length2 = len(shorter_list) # Length of the shorter of the two list

    if (longer_list == shorter_list):
        return (IDENTICAL,IDENTICAL)
    elif((longer_list > shorter_list) and (longer_list[:length2] == shorter_list[:length2]) ):
        return (length2,0)
    else:
        for line in range(len(longer_list)):
            if (longer_list[line] != shorter_list[line]):
                char_index = singleline_diff(longer_list[line], shorter_list[line])
                return (line, char_index)


print(multiline_diff(["Olawale","Ridwan","Baseeroh","Shamsudeen",], ["Olawale","Ridwan","Baseeroh","Shamsudeen","Raheemah"]))


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or 
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    file_lines = []
    openfile = open(filename,"rt")

    
    #data = openfile.read()
    #print(data)
    #openfile.close
    for line in openfile.readlines():
        #new_line = line.rstrip()
        #file_lines.append(new_line)
        if("\n" in line and "\r" in line):
            new_line = line.replace("\n","")
            new_line = line.replace("\r","")
            file_lines.append(new_line)
        elif("\n" in line):
            new_line = line.replace("\n","")
            file_lines.append(new_line)
        elif("\r" in line):
            new_line = line.replace("\r","")
            file_lines.append(new_line)
        else: 
             file_lines.append(line)
             
    return file_lines
    openfile.close()

#print(get_file_lines(r"C:\Users\HP\Desktop\myPythonCodes\newsample.txt"))

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    file1_list = get_file_lines(filename1)
    file2_list = get_file_lines(filename2)

    tuple = multiline_diff(file1_list, file2_list)
    #The above line is a tuple showing the line and index where the difference occur
    if tuple == (IDENTICAL,IDENTICAL):
        return "No diffrences\n"
    else:
        print("Line " + str(tuple[0]))
        first_files_diff = singleline_diff_format(file1_list[tuple[0]], file2_list[tuple[0]], tuple[1])
        return first_files_diff
    
print(file_diff_format(r"C:\Users\HP\Desktop\myPythonCodes\newsample.txt", r"C:\Users\HP\Desktop\myPythonCodes\secondfile.txt"))