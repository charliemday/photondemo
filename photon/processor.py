from .providers import OpenAIProvider


class PhotonProcessor:
    """
    This class handles processing the response from the different
    providers
    """

    def __init__(self, provider: str = None, response: dict = None, *args, **kwargs) -> None:
        self.provider = provider
        self.args = args
        self.kwargs = kwargs
        self.response = response
        self.providers = ["openai", "anthropic", "replicate"] # TODO: Add more providers

    def process_provider(self, *args, **kwargs) -> None:
        # Check if provider is valid
        if self.provider not in self.providers:
            raise ValueError(f"Provider must be one of {self.providers}")
        
        if self.provider == "openai":
            provider = OpenAIProvider(self.response)
            return provider.process_response(*args, **kwargs)
            # Do something

        # TODO: Add further providers

        return None