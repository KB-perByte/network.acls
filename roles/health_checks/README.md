# Health Checks
The role allows users to perform platform-independent Access Control List (ACL) health checks, ensuring consistent and reliable validation across various networking environments.

## Capabilities

**ACL Health Checks** :
- Enables users to perform health checks for ACL configurations and their interface assignments.
- Users can perform the following health checks:
  - `available_acls`: Lists all ACLs configured on the device.
  - `missing_acls`: Identifies ACLs referenced in interfaces but not defined.
  - `unassigned_acls`: Shows ACLs that are defined but not used on any interface.
  - `interface_acl_status`: Shows the status of ACL assignments on interfaces.
    
## Variables

| Variable Name        | Default Value | Required | Type | Description                                                  |       Example       |
|:---------------------|:-------------:|:--------:|:----:|:-------------------------------------------------------------|:-------------------:|
| `ansible_network_os` | `""`          | no       | str  | Network OS to be used while performing health-checks.        | `"cisco.ios.ios"`   |

### Perform ACL Health Checks
- Health Checks operation verifies the current status of ACL configurations and their assignments.
- This can also include details about ACL rules and interface bindings.

```yaml
- name: Perform ACL health checks
  hosts: ios
  gather_facts: false
  tasks:
    - name: Run ACL health checks
      ansible.builtin.include_role:
        name: network.acls.health_checks
      vars:
        ansible_network_os: cisco.ios.ios
        acl_health_check:
          name: health_check
          vars:
            details: true
            checks:
              - name: available_acls
              - name: missing_acls
              - name: unassigned_acls
              - name: interface_acl_status
```
## License
GNU General Public License v3.0 or later.
See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.

## Author Information
- Ansible Network Content Team
