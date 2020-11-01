import glob
from constants.file_types import FileTypes


def determine_file_type(upload_dir):
    txt_file_list = glob.glob(upload_dir + '/*.txt')
    if txt_file_list:
        return FileTypes.Text
    pdf_file_list = glob.glob(upload_dir + '/*.pdf')
    if pdf_file_list:
        return FileTypes.Pdf
