import os
import subprocess

file_path = os.path.abspath(os.path.dirname(__file__))

subprocess.Popen(f'start /wait zf.exe 12 "{file_path}"', shell=True)
subprocess.Popen(f'start /wait zf.exe 14 "{file_path}"', shell=True)
subprocess.Popen(f'start /wait zf.exe 16 "{file_path}"', shell=True)
subprocess.Popen(f'start /wait zf.exe 18 "{file_path}"', shell=True)
subprocess.Popen(f'start /wait zf.exe 20 "{file_path}"', shell=True)
