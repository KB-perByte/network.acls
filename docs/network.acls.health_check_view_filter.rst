.. _network.acls.health_check_view_filter:


******************************
network.acls.health_check_view
******************************

**Generate the filtered health check dict based on the provided target.**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Generate the filtered health check dict based on the provided target.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                <th>Configuration</th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>health_facts</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                    <td>
                    </td>
                <td>
                        <div>Specify the health check dictionary.</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

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
      hosts: ios
      gather_facts: false
      tasks:
        - name: ACLs health check via ACLs Manager
          ansible.builtin.include_role:
            name: network.acls.health
          vars:
            actions:
              - name: health_check

    # Task Output:
    # ------------
    #
    # TASK [network.acls.run : Resource health checks]
    #   failed_when_result: true
    #   health_checks:
    #     available_acls:
    #     - RM-MCAST-RP
    #     - test-rm
    #     - SNMP
    #     - branchoffices
    #     details:
    #       GigabitEthernet1:
    #         name: GigabitEthernet1
    #         outbound_v4: null
    #       GigabitEthernet2:
    #         inbound_v4: null
    #         name: GigabitEthernet2
    #         outbound_v4: null
    #       GigabitEthernet3:
    #         inbound_v4:
    #           aces:
    #             '10': permit
    #             '20': permit
    #           acl_type: extended
    #           afi: ipv4
    #           name: branchoffices
    #         name: GigabitEthernet3
    #       GigabitEthernet4:
    #         name: GigabitEthernet4
    #       Loopback888:
    #         name: Loopback888
    #       Loopback999:
    #         name: Loopback999
    #     missing_acls:
    #     - google_block
    #     - acl_123
    #     - test
    #     status: unsuccessful
    #     unassigned_acls:
    #     - RM-MCAST-RP
    #     - SNMP
    #     - test-rm



Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this filter:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>health_checks</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td></td>
                <td>
                            <div>ACLs health checks</div>
                    <br/>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Sagar Paul (@KB-perByte)


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.
