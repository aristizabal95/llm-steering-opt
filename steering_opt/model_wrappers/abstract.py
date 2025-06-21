from abc import abstractmethod, ABC 

class ModelWrapper(ABC):
    def __init__(self, model):
        self.model = model

    @property
    @abstractmethod
    def layers(self):
        """
        The layers of the model.
        """
        pass
    
    @property
    @abstractmethod
    def d_model(self):
        """
        The dimension of the model.
        """
        pass