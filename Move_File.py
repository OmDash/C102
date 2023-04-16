import os
import shutil


from_dir = os.path.expanduser("FolderA")
to_dir = os.path.expanduser("FolderB")


list_of_files = os.listdir(from_dir)
print(list_of_files)


for file_name in list_of_files:
   
    name, extension = os.path.splitext(file_name)
    
 
    if extension == '':
        continue
    
    
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        
       
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, file_name)      
        
        print("Moving", file_name)
        shutil.move(path1, path2)