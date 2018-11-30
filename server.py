import json
import bottle

from chatbot import Chatbot


class Server(bottle.Bottle):

    def __init__(self):
        super(Server, self).__init__()
        self.chatbot = Chatbot('corpus.json')
        self.route('/', method='GET', callback=self.index)
        self.route('/chat', method='POST', callback=self.chat)
        self.route('/<path:path>', method='GET', callback=self.static)

    def static(self, path):
        return bottle.static_file(path, './static')

    def index(self):
        return bottle.template('index.html')

    def chat(self):
        data = bottle.request.json
        response = self.chatbot.chat(data['text'])
        return json.dumps(response)


if __name__ == '__main__':
    Server().run(host='127.0.0.1', port=8080)
