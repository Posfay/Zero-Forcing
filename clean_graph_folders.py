import os
import datetime


def create_timestamp():

    t = datetime.datetime.now()
    time_stamp = f"[{t.strftime('%H')}:{t.strftime('%M')}:" \
                 f"{t.strftime('%S')}.{t.strftime('%f')}]"
    return time_stamp


def clear_one_dir(path):

    max_zf = 0
    n = 0
    d = 0

    timestamp = create_timestamp()
    print(f"{timestamp} - Scanning folder: {path}")

    for e in os.scandir(path):
        if e.is_file():
            n += 1
            zf = int(e.name[0])
            if e.name[1].isnumeric():
                zf = int(e.name[0:2])
            if zf > max_zf:
                max_zf = zf

    timestamp = create_timestamp()
    print(f"{timestamp} - Found      {n}   files")

    for e in os.scandir(path):
        if e.is_file():
            zf = int(e.name[0])
            if e.name[1].isnumeric():
                zf = int(e.name[0:2])
            if zf < max_zf:
                os.remove(e.path)
                d += 1

    timestamp = create_timestamp()
    print(f"{timestamp} - Deleted    {d}   files")
    print("")


def clear_dir(path):

    for e in os.scandir(path):
        if e.is_dir() and len(e.name) == 2:
            clear_one_dir(e.path)


dir_path = os.path.abspath(os.path.dirname(__file__))

for entry in os.scandir(dir_path):
    if entry.is_dir() and entry.name == "Graphs":
        clear_dir(entry.path)

ts = create_timestamp()
input(f"{ts} - Ready. Press Enter to exit!")
