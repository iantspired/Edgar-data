# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 13:41:54 2017

@author: Ian Thomas
"""

from pathlib import Path

#p is used to hold the name of the working path...
p = Path(r'C:\Users\ecikt\Python course\Lecturer files\data\10kdown')


directory_list=[]   #directory_list holds a list of subdirectories of the path p

for file_obj in p.glob('**/*'):  #file objs can be directories or files
    if file_obj.is_dir():   #if the file object is a directory...
        directory_list.append(file_obj.name)  # ...make a list of directories
        


files_count=0  #a variable that checks that all files in all directories have been processed
for direct_name in directory_list: # for all sub directories in the list...

    search_string = direct_name+'/*.txt'  #adds a directory path onto the search string used in glob
    
    # make a list of file names, using the .name property of file_obj, which is the txt files found by glob...
    file_list= [file_obj.name for file_obj in p.glob(search_string)]  #selects all the text files in that directory
    #file_list is a string list of file names.
    #When used with the Path variable p (defined above), 
    #the list can be used to open, read and write files, just like regular os expressions
    
    print('In the', direct_name, 'directory there are '+str(len(file_list))+' files.')
    files_count=files_count+len(file_list)    #updates the total count


print('\nA total of '+str(files_count)+' files have been processed.')

