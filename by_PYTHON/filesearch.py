import os
working_dir = os.path.dirname(os.path.realpath(__file__)) 
files = []
def fileSearch(dir_name):
    file_lst = os.listdir(dir_name)
    for filename in file_lst:
        full_filename = os.path.join(dir_name,filename)
        if os.path.isdir(full_filename):
            fileSearch(full_filename)
        else:
            files.append(full_filename)
