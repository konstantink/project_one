import re
from django.conf import settings
import pysvn
from VCS.client.svn_client import Client


class TestGroupManage(Client):
    def __init__(self):
        super(Client, self).__init__(**kwargs)

    def create_or_update(self):
        full_urls = self.urls('/Group/SubGroup/src/')
        new_test = re.search(r'runme__\d{3}.do', full_urls)
        name_test = re.serch(r'\d{3}__\w+\.v(hdl?)?', full_urls)
        if re.findall('(\d+)', new_test) == re.findall('(\d+)', name_test):
            name_one_test = str(re.findall(r'^\w+', name_test))
            name_new_test = new_test[0:-6] + name_one_test[2:-3] + new_test[-3:]
            return name_new_test
        else:
            name_new_test = new_test
            return name_new_test

    def create_dict_group(self):
        name_subgroup = re.findall(r'\w+', full_urls)[-2]
        name_group = re.findall(r'\w+', full_urls)[-3]
        create_dict = {name_group: {name_subgroup: name_new_test}}
        return create_dict
        


