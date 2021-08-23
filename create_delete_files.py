import os
import json
import argparse 

parse = argparse.ArgumentParser()
parse.add_argument('-fo', '--folder', type=str, help = 'creates a new folder or navigates to that folder')
parse.add_argument('-f', '--file', type=str, help='the name of the instance of the file or files')
parse.add_argument('-cr', '--create',type = bool, help='creates a file')
parse.add_argument('-d', '--delete', type= bool, help='deletes the file')
parse.add_argument('-co', '--count', type = int, help='indicates the number of instances')
args = parse.parse_args()

folder_name = args.folder
file_name = args.file
count = args.count
point_pos = file_name.find('.') if file_name else None
count = (count +1) if count else None

path_list = os.listdir()
path_dir = os.getcwd() 

if folder_name:
    path_dir = f'{os.getcwd()}\\{folder_name}'
    

created_list = list()
remove_list = list()
exists_list = list()

# creates folder
def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
    except FileExistsError as fe:
        print(fe)

# deletes folder
def delete_folder(folder_name):
    try:
        os.rmdir(folder_name)
    except FileNotFoundError as nf:
        print(nf)

# the function creates files in the current directory, the number of which does not exceed 'count'
# if there are these files in the current directory, then the function does not duplicate them, 
# but only adds the missing amount
def create_file(tmp):    
    for k in range(1, count):
        tmp = file_name[:point_pos] + f'{k}' + file_name[point_pos:]
        if  os.path.exists(path_dir):
            new_file = os.path.join(path_dir, tmp)
            fl = open(new_file, 'w').close()
            created_list.append(tmp)
        else:
            exists_list.append(tmp)

# a function that removes files that enter the loop from zero to 'count'
# if the file is not in the current directory, then the function checks the next by number
def delete_file(tmp):
    for j in range(1, count):
        tmp = file_name[:point_pos] + f'{j}' + file_name[point_pos:]
        if os.path.exists(f'{path_dir}\\{tmp}'):
            old_file = os.path.join(path_dir, tmp)
            remove_list.append(tmp)
            os.remove(old_file)
        else:
            exists_list.append(tmp)

def create(f_name, cr_ls):
    create_file(f_name)
    created_list = json.dumps(cr_ls)
    #exists_list = json.dumps(ex_ls)
    jsoncreated = json.loads(created_list)
    #jsonexists = json.loads(exists_list)
    print('The following files have been successfully ',
    'created in the current directory: \n({})\n {}'.format(path_dir, jsoncreated))
    #print('The following files exist in the current directory: \n{}'.format(jsonexists))

def delete(f_name, rm_ls):
    delete_file(f_name)
    deleted_list = json.dumps(rm_ls)
    #NOexists_list = json.dumps(ex_ls)
    jsondeleted = json.loads(deleted_list)
    #jsonNOexists = json.loads(NOexists_list)
    print('The following files have been successfully',
    'removed from the current directory: \n({})\n {}'.format(path_dir, jsondeleted))
    #print('The following files not exist in the current directory: \n{}'.format(jsonNOexists))
    
if __name__ == '__main__': 
    if folder_name and args.create:
        create_folder(folder_name)
        if file_name:
            create(file_name, created_list)    
    elif not folder_name and args.create:
        create(file_name, created_list)
    elif not folder_name and args.delete:
        delete(file_name, remove_list)
    elif folder_name and args.delete:
        if file_name:
            delete(file_name,remove_list)
            os.chdir(path_dir)
        tmp_ls = os.listdir()
        os.chdir(r'C:\Users\Shadow\Desktop\py_projects')
        if not tmp_ls:
            print(tmp_ls)
            delete_folder(folder_name
