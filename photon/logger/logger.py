import requests


class PhotonLogger:
    def __init__(self, *args, **kwargs) -> None:
        custom_url = kwargs.get("custom_url")
        self.photon_url = "https://beacon-demo-production.up.railway.app/api" if custom_url is None else custom_url

    def log_output(self, payload):
        endpoint = "/prompts/log-prompt/"
        url = self.photon_url + endpoint
        response = requests.post(url, json=payload) 
        return response