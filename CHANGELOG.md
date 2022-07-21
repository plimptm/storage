Changelog
=========

[1.8.1] - 2022-06-12
--------------------

### New Features

- check for thinlv name before assigning to thinlv\_params

### Bug Fixes

- none

### Other Changes

- none

[1.8.0] - 2022-06-02
--------------------

### New Features

- LVM RAID raid0 level support
- Thin pool support

### Bug Fixes

- none

### Other Changes

- none

[1.7.3] - 2022-05-16
--------------------

### New Features

- add support for mount\_options

### Bug Fixes

- none

### Other Changes

- Use meta/collection-requirements.yml for collection dependencies
- bump tox-lsr version to 2.11.0; remove py37; add py310

[1.7.2] - 2022-04-19
--------------------

### New Features

- add xfsprogs for non-cloud-init systems
- allow role to work with gather\_facts: false
- add setup snapshot to install packages into snapshot

### Bug Fixes

- none

### Other Changes

- none

[1.7.1] - 2022-03-18
--------------------

### New Features

- Less verbosity by default

### Bug Fixes

- none

### Other Changes

- README-devel: Add information about the generated tests
- bump tox-lsr version to 2.10.1

[1.7.0] - 2022-01-10
--------------------

### New Features

- Add LVM RAID specific parameters to module\_args
- Added support for LVM RAID volumes
- Add support for creating and managing LVM cache volumes
- Nested module params checking
- Refined safe\_mode condition in create\_members

### Bug Fixes

- none

### Other Changes

- bump tox-lsr version to 2.8.3
- change recursive role symlink to individual role dir symlinks

[1.6.4] - 2021-12-01
--------------------

### New Features

- add support for storage\_udevadm\_trigger
- Add workaround for the service\_facts module for Ansible \< 2.12

### Bug Fixes

- none

### Other Changes

- remove py27 from github CI testing
- add tags to allow skipping lvm tests
- update tox-lsr version to 2.8.0

[1.6.3] - 2021-11-08
--------------------

### New Features

- support python 39, ansible-core 2.12, ansible-plugin-scan
- Add support for Rocky Linux 8

### Bug Fixes

- none

### Other Changes

- update tox-lsr version to 2.7.1
- add meta/requirements.yml; support ansible-core 2.11

[1.6.2] - 2021-10-04
--------------------

### New Features

- Replace crypttab with lineinfile
- replace json\_query with selectattr and map

### Bug Fixes

- none

### Other Changes

- Improve wording
- use apt-get install -y
- use tox-lsr version 2.5.1
- Added skip checks feature to speed up the tests

[1.6.0] - 2021-08-11
--------------------

### New Features

- Raise supported Ansible version to 2.9

### Bug Fixes

- none

### Other Changes

- none

[1.5.3] - 2021-08-07
--------------------

### New Features

- use volume1\_size; check for expected error

### Bug Fixes

- none

### Other Changes

- none

[1.5.2] - 2021-08-03
--------------------

### New Features

- none

### Bug Fixes

- none

### Other Changes

- tag tests that use NVME and SCSI

[1.5.1] - 2021-07-29
--------------------

### New Features

- none

### Bug Fixes

- omit unnecessary conditional - deadcode reported by static scanner

### Other Changes

- none

[1.5.0] - 2021-07-28
--------------------

### New Features

- percentage-based volume size \(lvm only\)

### Bug Fixes

- none

### Other Changes

- Allow a tolerance of up to 1% when verifying volume size in tests.
- skip vdo test if kernel module is not loadable
- Added support for NVME and SCSI HW test setup

[1.4.1] - 2021-07-14
--------------------

### New Features

- none

### Bug Fixes

- Fixed volume relabeling

### Other Changes

- none

[1.4.0] - 2021-06-23
--------------------

### New Features

- LVMVDO support

### Bug Fixes

- none

### Other Changes

- none

[1.3.1] - 2021-05-17
--------------------

