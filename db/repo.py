import abc

class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_lexicon(self) -> list:
        raise NotImplementedError

    def dev_gloss(self):
        raise NotImplementedError

    def dev_query(self, query: str):
        raise NotImplementedError

    def eng_query(self, query: str):
        raise NotImplementedError

    def eng_gloss(self):
        raise NotImplementedError

    def story_query(self, query: str):
        raise NotImplementedError
