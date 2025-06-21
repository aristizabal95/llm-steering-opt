from model_wrappers.abstract import ModelWrapper


class DefaultModelWrapper(ModelWrapper):
    def __init__(self, model):
        self.model = model

    @property
    def layers(self):
        return self.model.model.layer
    
    @property
    def d_model(self):
        return self.model.config.hidden_size
