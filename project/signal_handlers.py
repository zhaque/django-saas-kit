import subscription.signals

def impossible_downgrade(sender, subscription, **kwargs):
    before = sender.subscription
    after = subscription
    if not after.price:
        if before.price: return "You cannot downgrade to a free plan."
        else: return None
        
    if before.recurrence_unit:
        if not after.recurrence_unit:
            return "You cannot downgrade from recurring subscription to one-time."
        else:
            if after.price_per_day() > before.price_per_day(): return None
            else: return "You cannot downgrade to a cheaper plan."
    else:
        if not after.recurrence_unit:
            if after.price > before.price: return None
            else: return "You cannot downgrade to a cheaper plan."

__installed = False
def install():
    global __installed
    if not __installed:
        subscription.signals.change_check.connect(impossible_downgrade)
        __installed = True
