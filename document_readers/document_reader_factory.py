from document_readers.text_file_reader import TextFileReader
from constants.file_types import FileTypes


class DocumentReaderFactory:
    """
    Factory class to instantiate different types of readers
    """

    def __init__(self):
        self._instances = {}
        self.add_handler(TextFileReader, FileTypes.Text)

    def add_handler(self, file_reader, file_type):
        self._instances[file_type] = file_reader

    def get_handler(self, file_type):
        try:
            return self._instances[file_type]
        except KeyError:
            return
