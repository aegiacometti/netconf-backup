import sys
import time
import glob
import os

# Specify how many backup files do you want to keep
num_files = 10

device_hostname = sys.argv[1]
output = sys.argv[2]


def remove_old_files():
    list_files = glob.glob('../backup/{}*'.format(device_hostname))

    if len(list_files) >= num_files:
        list_files.sort(reverse=True)
        for index in range(num_files-1, len(list_files)):
            os.remove(list_files[index])


def search_changed_config_file():
    list_files = glob.glob('../backup/{}*'.format(device_hostname))

    if len(list_files) == 0:
        return True

    list_files.sort(reverse=True)

    last_file = open(list_files[0], 'r')
    last_file_text = last_file.read()

    return output != last_file_text


def save_file():
    get_date = time.localtime()
    current_date = time.strftime('%Y-%m-%d-%H-%M-%S', get_date)

    filename = '../backup/{}-{}.cfg'.format(device_hostname, current_date)
    file = open(filename, 'w')
    file.write(output)
    file.close()


if __name__ == '__main__':
    if search_changed_config_file():
        save_file()
    remove_old_files()
