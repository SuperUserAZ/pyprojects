import os
import json
import argparse 

parse = argparse.ArgumentParser()
parse.add_argument('-fo', '--folder', type=str, help = 'creates a new folder or navigates to that folder')
parse.add_argument('-f', '--file', type=str, help='the name of the instance of the file or files')
parse.add_argument('-df', '--delfolder', type=str, help='deletes folder')
parse.add_argument('-cr', '--create',type = bool, help='creates a file')
parse.add_argument('-d', '--delete', type= bool, help='deletes the file')
parse.add_argument('-co', '--count', type = int, help='indicates the number of instances')
args = parse.parse_args()

folder_name = args.folder
del_folder_name = args.delfolder
file_name = args.file
count = args.count
point_pos = file_name.find('.') if file_name else None
count = (count +1) if count else None

path_dir = f'{os.getcwd()}\\{folder_name}' if folder_name else os.getcwd()
dirs = os.listdir(path_dir)

created_list = list()
remove_list = list()
exists_list = list()

def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
    except FileExistsError as fe:
        print(fe)

def delete_folder(folder_name):
    try:
        os.rmdir(folder_name)
    except FileNotFoundError as nf:
        print(nf)

# the function creates files in the current directory, the number of which does not exceed 'count'
# if there are these files in the current directory, then the function does not duplicate them, 
# but only adds the missing amount
def create_js_file(tmp):    
    for k in range(1, count):
        tmp = file_name[:point_pos] + f'{k}' + file_name[point_pos:]
        if  tmp not in dirs:
            new_js_file = os.path.join(path_dir, tmp)
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
            old_js_file = os.path.join(path_dir, tmp)
            remove_list.append(tmp)
            os.remove(old_js_file)
        else:
            exists_list.append(tmp)


if __name__ == '__main__':
    if args.create and not args.delete:
        if folder_name:
            create_folder(folder_name)
        create_js_file(file_name)
        created_list = json.dumps(created_list)
        exists_list = json.dumps(exists_list)
        jsoncreated = json.loads(created_list)
        jsonexists = json.loads(exists_list)
        print('The following files have been successfully ',
        'created in the current directory:\n {}'.format(jsoncreated))
        print('The following files exist in the current directory: \n{}'.format(jsonexists))
    elif args.delete and not args.create:
        delete_js_file(file_name)
        deleted_list = json.dumps(remove_list)
        NOexists_list = json.dumps(exists_list)
        jsondeleted = json.loads(deleted_list)
        jsonNOexists = json.loads(NOexists_list)
        print('The following files have been successfully',
        'removed from the current directory:\n {}'.format(jsondeleted))
        print('The following files not exist in the current directory: \n{}'.format(jsonNOexists))
    elif del_folder_name:
        delete_folder(del_folder_name)
