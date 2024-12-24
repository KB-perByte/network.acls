# Gather

## Overview
The `gather` role enables users to collect and display structured facts for ACL configurations across network devices. This role helps administrators gain insights into the current state of access control lists and their interface assignments in a standardized format.

## Features
- Retrieve structured facts for specified network resources.
- Support for various network resources like `acl_interfaces`,`acls` etc.
- Provides data in YAML format for easy consumption and analysis.

## Variables

| Variable Name        | Default Value | Required | Type | Description                                                  |      Example        |
|:---------------------|:-------------:|:--------:|:----:|:-------------------------------------------------------------|:-------------------:|
| `ansible_network_os` | `""`          | no       | str  | Network OS to be used during gather.                         |  `"cisco.ios.ios"`  |

## Usage
Below is an example playbook demonstrating how to use the `gather` role to collect ACL configurations:

```yaml
---
- name: Gather structured facts for ACL resources
  hosts: all
  gather_facts: true
  tasks:
    - name: Invoke gather role
      ansible.builtin.include_role:
        name: network.acls.gather
      vars:
        ansible_network_os: cisco.ios.ios
```
Example Output
When the playbook is executed successfully, the output will display the structured facts for the specified resources.

## License
GNU General Public License v3.0 or later.
See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.

## Author Information
- Ansible Network Content Team
