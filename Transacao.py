from abc import ABC, abstractproperty, abstractclassmethod
from Conta import Conta


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self) -> float:
        pass

    @abstractclassmethod
    def registrar(self, conta: Conta):
        pass
