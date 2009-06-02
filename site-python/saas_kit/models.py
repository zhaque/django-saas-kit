import re

from django.db import models

from subscription.signals import signed_up, subscribed
from muaccounts.models import MUAccount

def _domainify(s):
    s = s.lower()
    s = re.sub(r'[^a-z0-9-]+', '-', s)
    s = re.sub(r'^-+', '', s)
    s = re.sub(r'-+$', '', s)
    return s

def create_muaccount_on_subscribed(sender, user=None, **kwargs):
    base_dn = _domainify(user.username)

    taken_domains = set([
        mua.domain for mua in MUAccount.objects.filter(
            domain__contains=base_dn).all()])

    if base_dn not in taken_domains:
        mua = MUAccount(owner=user, domain=base_dn)
    else:
        i = 0
        while True:
            i += 1
            dn = '%s-%d' % (base_dn, i)
            if dn not in taken_domains:
                mua = MUAccount(owner=user, domain=dn)
                break

    mua.save()    # race condition here, but it's only an example code


signed_up.connect(create_muaccount_on_subscribed)
subscribed.connect(create_muaccount_on_subscribed)
