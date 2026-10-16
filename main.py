import ollama

# URL = 'http://localhost:11434/api/chat'
MODEL_NAME = 'phi3'


def chat_request(messages):

    response = ollama.chat(model=MODEL_NAME, messages=messages)

    return response['message']['content']

def main():
    messages = [
        {
            'role': 'system',
            'content': 'You are a helpful assistant. Answer briefly and shortly'
        }
    ]

    print('phi3 simple chat. Type "exit" to exit')
    while True:
        user_input = input('You:  ')
        if user_input == 'exit':
            print('Exiting...')
            break

        messages.append({
            'role': 'user',
            'content': user_input
        })
        reply = chat_request(messages)
        messages.append({
            'role': 'assistant',
            'content': reply
        })

        print('\n Assistant: ', reply)
        print('_' * 60)


main()