from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.idm import dashboard


class myApplications(horizon.Panel):
    name = _("My Applications")
    slug = "myApplications"


dashboard.Idm.register(myApplications)