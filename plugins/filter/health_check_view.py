from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
    name: health_check_view
    author: Sagar Paul (@KB-perByte)
    version_added: "1.0.0"
    short_description: Generate the filtered health check dict based on the provided target.
    description:
        - Generate the filtered health check dict based on the provided target.
    options:
      health_facts:
        description: Specify the health check dictionary.
        type: dict
"""

EXAMPLES = r"""
# ACLs configuration in device

# Router#sh access-lists
# Standard IP access list 2
#     30 permit 172.16.1.11
#     20 permit 172.16.1.10
#     10 permit 172.16.1.2
# Extended IP access list 101
#     15 permit tcp any host 172.16.2.9
#     18 permit tcp any host 172.16.2.11
#     20 permit udp host 172.16.1.21 any
#     30 permit udp host 172.16.1.22 any
#     40 deny icmp any 10.1.1.0 0.0.0.255 echo
#     50 permit ip any 10.1.1.0 0.0.0.255
#     60 permit tcp any host 10.1.1.1 eq telnet
#     70 permit tcp 10.1.1.0 0.0.0.255 172.16.1.0 0.0.0.255 eq telnet time-range EVERYOTHERDAY (active)
# Extended IP access list DNB-SNMP
#     10 permit ip host 10.0.1.1 any
#     20 permit ip host 10.0.1.2 any
#     30 permit ip host 10.0.1.3 any
#     40 deny ip any any log
# Extended IP access list acl_123
#     10 permit tcp any any eq 22
#     21 permit tcp host 192.168.11.8 host 192.168.20.5 eq 22
#     30 deny ip any any
# Extended IP access list google_block
#     10 deny ip any host 8.8.8.8
# Extended IP access list outboundfilters
#     10 permit icmp 10.1.1.0 0.0.0.255 172.16.1.0 0.0.0.255
# Extended IP access list test
#     10 permit ip host 10.2.2.2 host 10.3.3.3
#     20 permit tcp host 10.1.1.1 host 10.5.5.5 eq www
#     30 permit icmp any any
#     40 permit udp host 10.6.6.6 10.10.10.0 0.0.0.255 eq domain

# INTERFACEs configuration in device

# Router#sh ip interface
# GigabitEthernet1 is up, line protocol is up
#   Address determined by DHCP
#   MTU is 1500 bytes
#   Helper address is not set
#   Directed broadcast forwarding is disabled
#   Outgoing Common access list is not set
#   Outgoing access list is google_block
#   Inbound Common access list is not set
#   Inbound  access list is not set
# GigabitEthernet2 is up, line protocol is up
#   Helper address is not set
#   Directed broadcast forwarding is disabled
#   Outgoing Common access list is not set
#   Outgoing access list is test
#   Inbound Common access list is not set
#   Inbound  access list is acl_123
#   Proxy ARP is enabled
# GigabitEthernet3 is administratively down, line protocol is down
#   Internet protocol processing disabled
# GigabitEthernet3.100 is administratively down, line protocol is down
#   Internet protocol processing disabled
# GigabitEthernet4 is administratively down, line protocol is down
#   Internet protocol processing disabled
# Loopback999 is administratively down, line protocol is down
#   Internet protocol processing disabled
# Port-channel10 is down, line protocol is down
#   Internet protocol processing disabled
# Port-channel20 is down, line protocol is down
#   Internet protocol processing disabled
# Port-channel30 is down, line protocol is down
#   Internet protocol processing disabled

- name: Perform ACLs health checks
  hosts: iosxe
  gather_facts: false
  tasks:
    - name: ACLs health check via ACLs Manager
      ansible.builtin.include_role:
        name: network.acls.run
      vars:
        actions:
          - name: health_check

# Task Output:
# ------------
#
# TASK [network.acls.run : Resource health checks]
#   health_checks:
#     GigabitEthernet1:
#       name: GigabitEthernet1
#       outbound:
#         acl_type: extended
#         afi: ipv4
#         grant: deny
#         name: google_block
#         sequence: 10
#       status: up
#     GigabitEthernet2:
#       inbound:
#         acl_type: extended
#         afi: ipv4
#         grant: deny
#         name: acl_123
#         sequence: 30
#       name: GigabitEthernet2
#       outbound:
#         acl_type: extended
#         afi: ipv4
#         grant: permit
#         name: test
#         sequence: 40
#       status: up
#     GigabitEthernet3:
#       name: GigabitEthernet3
#       status: down
#     GigabitEthernet3.100:
#       name: GigabitEthernet3.100
#       status: down
#     GigabitEthernet4:
#       name: GigabitEthernet4
#       status: down
#     Loopback999:
#       name: Loopback999
#       status: down
#     Port-channel10:
#       name: Port-channel10
#       status: down
#     Port-channel20:
#       name: Port-channel20
#       status: down
#     Port-channel30:
#       name: Port-channel30
#       status: down
"""

RETURN = """
  health_checks:
    description: ACLs health checks
    type: dict

"""

from ansible.errors import AnsibleFilterError

ARGSPEC_CONDITIONALS = {}

import debugpy

debugpy.listen(3000)
debugpy.wait_for_client()


def health_check_view(*args, **kwargs):
    params = ["acls_facts", "target"]

    data = dict(zip(params, args))
    data.update(kwargs)
    if len(data) < 2:
        raise AnsibleFilterError(
            "Missing either 'health facts' or 'other value in filter input,"
            "refer 'ansible.utils.health_check_view' filter plugin documentation for details",
        )
    acls_facts = data.get("acls_facts", {})
    checks = data.get("target", {}).get("checks")

    if acls_facts.get("interface_data") or acls_facts.get("acls_data"):
        acls = list(acls_facts.get("acls_data", {}).keys())
        details = {}
        for intf, intf_details in acls_facts.get("interface_data").items():
            for direction in ["inbound_v4", "outbound_v4", "inbound_v6", "outbound_v6"]:
                if intf_details.get(direction):
                    intf_details[direction] = acls_facts.get("acls_data", {}).get(
                        intf_details.get(direction)
                    )
            details[intf] = intf_details

        return details


def get_status(stats, check, count=None):
    pass


def get_ignore_status(item):
    pass


def is_present(health_checks, option):
    pass


def get_health(checks):
    pass


class FilterModule(object):
    """health_check_view"""

    def filters(self):
        """a mapping of filter names to functions"""
        return {"health_check_view": health_check_view}
