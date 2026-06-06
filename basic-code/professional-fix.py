from ollama import chat

sentence = input("Enter a sentence: ")

response = chat(
    model='llama3.2',
    messages=[
        {
            'role': 'user',
            'content': sentence
        },
        {
            'role': 'system',
            'content': 'You are a helpful assistant that rewrites text professionally.'
        }
    ]
)

print("\nCorrected:")
print(response['message']['content'])