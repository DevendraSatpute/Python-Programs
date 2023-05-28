import argparse
import traceback
from _utils.logger import log_error, log_debug, log_info, log_warning, log_critical, create_log_file

def readFile():
    pass

def preprocessData():
    pass

def writeFile():
    pass

if __name__ == '__main__':
    file_format = ['csv', 'gzip', 'json', 'html', 'xml', 'parquet', 'avro']
    parser = argparse.ArgumentParser()
    parser.add_argument('-source_path', type=str, help='give source path')
    parser.add_argument('-destination_path', type=str, help='give destination path')
    args = parser.parse_args()
    log_file_path = create_log_file()
    import pdb; pdb.set_trace()

    """ This program can be used to read a files, preprocess the data as per your requirement and write
        same or different file format"""
