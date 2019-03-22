import unittest
from tests.Accounts import test_users
from tests.Accounts import test_groups
from tests.Accounts import test_accounts

"""
    NOTICE: Give id_filepath in group_manager an absolute value before starting or the test 
    cases might create separate files in different directories that could cause them to fail. 
"""
loader = unittest.TestLoader()
user_suite = loader.loadTestsFromModule(test_users)
group_suite = loader.loadTestsFromModule(test_groups)
account_suite = loader.loadTestsFromModule(test_accounts)
all_tests = unittest.TestSuite([user_suite, group_suite, account_suite])
unittest.TextTestRunner(verbosity=2).run(all_tests)
