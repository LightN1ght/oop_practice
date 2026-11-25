class LoggingMixin:
    def __init__(self):
        super().__init__()
        print(repr(self))
