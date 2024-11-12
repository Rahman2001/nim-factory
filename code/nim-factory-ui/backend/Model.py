class Model:
    def __init__(self):
        self.family: str = ""
        self.version: str = ""
        self.type: str | None = None

    def get_dict(self):
        return {"family": self.family, "version": self.version, "type": self.type}
