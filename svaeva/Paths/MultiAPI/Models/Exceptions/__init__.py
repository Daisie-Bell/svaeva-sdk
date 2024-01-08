
class InvalidSkeleton(Exception):
    def __init__(self, message):
        self.message = "The id ({}) of the skeleton is not present in Svaeva\n Help: https://github.com/Daisie-Bell/svaeva-sdk#skeletons".format(message)
        super().__init__(self.message)

class InvalidConfig(Exception):
    def __init__(self, message):
        self.message = "The id ({}) of the config is not present in Svaeva\n Help: https://github.com/Daisie-Bell/svaeva-sdk#configs".format(message)
        super().__init__(self.message)

class InvalidKey(Exception):
    def __init__(self, message):
        self.message = "The key ({}) of the skeleton is not present in Svaeva\n Help: https://github.com/Daisie-Bell/svaeva-sdk#wallets".format(message)
        super().__init__(self.message)