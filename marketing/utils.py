

from django.conf import settings 
import requests 
import json


MAILCHIMP_API_KEY = getattr(settings,"MAILCHIMP_API_KEY", None)
MAILCHIMP_DATA_CENTER = getattr(settings,"MAILCHIMP_DATA_CENTER", None)
MAILCHIMP_EMAIL_LIST_ID = getattr(settings,"MAILCHIMP_EMAIL_LIST_ID", None)


class Mailchimp(object):
    def __init__(self):
        super(Mailchimp, self).__init__()
        self.key = MAILCHIMP_API_KEY
        self.api_url = "https://{dc}.api.mailchimp.com/3.0".format(dc=MAILCHIMP_DATA_CENTER)
        self.list_id = MAILCHIMP_EMAIL_LIST_ID
        self.list_endpoint = '{}/lists/7ad3556958'.format(self.api_url) #ошибка с list_id

    def check_subscription_status(self, email):
        endpoint = self.api_url
        r = requests.get(endpoint, auth =("", self.key))

        return r.json()
    
    def check_valid_status(self, status):
        choices = ['subscribed', 'unsubscribed', 'cleaned', 'pending']
        if status not in choices:
            raise ValueError("Not valid status")
        return status

    def add_email(self, email): # не работает 
        status = 'subscribed'
        # self.check_valid_status(status) - вызывает ValueErroe 
        data = {
            "email_address": email,
            "status": status,
        }
        endpoint = self.list_endpoint + "/members"
        r = requests.get(endpoint, auth =("", self.key), data=json.dumps(data))

        return r.json()

    