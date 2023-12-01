=====================================
Network Acls Collection Release Notes
=====================================

.. contents:: Topics


v2.0.0
======

Release Summary
---------------

Starting from this release, the minimum `ansible-core` version this collection requires is `2.14.0`. The last known version compatible with ansible-core<2.14 is `v1.0.2`.

Major Changes
-------------

- Bumping `requires_ansible` to `>=2.14.0`, since previous ansible-core versions are EoL now.

v1.0.2
======

Bugfixes
--------

- Fix eos healthchecks, update regexes to render correct configuration.

v1.0.1
======

Documentation Changes
---------------------

- Update badges to refer to proper Github repository.
- Update installation process in README.

v1.0.0
======

Release Summary
---------------

Release 1.0.0 with support for health checks and collector setup.

Minor Changes
-------------

- Support deploy_collection action.

New Plugins
-----------

Filter
~~~~~~

- health_check_view - Generate the filtered health check dict based on the provided target.
