import requests

from photon.config import PHOTON_API


class PhotonLogger:
    def __init__(self, *args, **kwargs) -> None:
        custom_url = kwargs.get("custom_url")
        self.disable = kwargs.get("disable")
        self.photon_url = PHOTON_API if custom_url is None else custom_url

    def log_output(self, payload):
        
        if self.disable:
            # Useful when you want to disable photon for testing
            return
                
        endpoint = "/prompts/log-prompt/"
        url = self.photon_url + endpoint
        response = requests.post(url, json=payload) 
        return response