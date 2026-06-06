from ollama import chat

sentence = input("Enter a sentence: ")

response = chat(
    model = 'llama3.2',
    messages = [
        {
            'role': 'user',
            'content': sentence
        },
        {
            'role': 'system',
            'content': 'Make the text concise while keeping meaning.'
        }
    ]
)

print("\nConcise:")
print(response['message']['content'])