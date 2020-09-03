# Simple configuration backup for Cisco IOS, NxOS, ASA, Arista, F5 and FortiOS

Simple and complete backup setup with Ansible and Python3.
 
- The master Playbook ``netconfig-backup.yml`` imports the Playbooks for the OSs.

- Each Playbook will get and store de configuration in the ``./backup`` directory, with format "hostname-date-time".

- Will only store the configuration if it's different from the last backup. (NA for F5)

- By default keeps a historic of 10 configuration files. (read Optionals)

- Can send an email or Slack message if a configuration backup fail per device. (read Optionals)

## Requirements
- Ansible
- Python3

## Setup
Customize the ``hosts`` file according to your needs. *(Sample file provided)*.
Pay special attention to setup the ``platform=xxx`` value of each host.

## Usage

Run the master Playbook with: ``ansible-playbook netconf-backup.yml``

### Optionals

- It's recommended to use **Ansible-Vault** to hide the user/password information. Refer to Ansible Documentation at https://docs.ansible.com/ansible/latest/user_guide/vault.html

- To modify the number of historic file to keep change that variable ``historic_files_to_keep`` in the master Playbook ``netconfig-backup.yml``.

- If you want the alerts to be sent when a configuration backup fail, set to **"yes"** the variables 
"alert_mail" and/or "alert_slack" at the master Playbook ``netconfig-backup.yml``. And set your mail details and/or Slack webhook at the
file ``group_vars/all.yml``

- Add periodic execution via ``crontab -e``.

### Special SSH connectivity notes

If normal prompt ssh connection don't work, it will not work with Ansible either. So first check 
the normal ssh connection from command line, and if you have problems, check these
two configurations to add to your Linux.

- Depending on the OS of your network devices you might need to enable other SSH parameters.
lines with ``sudo vi /etc/ssh/ssh_config``.

``` 
#Legacy changes
KexAlgorithms diffie-hellman-group1-sha1,curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group14-sha1
Ciphers aes128-cbc,aes128-ctr,aes256-ctr
```

- On the Ansible side, analyse the addition of these two parameters in your ``.ansible.cfg``.

```
[defaults]
# uncomment this to disable SSH key host checking
host_key_checking = False

[paramiko_connection]
# When using persistent connections with Paramiko, the connection runs in a
# background process.  If the host doesn't already have a valid SSH key, by
# default Ansible will prompt to add the host key.  This will cause connections
# running in background processes to fail.  Uncomment this line to have
# Paramiko automatically add host keys.
host_key_auto_add = True
```
