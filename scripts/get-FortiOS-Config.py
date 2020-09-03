from sys import argv

ip_address = argv[1]
user = argv[2]
passwd = argv[3]
filename = argv[4]
backup_dir = argv[5]
full_backup = False


def backup_config(ip, username, password, full, path):
    """
    Retrieve fortigate configuration and save it to the local path
    :param ip: a string for target ip address
    :param username: a string for username who has read access
    :param password: a string for password
    :param full: boolean . Get full config if True, Get minimum config(diff from the factory default config) if False
    :param path: path to save the backup file
    :return: Name of the file saved with full path
    """
    import paramiko
    from scp import SCPClient

    ssh = paramiko.client.SSHClient()
    # ssh.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
    ssh.set_missing_host_key_policy(paramiko.WarningPolicy())
    # ssh.load_system_host_keys()

    try:
        ssh.connect(ip, username=username, password=password)

    except Exception as e:
        return str(e)

    else:
        with SCPClient(ssh.get_transport()) as scp:
            if full:
                config = 'fgt_config'
            else:
                config = 'sys_config'

            try:
                scp.get(config, path)

            except Exception as e:
                response = str(e)

            else:
                response = 'ok'

        return response


if __name__ == '__main__':
    result = backup_config(ip_address, user, passwd, full_backup, backup_dir + "/" + filename)
    print(result)
