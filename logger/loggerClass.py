from os import close, dup, O_WRONLY, getcwd, path, open as osOpen

class logger:
    def __init__(self):
        self.Err = None
        self.Out = None
        self.outFile = f"{getcwd()}/.outLogger.txt"
        self.errFile = f"{getcwd()}/.errLogger.txt"


    def open(self):
        if not path.exists(self.outFile):
            open(self.outFile, 'w+').close()

        if not path.exists(self.errFile):
            open(self.errFile, 'w+').close()

        self.Out = dup(1)
        close(1)
        osOpen(self.outFile, O_WRONLY)

        self.Err = dup(2)
        close(2)
        osOpen(self.errFile, O_WRONLY)


    def close(self):
        close(1)
        dup(self.Out)
        close(self.Out)

        close(2)
        dup(self.Err)
        close(self.Err)
