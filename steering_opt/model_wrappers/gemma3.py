from steering_opt.model_wrappers.abstract import ModelWrapper


class Gemma3Wrapper(ModelWrapper):
    def __init__(self, model):
        self.model = model

    @property
    def layers(self):
        return self.model.model.language_model.layers
    
    @property
    def d_model(self):
        return self.model.config.text_config.hidden_size