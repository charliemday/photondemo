import requests


class PhotonLogger:
    def __init__(self, *args, **kwargs) -> None:
        self.photon_url = "https://beacon-demo-production.up.railway.app/api"

    def log_output(self, payload):
        endpoint = "/prompts/log-prompt/"
        url = self.photon_url + endpoint
        response = requests.post(url, json=payload) 
        return response