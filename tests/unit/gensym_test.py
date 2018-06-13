import pytest 

from lvm_gensym import * 

used_lv_names = ['root', 'root_0', 'root_1', 'root_2', 'root_3', 'swap_0', 'swap', 'swap_1']

test_lv_names = [{'fs_type': 'ext', 'mount': '/' }, 
                 {'fs_type': 'zfs', 'mount': '/home/user'},
                 {'fs_type': 'swap', 'mount': ''}
                ]

used_vg_names = ['linux_host', 'rhel_user0', 'rhel_0_user']

test_vg_names = ['rhel_user', 'rhel_user_0', 'rhel_user_1', 
                 'rhel_user_2', 'rhel_user_3', 'linux_user',
                 'fedora_user', 'fedora_user_0', 'fedora_user_1'
                ]

lvm_facts = {'lvs': {'Home': '', 'Swap': '', 'Root': '', 
                     'Root_0': '', 'root': '', 'root_0': '',
                     'swap': '', 'swap_0': '', 'swap_1': '',
                    }, 
             'vgs': {'rhel_user': '', 'rhel_user_0': '', 'rhel_user_1': ''} 
            }

def test_unique_base_name():
    assert get_unique_name_from_base('root', used_lv_names) == 'root_4'
    assert get_unique_name_from_base('rhel_user', test_vg_names) == 'rhel_user_4'

def test_return_val():
    for (index, name) in enumerate(test_vg_names):
        assert name_is_unique(test_vg_names[index], used_vg_names) == True 

def test_get_base_vg_name():
    assert get_vg_name_base('hostname', 'rhel') == 'rhel_hostname'

def test_vg_eval():
    assert get_vg_name('user', lvm_facts) == 'rhel_user_2'
    assert get_vg_name('', lvm_facts) == 'rhel'

def test_lv_eval():
    expected = ['root_1', 'home_user', 'swap_2']

    for (ctr, name_inputs) in enumerate(test_lv_names):
        assert get_lv_name(name_inputs['fs_type'], name_inputs['mount'], lvm_facts) == expected[ctr]

def test_get_base_lv_name():
    expected = ['root', 'home_user', 'swap']

    for (ctr, names_input) in enumerate(test_lv_names):
        assert get_lv_name_base(names_input['fs_type'], names_input['mount']) == expected[ctr]
