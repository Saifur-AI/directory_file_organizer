# -*- coding: utf-8 -*-
"""
Created on Thu May 19 12:10:07 2022

@author: msrahman
"""

import os
import shutil
import time

from glob import glob 

## FILL IN BELOW
source_dir ="./Downloads/" ## folder to track # example for Windows C:\\Users\\Name\\Downloads
ext_list=list([os.path.splitext(i)[1] for i in glob(source_dir+"*")])
ext_list=[x.strip() for x in ext_list if x.strip()]
dest_dir_ppt = source_dir+"PPT_doc/"## folder for images
dest_dir_excel = source_dir+"excel_doc/"## folder for images
dest_dir_music =  source_dir+"musics/"## folder for images
dest_dir_video =  source_dir+"videos/"## folder for images
dest_dir_image =  source_dir+"images/"## folder for images## etc
dest_dir_pdf = source_dir+"pdf/"## folder for images #example "C:\\Users\\Name\\Desktop\\Pdfs"
dest_dir_zip = source_dir+"zip/"## folder for images #example "C:\\Users\\Name\\Desktop\\Pdfs"
dest_dir_others = source_dir+"others/"## folder for images #example "C:\\Users\\Name\\Desktop\\Pdfs"
path = source_dir+"*{}"
file_types =ext_list# [".doc",".mov",".mp4",".mp3",".wav",".xlsx",".csv",".zip", ".rar",".jpg", ".pdf", ".png", ".txt",".ppt",".pptx",".docx"]
fnames = []
for ext in file_types:
    for fname in glob( path.format( ext )):
        if ext==".jpg" or ext==".png":
           dest = dest_dir_image
           os.makedirs(dest, exist_ok=True)
           shutil.move(fname,dest) 
        elif ext==".pdf":
            dest = dest_dir_pdf
            os.makedirs(dest, exist_ok=True)
            shutil.move(fname,dest) 
           
        elif ext==".ppt" or ext==".pptx" or ext==".doc" or ext==".docx":
            dest = dest_dir_ppt
            os.makedirs(dest, exist_ok=True)
            shutil.move(fname,dest)   
        elif ext==".mov" or ext==".mp4":
             dest = dest_dir_video
             os.makedirs(dest, exist_ok=True)
             shutil.move(fname,dest)     
             
             
        elif ext==".wav" or ext==".mp3":
             dest = dest_dir_music
             os.makedirs(dest, exist_ok=True)
             shutil.move(fname,dest)  

        elif ext==".csv" or ext==".xlsx":
             dest = dest_dir_excel
             os.makedirs(dest, exist_ok=True)
             shutil.move(fname,dest)  
        elif ext==".zip" or ext==".rar":
             dest = dest_dir_zip
             os.makedirs(dest, exist_ok=True)
             shutil.move(fname,dest)  
        else:
             dest = dest_dir_others
             os.makedirs(dest, exist_ok=True)
             shutil.move(fname,dest) 