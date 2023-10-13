

class ClientException(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ProviderError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

