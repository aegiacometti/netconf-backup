import sys
import time
import glob
import os

device_hostname = sys.argv[1]
output = sys.argv[2]
historic_files_to_keep = sys.argv[3]


def remove_old_files():
    list_files = glob.glob('./backups/{}*'.format(device_hostname))

    if len(list_files) >= int(historic_files_to_keep):
        list_files.sort()
        for index in range(int(historic_files_to_keep)-1, len(list_files)-1):
            os.remove(list_files[index])


def search_changed_config_file():
    list_files = glob.glob('./backups/{}*'.format(device_hostname))

    if len(list_files) == 0:
        return True

    list_files.sort(reverse=True)

    last_file = open(list_files[0], 'r')
    last_file_text = last_file.read()

    return output != last_file_text


def save_file():
    get_date = time.localtime()
    current_date = time.strftime('%Y-%m-%d-%H-%M-%S', get_date)

    filename = './backups/{}-{}.cfg'.format(device_hostname, current_date)
    file = open(filename, 'w')
    file.write(output)
    file.close()


if __name__ == '__main__':
    if search_changed_config_file():
        save_file()
    remove_old_files()
