import json


class OpenAIProvider:
    def __init__(self, response: dict) -> None:
        self.response = response
        self.request_type = response.get("object")

    def build_object(self, prompt, model, tokens):
        return {
            "provider": "openai",
            "prompt": prompt,
            "model": model,
            "tokens": tokens,
            "response": json.dumps(self.response),
        }

    def process_chat_completions(self, *args, **kwargs):
        prompt = kwargs.get("messages")[0].get("content")
        return self.build_object(
            prompt=prompt,
            model=kwargs["model"],
            tokens=self.response.usage.total_tokens,
        )

    def process_completion(self, *args, **kwargs):
        prompt = kwargs["prompt"]
        return self.build_object(
            prompt=prompt,
            model=kwargs["model"],
            tokens=self.response.usage.total_tokens,
        )

    def process_response(self, *args, **kwargs) -> None:
        if self.request_type == "chat.completion":
            return self.process_chat_completions(*args, **kwargs)

        if self.request_type == "completion":
            return self.process_completion(*args, **kwargs)

        return
