import os
import secrets
from time import sleep
import shutil
import subprocess
import time


new_render_path = "F:/FTP/tauans-remote-render/new-render-jobs/"
finished_render_jobs_path = "F:/FTP/tauans-remote-render/finished-render-jobs/"
blender_path = "C:/Program Files/Blender Foundation/Blender 3.0/"
processed_path = "F:/FTP/tauans-remote-render/processed-jobs/"
path_to_log = "F:/FTP/tauans-remote-render/logs/"


def new_job_in_path():
    dir_content = os.listdir(new_render_path)
    files_in_path = len(dir_content)
    if files_in_path > 0:
        return True
    else:
        return False

def move_file_to_processed():
    shutil.move(name_and_path_of_file, processed_path+name_of_file)

def rename_file_in_process_folder():
    os.rename(processed_path+name_of_file, processed_path+str(secrets.token_hex(15))+name_of_file)

def get_name_of_file():
    dir_content = os.listdir(new_render_path)
    file_name = dir_content[0]
    return file_name

def get_time():
    return str(time.strftime("%Y-%m-%d-%H-%M"))

def new_blender_job():
    print("New job found!")
    blender_command = f"blender.exe -b {name_and_path_of_file} -o {finished_render_jobs_path}render_{get_time()} -F PNG -f -1"
    print(blender_command)
    print(blender_path)
    full_command = blender_path+blender_command
    logg = open("F:/FTP/tauans-remote-render/logs/logs.txt", "w")
    subprocess.run(full_command, stdout=logg)
    #subprocess.run(full_command)

while True:
    error = False
    try:
        print("Waiting for a new job...")
        if new_job_in_path():
            name_and_path_of_file = new_render_path + get_name_of_file()
            name_of_file = get_name_of_file()
            new_blender_job()
            print("Job done!")
            move_file_to_processed()
            print("Moveing file...")
            sleep(5)
            rename_file_in_process_folder()
            print("Renaming file...")
        sleep(5)
    except Exception as E:
        print(E)
        error = True
        sleep(10)