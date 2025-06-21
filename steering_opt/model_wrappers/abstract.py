class ModelWrapper:
    def __init__(self, model):
        self.model = model

    @abstractmethod
    @property
    def layers(self):
        """
        The layers of the model.
        """
        pass
    
    @abstractmethod
    @property
    def d_model(self):
        """
        The dimension of the model.
        """
        pass