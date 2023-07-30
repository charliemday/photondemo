import typing

from photon.logger import PhotonLogger
from photon.processor import PhotonProcessor


class Photon:
    def __init__(self, module, module_name=None, debug_url = None, disable = False):
        self.module = module
        self.module_name = module.__name__ if module_name is None else module_name
        self.original_attr = None
        self.debug_url = debug_url
        self.disable = disable

    def __getattr__(self, attr):
        self.original_attr = getattr(self.module, attr)

        # If the original attribute is a class, return a new class
        if isinstance(self.original_attr, type):
            return Photon(self.original_attr, module_name=self.module_name)

        # If the original attribute is a function, return a new function
        if isinstance(self.original_attr, typing.Callable):
            return self.wrapper

        return self.original_attr

    def wrapper(self, *args, **kwargs):
        # Call the result
        result = self.original_attr(*args, **kwargs)

        # Pass in the result higher level photon
        processor = PhotonProcessor(
            response=result, provider=self.module_name, *args, **kwargs
        )

        try:
            # Log the output
            photon_logger = PhotonLogger(
                debug_url=self.debug_url, disable=self.disable
            )
            photon_logger.log_output(
                payload=processor.process_provider(*args, **kwargs)
            )
        except Exception as e:
            print("[Photon Error]", e)

        return result