### New Features

- Capture inherited volume type in return value.
- Look up pool by name without disk list
- Trim volume size as needed to fit in pool free space
- Be smarter in choosing expected partition name.

### Bug Fixes

- Fix issues found by linters - enable all tests on all repos - remove suppressions
- fix most ansible-test issues, suppress the rest

### Other Changes

- Remove python-26 environment from tox testing
- update to tox-lsr 2.4.0 - add support for ansible-test sanity with docker
- CI: Add support for RHEL-9

[1.3.0] - 2021-02-14
--------------------

### New Features

- remove include\_vars, use public: true to export role vars, defaults
- Updated exception message
- add centos8

### Bug Fixes

- fix indentation in main-blivet.yml
- Fix centos6 repos; use standard centos images
- Confusing error message fix
- Non-existent pool removal fix
- Missing parameters

### Other Changes

- use tox-lsr 2.2.0
- use molecule v3, drop v2
- drop localhost from tests\_deps.yml
- remove ansible 2.7 support from molecule
- use tox for ansible-lint instead of molecule
- use new tox-lsr plugin
- use github actions instead of travis

[1.2.2] - 2020-10-28
--------------------

### New Features

- none

### Bug Fixes

- Fix yamllint warnings in tests

### Other Changes

- issue-67: Create storage\_lsr sub-directory under module\_utils and move size.py there
- lock ansible-lint version at 4.3.5; suppress role name lint warning
- sync collections related changes from template to storage role

[1.2.1] - 2020-09-24
--------------------

### New Features

- Disallow toggling encryption in safe mode

### Bug Fixes

- Make the var load test compatible with old Jinja2 \(2.7\)

### Other Changes

- Lock ansible-lint on version 4.2.0
- collections prep - use FQRN

[1.2.0] - 2020-08-23
--------------------

### New Features

- Pass -F to mke2fs for whole disks in RHEL
- TLS/crypto param and key naming consistency
- Advanced options support for raid pools
- Updated version of \#64
- Add tests for the optional encryption parameters
- Simplify device path checking
- Update supported Fedora versions
- MDRAID support for volumes
- Encrypted Pools
- Encrypted Volumes
- Do not report null\_blk devices as unused disks.
- MDRAID support for pools
- Check for duplicate pool/volume names.
- Streamline dependency gathering
- Determine too\_large\_size dynamically

### Bug Fixes

- Fix of overlooked pylint errors
- Don't try to set up mounts with invalid mount points.
- bug with current implementation of platform/version specific vars/tasks file include/import
- Resize fixes
- Avoid using ansible\_failed\_task in rescue blocks
- update the indent by two spaces
- Correctly Manage Swap Volumes

### Other Changes

- Update condition in tests\_misc.yml
- add 'disks\_needed: 3' to tests\_raid\_volume\_options.yml
- Add new test case for FS resize
- Avoid using Jinja2 template markers in assert
- workaround travis CI docker version issue
- sync with latest template including shellcheck
- Check Volume Size in Tests
- Improved RAID tests
- Add test for the include variable problem
- update to latest template
- use tox; use latest template code
- use molecule v2

[1.1.0] - 2020-01-14
--------------------

### New Features

- Make remaining class new-style \(derive from object\)
- Replace selectattr filter with json\_query filter
- Add flag to prevent implicit removal of existing device/fs.

### Bug Fixes

- Fail if there are not enough disks for testing
- Avoid missing\_required\_lib introduced only in 2.8
- Remove a forgotten `raise` found by Coverity

### Other Changes

- Fix issues found by lgtm.com
- Specify Python 2 for LGTM
- Remove empty files for unsupported OS versions

[1.0.2] - 2019-08-15
--------------------

### New Features

- none

### Bug Fixes

- none

### Other Changes

- Improve the YAML format of the example and of one test. Use the Galaxy prefix in README

[1.0.0] - 2019-08-14
--------------------

### Initial Release