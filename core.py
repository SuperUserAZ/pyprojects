if __name__ == '__main__':
    N = int(input())
    input_list = list()
    command_list = list()
    command, params = list(), list()

    for i in range(N):
        obj = list(input().split(' '))
        com = obj[0]
        result1 = [int(ob) for ob in obj[1:]]
        params.append(result1)
        command.append(com)
        result2 = tuple(zip(command, params))

    command_list.extend(result2)

    for _, command in enumerate(command_list):
        com1 = command[0]
        com2 = None
        if command[1]:
            com2 = command[1][0]
        if com1 == 'insert':
            input_list.insert(com2, command[1][1])
        elif com1 == 'append':
            input_list.append(com2)
        elif com1 == 'remove':
            if com2 in input_list:
                input_list.remove(com2)
        elif com1 == 'pop':
            if input_list:
                input_list.pop()
        elif com1 == 'sort':
            input_list.sort()
        elif com1 == 'reverse':
            input_list = reversed(input_list)
        elif com1 == 'print':
            print(input_list)
        

