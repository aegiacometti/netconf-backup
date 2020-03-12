import sys
import time
import glob
import os

# Specify how many backup files do you want to keep
num_files = 10

device_hostname = sys.argv[1]


def remove_old_files():
    list_files = glob.glob('../backup/{}*'.format(device_hostname))

    if len(list_files) >= num_files:
        list_files.sort(reverse=True)
        for index in range(num_files-1, len(list_files)):
            os.remove(list_files[index])


def rename_current_file():
    get_date = time.localtime()
    current_date = time.strftime('%Y-%m-%d-%H-%M-%S', get_date)

    filename = '../backup/{}-{}.ucs'.format(device_hostname, current_date)

    os.rename('../backup/backup.ucs', filename)


if __name__ == '__main__':
    rename_current_file()
    remove_old_files()
