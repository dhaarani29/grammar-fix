from ollama import chat

sentence = input("Enter a sentence: ")

response = chat(
    model='llama3.2',
    messages=[
        {
            'role': 'user',
            'content': f'Correct the grammar and return only the corrected sentence: {sentence}'
        },
        {
            'role': 'system',
            'content': 'Rewrite professionally and return only the rewritten text.'
        }
    ]
)

print("\nCorrected:")
print(response['message']['content'])