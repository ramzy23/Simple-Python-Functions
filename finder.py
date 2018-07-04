#This module will serve as a simple search function that can return the requseted information for all projects.

def throw_error(number):
    if number == 0:
        print("ERROR 000")
        print("Invalid delimiter(s). One of the given delimiters do not exist in the given string")
    elif number == 1:
        print("ERROR 001")
        print("No more information can be found")

def exists_string(phrase,string):
    #This will check if a given phrase exists in a given string
    string = str(string)
    phrase = str(phrase)

    if string.find(phrase) == -1:
        return False

    return True

def exists_array(phrase,array):
    #This will check if a given phrase exists in a given array
    for i in array:
        if exists_string(phrase,i):
            return True
    return False

def find_string(begin,finish,string):
    #This will return a trimmed version of the string given within the selected information
    begin = str(begin)
    finish = str(finish)
    string = str(string)
    if string.find(begin) == -1 or string.find(finish) == -1:
        throw_error(0)
        return False
    text = string[string.find(begin) + len(begin):string.find(finish)]
    return text

def find_array(begin,finish,array):
    #This will return a trimmed version of the string given within the selected information from an array
    string_array = str(array)
    text = find_string(begin,finish,string_array)
    text = str(text)
    text = text[4:-4]
    return text

def more_exist(begin,finish,string):
    #This will see if more data can be collected from a string
    if string.find(begin) == -1 or string.find(finish) == -1:
        throw_error(1)
        return False
    return True

def find_all(begin,finish,string):
    #This will return an array of all the wanted strings from a string
    info = []
    string = str(string)
    begin = str(begin)
    finish = str(finish)
    while more_exist(begin,finish,string):
        text = string[string.find(begin) + len(begin):string.find(finish)]
        string = string[string.find(finish):]
        info.append(text)


if __name__ == "__throw_error()__":
	throw_error()

if __name__ == "__exists_string()__":
	exists_string()

if __name__ == "__exists_array()__":
	exists_array()

if __name__ == "__find_string()__":
	find_string()

if __name__ == "__find_array()__":
	find_array()

if __name__ == "__more_exist()__":
	more_exist()

if __name__ == "__find_all()__":
	find_all()
