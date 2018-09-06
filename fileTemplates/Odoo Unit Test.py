# -*- coding: utf-8 -*-
# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import fields
import openerp.tests

from dateutil.relativedelta import relativedelta

class $ClassName(openerp.tests.TransactionCase):
    def setUp(self, *args, **kwargs):
        super($ClassName, self).setUp(*args, **kwargs)
        # Init code before launch a test case
        
    def tearDown(self, *args, **kwargs):
       # self.do_something_after_all_tests()
       return super($ClassName, self).tearDown(*args, **kwargs)
       
    @openerp.tests.common.at_install(True)
    @openerp.tests.common.post_install(True)
    def test_CASENAME(self):
     self.assertTrue(True,"Not Yet Implemented")
        # Test case
