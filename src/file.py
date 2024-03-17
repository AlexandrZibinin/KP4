from abc import ABC, abstractmethod

class File(ABC):
    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def del_data(self):
        pass


class JSONsaver(File):

    def save_data(self):
        pass

    def get_data(self):
        pass

    def del_data(self):
        pass

