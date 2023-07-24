import json


class OpenAIProvider:

    def __init__(self, response) -> None:
        self.response = response
        self.request_type = response.object


    def build_object(self, result, prompt, model, tokens):
        return {
            # TODO: Extend this string size
            "result": result[:200] if result is not None else "",
            "provider": "openai",
            "prompt": prompt,
            "model": model,
            "tokens": tokens,
            "response": json.dumps(self.response)
        }


    def process_chat_completions(self, *args, **kwargs):

        if self.response.choices[0].message.get("function_call") is not None:
            # Function call
            result = self.response.choices[0].message.function_call.arguments
        else:
            # Message call
            result = self.response.choices[0].message.content


        prompt = kwargs.get("messages")[0].get("content")
        return self.build_object(
            result=result,
            prompt=prompt,
            model=kwargs["model"],
            tokens=self.response.usage.total_tokens,
        )

    def process_completion(self, *args, **kwargs):
        result = self.response.choices[0].text
        prompt = kwargs["prompt"]
        return self.build_object(
            result=result,
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

        