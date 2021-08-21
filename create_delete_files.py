import os
import sys
import json

command = sys.argv[1]
file_name = sys.argv[2]
count = sys.argv[3]
point_pos = file_name.find('.')
count = int(count)
count += 1
dirs = os.listdir(os.getcwd())

created_list = list()
remove_list = list()
exists_list = list()

# the function creates files in the current directory, the number of which does not exceed 'count'
# if there are these files in the current directory, then the function does not duplicate them, 
# but only adds the missing amount
def create_js_file(tmp):    
    for k in range(1, count):
        tmp = file_name[:point_pos] + f'{k}' + file_name[point_pos:]
        if  tmp not in dirs:
            new_js_file = os.path.join(os.getcwd(), tmp)
            fl = open(new_js_file, 'w')
            fl.close()
            created_list.append(tmp)
        else:
            exists_list.append(tmp)


# a function that removes files that enter the loop from zero to 'count'
# if the file is not in the current directory, then the function checks the next by number
def delete_js_file(tmp):
    for j in range(1, count):
        tmp = file_name[:point_pos] + f'{j}' + file_name[point_pos:]
        if tmp in dirs:
            old_js_file = os.path.join(os.getcwd(), tmp)
            remove_list.append(tmp)
            os.remove(old_js_file)
        else:
            exists_list.append(tmp)
            

if __name__ == '__main__':
    if command == 'create':
        create_js_file(file_name)
        created_list = json.dumps(created_list)
        exists_list = json.dumps(exists_list)
        jsoncreated = json.loads(created_list)
        jsonexists = json.loads(exists_list)
        print('The following files have been successfully ',
        'created in the current directory:\n {}'.format(jsoncreated))
        print('The following files exist in the current directory: \n{}'.format(jsonexists))
    elif command == 'delete':
        delete_js_file(file_name)
        deleted_list = json.dumps(remove_list)
        NOexists_list = json.dumps(exists_list)
        jsondeleted = json.loads(deleted_list)
        jsonNOexists = json.loads(NOexists_list)
        print('The following files have been successfully',
        'removed from the current directory:\n {}'.format(jsondeleted))
        print('The following files not exist in the current directory: \n{}'.format(jsonNOexists))
