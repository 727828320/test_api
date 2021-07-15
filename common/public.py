import os


def fileDir(data):
    base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, data)


def filePath(fileDir='data', fileName='data.xlsx'):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), fileDir, fileName)
