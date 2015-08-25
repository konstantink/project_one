import re
from django.conf import settings
import pysvn
from VCS.client.svn_client import Client
# import VCScreate

from backend.models import TestGroup, Test


# def create_update_test(VCScreate):
#     full_urls = VCScreate
#     new_test = re.search(r'runme__\d{3}.do', full_urls)
#     name_test = re.serch(r'\d{3}__\w+\.v(hdl?)?', full_urls)
#     if re.findall('(\d+)', new_test) == re.findall('(\d+)', name_test):
#         name_one_test = str(re.findall(r'^\w+', name_test))
#         name_new_test = new_test[0:-6] + name_one_test[2:-3] + new_test[-3:]
#         return name_new_test
#     else:
#         name_new_test = new_test
#         return name_new_test
#
#
# def create_dict_group(VCScreate, name_new_test):
#     full_urls = VCScreate
#     name_subgroup = re.findall(r'\w+', full_urls)[-2]
#     name_group = re.findall(r'\w+', full_urls)[-3]
#     create_dict = {
#         name_group:
#             {name_subgroup: name_new_test}
#     }
#     return create_dict

# TODO: Move to settings
TEST_MACRO_REGEXP = '/src/runme__(?P<num>\d{3})\.do$'
TEST_FILE_REGEXP = '/src/(?P<name>%s_\w+)\.v(hdl?)?$'
GROUP_REGEXP = '^(/(?P<supergroup>\w+))?/(?P<group>\w+)/(?P<subgroup>\w+)/src'

DEFAULT_TEST_NAME = 'runme__%s.do'


class TestGroupManager(object):

    #NOTE: paths should be sorted
    def create(self, paths):
        for path in paths:
            mr = re.search(TEST_MACRO_REGEXP, path)
            if mr is not None:
                num = mr.groupdict().get('num')
                name = self._get_test_name(paths, num) or DEFAULT_TEST_NAME % num
                supergroup, group, subgroup = self._get_group_names(path)
                if supergroup is not None:
                    supergroup = TestGroup.objects.get_or_create(name=supergroup)[0]
                group = TestGroup.objects.get_or_create(name=group, parent_group=supergroup)[0]
                subgroup = TestGroup.objects.get_or_create(name=subgroup, parent_group=group)[0]
                test = Test.objects.create(name=name, group=subgroup)

    def _get_group_names(self, path):
        mr = re.search(GROUP_REGEXP, path)
        if mr is not None:
            groups = mr.groupdict()
            return groups.get('supergroup'), groups.get('group'), groups.get('subgroup')
        return None, None, None

    def _get_test_name(self, paths, test_number):
        for path in paths:
            mr = re.search(TEST_FILE_REGEXP % test_number, path)
            if mr is not None:
                name = mr.groupdict().get('name')
                return name
        return None
