from os import close, dup, O_WRONLY, getcwd, path, write, open as osOpen
from datetime import datetime

class logger:
    """
    A class dedicated to loggin the stdout and stderr from the
    wtc-lms-GUI program.

    Attributes
    ----------
        err : file descriptor
            The file descriptor for stderr for this program.
        out : file descriptor
            The file descriptor for stdout for this program.
        errFile : string
            The file location to save the for stderr for this program.
        outFile : string
            The file location to save the stdout for this program.

    Methods
    -------
        open()
            Start redirecting all stdout and stderr to logger files
            for each.
        close()
            Restore the original stdout and stderr printing to
            termianl.
    """
    def __init__(self):
        """
        The constructor for the logger class, sets up the needed
        variables.
        """
        self.err = None
        self.out = None
        self.outFile = f"{getcwd()}/.outLogger.txt"
        self.errFile = f"{getcwd()}/.errLogger.txt"


    def open(self):
        """
        Start redirecting all stdout and stderr to logger files for
        each.
        """
        if not path.exists(self.outFile):
            open(self.outFile, 'w+').close()

        if not path.exists(self.errFile):
            open(self.errFile, 'w+').close()

        currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.out = dup(1)
        close(1)
        osOpen(self.outFile, O_WRONLY)
        write(1, b"Launch Time:\t" + str.encode(currentTime))

        self.err = dup(2)
        close(2)
        osOpen(self.errFile, O_WRONLY)
        write(2, b"Launch Time:\t" + str.encode(currentTime))


    def close(self):
        """
        Restore the original stdout and stderr printing to termianl.
        """
        close(1)
        dup(self.out)
        close(self.out)

        close(2)
        dup(self.err)
        close(self.err)
