from brain import think

class AIEngine:

    def __init__(self, name):

        self.name = name

    def process(self, question):

        return think(question, self.name)
