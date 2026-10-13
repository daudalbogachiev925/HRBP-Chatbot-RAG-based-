class ChatSession:
    def __init__(self, bot):
        self.bot = bot
        self.history = []

    def ask(self, query):
        response = self.bot.answer(query)
        self.history.append({"q": query, "a": response})
        return response
