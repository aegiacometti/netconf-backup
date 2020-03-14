import sys
import time
import glob
import os

device_hostname = sys.argv[1]
historic_files_to_keep = sys.argv[2]


def remove_old_files():
    list_files = glob.glob('./backup/{}*'.format(device_hostname))

    if len(list_files) >= int(historic_files_to_keep):
        list_files.sort()
        for index in range(int(historic_files_to_keep)-1, len(list_files)-1):
            os.remove(list_files[index])


def rename_current_file():
    get_date = time.localtime()
    current_date = time.strftime('%Y-%m-%d-%H-%M-%S', get_date)

    filename = './backup/{}-{}.ucs'.format(device_hostname, current_date)

    os.rename('./backup/backup.ucs', filename)


if __name__ == '__main__':
    rename_current_file()
    remove_old_files()
