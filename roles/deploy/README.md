# Deploy

## Overview
The `deploy` role will read the ACL facts from the provided/default or remote inventory and deploy the changes onto the appliances. It enables users to read the config as host_vars from a local or remote data store and deploy ACL configurations if any changes are found. This role is designed to ensure that access control configurations remain consistent and secure across devices.

## Features
- Read ACL configuration data from local or remote repositories
- Deploy ACL configurations only when changes are detected
- Support for integration with Git repositories for version control
- Maintain consistent access control policies across network infrastructure

## Variables

| Variable Name        | Default Value | Required | Type | Description                                                   |          Example         |
|:---------------------|:-------------:|:--------:|:----:|:------------------------------------------------------------- |:------------------------:|
| `ansible_network_os` | `""`          | no       | str  | Network OS to be used during deploy.                          | `"cisco.ios.ios"`        |
| `data_store`         | `""`          | yes      | dict | Defines the source of the configurations (local or remote).   | See usage example below. |

## Usage
Below is an example playbook demonstrating how to use the deploy role to retrieve and deploy ACL configurations from a specified repository:

```yaml
- name: Deploy ACL configurations
  hosts: all
  gather_facts: true
  tasks:
    - name: Include deploy role
      ansible.builtin.include_role:
        name: network.acls.deploy
      vars:
        data_store:
          scm:
            origin:
              url: "{{ gh_scm_path }}"
              token: "{{ gh_token }}"
              user:
                name: "{{ gh_username }}"
                email: "{{ gh_user_email }}"
```
Example Output
When the playbook is executed successfully, the output will show the ACL configurations being deployed when output verbosity is debug mode.

## License
GNU General Public License v3.0 or later.
See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.

## Author Information
- Ansible Network Content Team
