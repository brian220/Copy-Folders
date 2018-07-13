"""
This program is going to move all the files from different folders to another folders

Author: b608390
"""
import os
import shutil
"""
#Ask user to input their source folder and destination folder
def input_folder():
  src_list = []
  dest_list = []
  src = input("Please input the src_folder_file:")
  dest = input("Please input the dest_folder_file:")
  src_file = open(src, "r")

  for line in open(src):
    src_list.append(src_file.readline().strip('\n'))
    print (src_list)
  src_file.close()
  
  dest_file = open(dest, "r")
  for line in open(dest):
    dest_list.append(dest_file.readline().strip('\n'))
    print (dest_list)
  dest_file.close()
  return src_list, dest_list
"""  
  
def move_file_between_folder(src_list, dest_list):
  for src, dest in zip(src_list, dest_list):
    print (src)
    print (dest)  
    src_files = os.listdir(src)
    for file_name in src_files:
      full_file_name = os.path.join(src, file_name)
      if (os.path.isfile(full_file_name)):
        shutil.copy(full_file_name, dest)
"""
def copy_folder():
  src_list, dest_list = input_folder()
  move_file_between_folder(src_list, dest_list)
  print ("Moving complete.")

copy_folder()
 """