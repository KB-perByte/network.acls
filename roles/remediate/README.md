# Remediate

## Overview
The `remediate` role enables users to fix ACL configuration drifts by overriding the running access control policies with the desired state provided in the inventory host variables. This role ensures that network devices maintain their intended access control configurations and security policies.

## Features
- Remediate ACL configuration drifts by applying the desired state.
- Supports both local and remote SCM data stores
- Ensures network devices maintain consistent and secure access control policies

## Variables

| Variable Name        | Default Value | Required | Type | Description                                                   |          Example         |
|:---------------------|:-------------:|:--------:|:----:|:------------------------------------------------------------- |:------------------------:|
| `ansible_network_os` | `""`          | no       | str  | Network OS to be used during remediation.                     |      `"cisco.ios.ios"`   |
| `data_store`         | `""`          | yes      | dict | Specifies the data store to be used (local or SCM).           | See usage example below. |

## Usage
Below are examples demonstrating how to use the `persist` role:

```yaml
---
- name: Remediate ACL configuration drift from local data store
  hosts: all
  gather_facts: true
  tasks:
    - name: Invoke remediate role
      ansible.builtin.include_role:
        name: network.acls.remediate
      vars:
        data_store:
          local: "~/data/network"
```
Example Output
When the playbook is executed, the persisted ACL configurations will be saved in the specified data store in a structured YAML format.

### Example 2: Remediate ACL Drift from SCM Repository
This example reads inventory host variables from a remote SCM repository and applies them to the network devices if ACL configuration drift exists:
**[CAUTION!]**: This operation will override the running ACL configurations on the device. Use with care in production environments.
```yaml
---
- name: Remediate ACL configuration drift from SCM repository
  hosts: all
  gather_facts: true
  tasks:
    - name: Invoke remediate role
      ansible.builtin.include_role:
        name: network.acls.remediate
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
## License
GNU General Public License v3.0 or later.
See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.

## Author Information
- Ansible Network Content Team
