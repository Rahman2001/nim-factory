from backend.Model import Model


class Environment:
    def __init__(self):
        self.model: Model = Model()
        self.huggingface: dict | None = None

    def get_json(self):
        return {"huggingface": self.huggingface, "model": self.model.get_dict()}
