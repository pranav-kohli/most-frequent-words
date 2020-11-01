from document_readers.document_reader_interface import DocumentReaderInterface


class TextFileReader(DocumentReaderInterface):

    def __init__(self, file_list: list):
        self.file_list = file_list

    def parse_as_string(self) -> dict:
        file_text = {}
        for file in self.file_list:
            # open and read each file as text
            with open(file, mode="r", encoding="utf8") as f:
                text = f.read()
                file_text[file] = text
        return file_text
