#!/usr/bin/env python
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from nose.tools import assert_true, assert_false

from desktop.lib.django_test_util import make_logged_in_client
from desktop.lib.test_utils import grant_access
from oozie.tests import OozieBase


class TestAboutBase(OozieBase):
  def setUp(self):
    self.client = make_logged_in_client(username="about", is_superuser=False)
    grant_access("about", "about", "about")

    self.client_admin = make_logged_in_client(username="about_admin", is_superuser=True)
    grant_access("about_admin", "about_admin", "about")


class TestAbout(TestAboutBase):

  def test_admin_wizard_permissions(self):

    response = self.client_admin.get(reverse('about:index'))
    assert_true('Check Configuration' in response.content, response.content)

    response = self.client.get(reverse('about:index'))
    assert_false('Check Configuration' in response.content, response.content)
