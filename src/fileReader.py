__author__ = 'fsegovia'


class FileReader():
    """Reads files"""
    def __init__(self, fileName, options):
        self.file = open(fileName, options)

    def closeFile(self):
        self.file.close()

    def readLines(self):
        lines = self.file.readlines()
        self.closeFile()
        return lines

    def write(self,txtContent):
        self.file.write(txtContent)
