#This module is used to make modules easier. It will add the necesarry lines of code that are needed to make it work well.
buffer = ["\n"]

def function_exists(file):
    #This will check if a function exists in a string passed in as file
    answer = file.find("def ")
    if answer != -1:
        return True
    return False


def file_data(file_path):
    #This opens the file and will read and save it. The saved file will be returned
    file = open(file_path,"r")
    read_file = []
    for i in file:
        read_file.append(i)
    file.close()
    return read_file

def add_to_buffer(function_name):
    #This will write to the global variable buffer for later use
    function = remove_parameters(function_name)
    line1 = "if __name__ == \"__" + function + "__\":"
    line2 = "\t" + function
    buffer.append(line1)
    buffer.append(line2)
    buffer.append("")

for i in buffer:
    print(i)
def get_function_name(function_line):
    #This will search for a function name and return it in a string. It will also add it to the buffer of functions to be written to the file.
    function_name = function_line[function_line.find("def ") + 4: function_line.find(":")]
    add_to_buffer(function_name)

def remove_parameters(function_name):
    #This removes a functions parameters
    end = function_name.find("(")
    function = function_name[:end + 1] + ")"
    return function

def interface(file_path):
    #This function sets up the buffer to write to the file
    data = file_data(file_path)
    for i in data:
        if function_exists(i):
            get_function_name(i)

def write(file_path):
    #This writes to the file_path given
    filet = file_data(file_path)

    new_file = open(file_path,"w")
    for i in filet:
        print(i,end ="",file = new_file)
    for i in buffer:
        print(i,file = new_file)
    new_file.close()

def write_to_file(file_path):
    #This will give a final chance to confirm weather or not a file should be changed.
    filet = file_data(file_path)
    for i in filet:
        print(i ,end = "")
    for i in buffer:
        print(i)

    print("The above is about to be written to the file " + file_path + ".")
    if input("Do you agree? y/n: ") == "y":
        write(file_path)
    else:
        exit()

print("Welcome to the module maker. Please note that this file needs to be in the same directory as the module you need to verify.")
path = input("Please enter the name of the file + extension: ")
interface(path)
write_to_file(path)

print("Done!\nIf you feel you have made a mistake, tough luck. We will make the undo-er soon. We will also add more functionability soon.")
