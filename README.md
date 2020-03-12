# Simple configuration backup for Cisco IOS, ASA and F5

Simple and complete backup setup with Ansible and Python3.
 
The master Playbook ``netconfig-backup.yml`` imports the Playbooks for IOS, ASA, and F5.

Each Playbook will get and store de configuration in the ``./backup`` directory, including hostname and date.

Will only store the configuration if it's different from the last backup. (NA for F5)

Will keep a historic of 10 configuration files.

Will send an email if a configuration backup fail per device.

## Requirements
- Ansible
- Python3

## Setup
Customize the ``hosts`` file according to your needs. *(Sample file provided)*

*(Optional)* - It's recommended to use **Ansible-Vault** to hide the user/password information. Refer to Ansible Documentation at https://docs.ansible.com/ansible/latest/user_guide/vault.html

*(Optional)* - Modify the master Playbook if you don't need backup of all the OSs, by commenting the respective line.

*(Optional)* - To modify the number of historic file to keep change that variable ``num_files`` in the scripts at ``playbooks/scripts`` directory.

Configure your email details at each of the playbooks in the ``./playbooks`` dir.

If you don't want the alerts when a backup fail, remove the task from the playbooks:

``- name: xxx - Sending an e-mail if host backup failed``

## Usage

Run the master Playbook with: ``ansible-playbook netconf-backup.yml``