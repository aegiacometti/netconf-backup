# Simple configuration backup for Cisco IOS, NxOS, ASA and F5

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
Customize the ``hosts`` file according to your needs. *(Sample file provided)*

## Usage

Run the master Playbook with: ``ansible-playbook netconf-backup.yml``

### Optionals

- It's recommended to use **Ansible-Vault** to hide the user/password information. Refer to Ansible Documentation at https://docs.ansible.com/ansible/latest/user_guide/vault.html

- To modify the number of historic file to keep change that variable ``historic_files_to_keep`` in the master Playbook ``netconfig-backup.yml``.

- If you want the alerts to be sent when a configuration backup fail, set to **"yes"** the variables 
"alert_mail" and/or "alert_slack" at the master Playbook ``netconfig-backup.yml``. And set your mail details and/or Slack webhook at the
playbooks ``netconfig-backup-send-mail.yml`` and/or ``netconfig-backup-msg-slack.yml``

- Add periodic execution via ``crontab -e``.
