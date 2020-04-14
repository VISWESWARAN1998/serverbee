# SWAMI KARUPPASWAMI THUNNAI

import requests


class DigitalOcean:

    def __init__(self, token):
        self.token = token

    def get_balance(self):
        balance = requests.get("https://api.digitalocean.com/v2/customers/my/balance",
                               headers={"Authorization": "Bearer {}".format(self.token)}).json()
        return balance

    def get_droplets(self):
        droplets = requests.get("https://api.digitalocean.com/v2/droplets",
                               headers={"Authorization": "Bearer {}".format(self.token)}).json()["droplets"]
        return droplets
