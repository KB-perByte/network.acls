# Detect

## Overview
The `detect` role will read the ACL facts from the local provided/default inventory and detect if any configuration drift exists w.r.t running-config. This role enables users to identify differences between the current running ACL configurations and the desired state, ensuring access control policies remain consistent and secure across devices.

## Features
- Detect configuration drifts between running configurations and host variables.
- Support for local and remote data stores.
- Provide detailed reports of detected changes.

## Variables

| Variable Name        | Default Value | Required | Type | Description                                                   |         Example          |
|:---------------------|:-------------:|:--------:|:----:|:------------------------------------------------------------- |:------------------------:|
| `ansible_network_os` | `""`          | no       | str  | Network OS to be used during detect.                          |    `"cisco.ios.ios"`     |
| `data_store`         | `""`          | yes      | dict | Specifies the data store to be used (local or SCM).          | See usage example below. |

## Usage
Below are examples demonstrating how to use the `detect` role:

```yaml
- name: Detect ACL configuration drifts
  hosts: all
  gather_facts: true
  tasks:
    - name: Include detect role
      ansible.builtin.include_role:
        name: network.acls.detect
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
When the playbook is executed successfully, the role will output a report highlighting the detected configuration drifts.

### Example 2: Detect ACL Configuration Drift from Remote Data Store
This example detects drifts by comparing the running ACL configuration with data stored in a remote SCM repository:
```yaml
---
- name: Detect ACL configuration drifts from SCM repository
  hosts: all
  gather_facts: true
  tasks:
    - name: Invoke detect role
      ansible.builtin.include_role:
        name: network.acls.detect
      vars:
        data_store:
          scm:
            origin:
              url: "{{ gh_scm_url }}"
              token: "{{ gh_token }}"
              user:
                name: "{{ gh_username }}"
                email: "{{ gh_email }}"
```
Example Output
When the playbook is executed successfully, the role will output a report highlighting any detected ACL configuration drifts, including changes to ACL rules, interface assignments, and policy modifications.
## License
GNU General Public License v3.0 or later.
See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.

## Author Information
- Ansible Network Content Team
