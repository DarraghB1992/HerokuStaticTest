from signals import subscription_was_cancelled, subscription_created
from paypal.standard.ipn.signals import subscription_signup, subscription_cancel


subscription_signup.connect(subscription_created)
subscription_cancel.connect(subscription_was_cancelled)
