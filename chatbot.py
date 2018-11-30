import json
import random


class Chatbot:

    def __init__(self, corpus_path):
        self.corpus = json.load(open(corpus_path))
        self.welcome_response = {
            'intent': 'welcome',
            'text': "Hello, let's talk!",
        }
        self.fallback_response = {
            'intent': 'fallback',
            'text': "Sorry, I can't understand this.",
        }

    def chat(self, question):
        response = {
            'intent': '',
            'text': '',
        }
        if question == '[begin]':
            return self.welcome_response
        for record in self.corpus:
            if question in record['inputs']:
                response['intent'] = record['intent']
                response['text'] = random.choice(record['responses'])
                return response
        return self.fallback_response


if __name__ == '__main__':
    chatbot = Chatbot('corpus.json')
    response = chatbot.get_welcome()
    print("Agent: %s [%s]" % (response['text'], response['intent']))
    while True:
        question = input(" User: ")
        response = chatbot.chat(question)
        print("Agent: %s [%s]" % (response['text'], response['intent']))
