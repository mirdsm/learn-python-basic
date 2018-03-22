

def insert(a,b):
    #b = str(b)
    list.insert(a,b)
    return list

def printing():
    print list
    return list

def remove(a):
    del list[0]
    return list

def append(a):
    #a = str(a)
    list.append(a)
    return list

def sort():
    list.sort()
    return list

def pop():
    list.pop(-1)
    return list

def reverse():
    list.reverse()
    return list


def controller_path(command):
    if command == "insert":
        return insert(a,b)
    elif command == "print":
        return printing()
    elif command == "remove":
        return remove(a)
    elif command == 'append':
        return append(a)
    elif command == 'sort':
        return sort()
    elif command == 'reverse':
        return reverse()
    elif command == 'pop':
        return pop()
    else:
        print "Missmatch type!"
        return None



list = []
how_much_action = int(raw_input("How much action do you need?\n"))

for i in range(0, how_much_action):
    list_split = []
    i_command = raw_input()
    i_command = [word for line in i_command for word in i_command.split()]
    #insert_command=" ".join(insert_command).split()
    #insert_command = [word for line in insert_command for word in line.split()]
    command = i_command[0]
    a=i_command[1]
    if a == command:
        a = 0
    else:
        a= int(a)
    #a = [map(int, x) for x in a1]
    b = i_command[2]
    if b == command:
        b = 0
    else:
        b = int(b)
    #b = [map(int, x) for x in b1]
    controller_path(command)
