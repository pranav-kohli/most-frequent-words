from abc import ABCMeta


class DocumentReaderInterface(metaclass=ABCMeta):
    """
    Interface for document reader. Subsequent implementations like text reader, pdf reader would implement this
    """

    def parse_as_string(self):
        raise NotImplementedError
