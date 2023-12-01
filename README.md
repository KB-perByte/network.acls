# Network Acls Validated Content
[![Test collection](https://github.com/redhat-cop/network.acls/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/redhat-cop/network.acls/actions/workflows/tests.yml)[![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/7660/badge)](https://bestpractices.coreinfrastructure.org/projects/7660)

This repository contains the `network.acls` Ansible Collection.

## Description

The `network.acls` enables users to manage the acls resources independent of platforms and perform acls health checks.

## Tested with Ansible

Tested with ansible-core >=2.14 releases.

## Installation
To consume this Validated Content from Automation Hub, the following needs to be added to `ansible.cfg`:

```
[galaxy]
server_list = automation_hub

[galaxy_server.automation_hub]
url=https://cloud.redhat.com/api/automation-hub/
auth_url=https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token
token=<SuperSecretToken>
```
Get the required token from the [Automation Hub Web UI](https://console.redhat.com/ansible/automation-hub/token).

With this configured, simply run the following commands:

```
ansible-galaxy collection install network.base
ansible-galaxy collection install network.acls
```

**Capabilities**
- `Build Brownfield Inventory`: This enables users to fetch the YAML structured resource module facts for acls resources like acls and acls_interfaces and save them as host_vars to a local or remote data store which could be used as a single SOT for other operations.
- `Acls Resource Management`: Users want to be able to manage the acls and acl_interfaces configurations.
  This also includes the enablement of gathering facts, updating acls resource host-vars, and deploying config onto the appliance.
- `Acls Health Checks`: Users want to be able to perform health checks for acls applications. These health checks should be able to provide the acls configuration status with the necessary details.
- Detect Drift and remediate: This enables users to detect any drift between the provided config and running-config and if required then override the running config.

### Usage
This platform-agnostic role enables the user to perform acls health checks. Users can perform the following health checks:
       `available_acls`
       `details`
       `missing_acls`
       `unassigned_acls`
- This role enables users to create a runtime brownfield inventory with all the acls configurations regarding host vars. These host vars are ansible facts gathered through the *_acls and *_acl_interfaces network resource modules. The tasks offered by this role can be observed below:

### Perform acls Health Checks
- Health Checks operation fetches the current status of acls configuration health.
- This can also include the details about the acls available, missing (not configured), and unassigned acls.

```yaml
health_checks.yml
---
- name: Perform health checks
  hosts: rtr1
  gather_facts: false
  tasks:
  - name: Acls Manager
    ansible.builtin.include_role:
      name: network.acls.run
    vars:
      ansible_network_os: cisco.ios.ios
      operations:
        - name: health_check
```


### Building Brownfield Inventory with Persist
- Persist operation fetches the acls and acls_interfaces facts and stores them as host vars.
The result of a successful Persist operation would be host_vars having YAML formatted resource facts.
- These host_vars could exist locally or even be published to a remote repository acting as SOT for operations like deploy, remediate, detect, etc.

#### - fetch acls resource facts and build local data_store.
```yaml
- name: Persist the facts into host vars
  hosts: rtr1
  gather_facts: false
  tasks:
  - name: Network acls Manager
    ansible.builtin.include_role:
      name: network.acls.run
    vars:
      ansible_network_os: cisco.ios.ios
      operations:
        - name: persist
      data_store:
        local: "~/backup/network"
```

#### - fetch acls resource facts and publish persisted host_vars inventory to the GitHub repository.
```yaml
- name: Persist the facts into remote data_store which is a github repository
  hosts: rtr1
  gather_facts: false
  tasks:
  - name: Network acls Manager
    ansible.builtin.include_role:
      name: network.acls.run
    vars:
      ansible_network_os: cisco.ios.ios
      operations:
        - name: persist
      persist_empty: false
      data_store:
        scm:
          origin:
            url: "{{ your_github_repo }}"
            token: "{{ github_access_token }}"
            user:
              name: "{{ ansible_github }}"
              email: "{{ your_email@example.com }}"
```

### Display Structured Data with Gather
- The gather operation gathers the running configuration specific to acls, acl_interfaces resources
  and displays these facts in YAML formatted structures.

```yaml
- name: Display acls resources in a structured format
  hosts: rtr1
  gather_facts: false
  tasks:
  - name: Acls Manager
    ansible.builtin.include_role:
      name: network.acls.run
    vars:
      ansible_network_os: cisco.ios.ios
      operations:
        - name: gather
```

### Deploy Acls Configuration
- Deploy operation will read the facts from the provided/default or remote inventory and deploy the changes onto the appliances.

#### read host_vars from local data_store and deploy onto the field.
```yaml
- name: Deploy changes
  hosts: rtr1
  gather_facts: false
  tasks:
  - name: Network acls Manager
    ansible.builtin.include_role:
      name: network.acls.run
    vars:
      ansible_network_os: cisco.ios.ios
      operations:
        - name: deploy
      data_store:
        local: "~/backup/network"
```

#### retrieve host_cars from the Github repository and deploy changes onto the field.
```yaml
- name: retrieve config from github repo and deploy changes
  hosts: rtr1
  gather_facts: false
  tasks:
  - name: Network acls Manager
    ansible.builtin.include_role:
      name: network.acls.run
    vars:
      ansible_network_os: cisco.ios.ios
      operations:
        - name: deploy
      persist_empty: false
      data_store:
        scm:
          origin:
            url: "{{ your_github_repo }}"
            token: "{{ github_access_token }}"
            user:
              name: "{{ ansible_github }}"
              email: "{{ your_email@example.com }}"
```

### Detect configuration drift in acls Configuration
- Detect operation will read the facts from the local provided/default inventory and detect if any configuration diff exists w.r.t running-config.

#### detect the config difference between host_vars in local data_store and running-config.

```yaml
- name: Configuration drift detection
  hosts: rtr1
  gather_facts: false
  tasks:
  - name: Network acls Manager
    ansible.builtin.include_role:
      name: network.acls.run
    vars:
      ansible_network_os: cisco.ios.ios
      operations:
        - name: detect
      data_store:
        local: "~/backup/network"
```

- Detect operation will read the facts from the GitHub repository inventory and detect if any configuration diff exists w.r.t running-config.

#### detect the config difference between host_vars in local data_store and running-config.
```yaml
- name: Configuration drift detection
  hosts: rtr1
  gather_facts: false
  tasks:
  - name: Network acls Manager
    include_role:
      name: network.acls.run
    vars:
      ansible_network_os: cisco.ios.ios
      operations:
        - name: detect
      data_store:
        scm:
          origin:
            url: "{{ your_github_repo }}"
            token: "{{ github_access_token }}"
            user:
              name: "{{ ansible_github }}"
              email: "{{ your_email@example.com }}"
```

#### Remediate configuration drift in acls Configuration
The remediate operation will read the facts from the locally provided/default inventory and remediate if any configuration changes are there on the appliances using the overridden state.

```yaml
- name: Remediate configuration
  hosts: rtr1
  gather_facts: false
  tasks:
  - name: Network acls Manager
    include_role:
      name: network.acls.run
    vars:
      ansible_network_os: cisco.ios.ios
      operations:
        - name: remediate
      data_store:
        local: "~/backup/network"
```

The remediate operation will read the facts from the Github repository and remediate if any configuration changes are there on the appliances using the overridden state.

```yaml
- name: Remediate configuration
  hosts: rtr1
  gather_facts: false
  tasks:
  - name: Network acls Manager
    include_role:
      name: network.acls.run
    vars:
      ansible_network_os: cisco.ios.ios
      operations:
        - name: remediate
      data_store:
        scm:
          origin:
            url: "{{ your_github_repo }}"
            token: "{{ github_access_token }}"
            user:
              name: "{{ ansible_github }}"
              email: "{{ your_email@example.com }}"
```

### Code of Conduct
This collection follows the Ansible project's
[Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html).
Please read and familiarize yourself with this document.


## Release notes

Release notes are available [here](https://github.com/redhat-cop/network.acls/blob/main/CHANGELOG.rst).

## Licensing

GNU General Public License v3.0 or later.

See [COPYING](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
