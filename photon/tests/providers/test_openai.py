from photon.providers import OpenAIProvider


def test_build_object():
    open_ai_provider = OpenAIProvider(response={
        "object": "chat.completion",
    })

    result = open_ai_provider.build_object(
        prompt="Hello, how are you?",
        model="davinci",
        tokens=10,
    )

    assert result == {
        "provider": "openai",
        "prompt": "Hello, how are you?",
        "model": "davinci",
        "tokens": 10,
        "response": '{"object": "chat.completion"}',
    }, "Should be equal"