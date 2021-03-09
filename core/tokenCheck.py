from datetime import datetime, timedelta

import os

import core


class tokensClass():
    """
    The token managment class that handles all token related data.

    Attributes
    ----------
        tokenPath : str
            The path to the save data file.
        currentTime : str
            The current system time.
        status : bool
            The status of the last token check.

    Methods
    -------
        currentTimeUpdate()
            Update the current time variable saved in the tokens class.
        forceTokenUpdate(tokenType)
            Force the saved token to be refreshed.
        tokenCheck(tokenType)
            Check the status of the assignments token.

    """
    def __init__(self):
        """
        Constructs all the necessary attributes for the standard token objects.
        
        Parameters
        ----------
            tokenPath : str
                The path to the save data file.
            currentTime : str
                The current system time.
            status : bool
                The status of the last check on the token.
        """
        self.tokenPath = core.dirCheck(f"{os.getcwd()}/.save_data")
        self.tokenPath = core.dirCheck(f"{self.tokenPath}/tokens")
        self.currentTime = None
        self.status = False


    def currentTimeUpdate(self):
        """
        Sets the current time variable to the current system time.
        """
        self.currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def forceTokenUpdate(self, tokenType="Login"):
        """
        Force the saved token to be refreshed.

        Parameters
        ----------
        tokenType : str
            The type of token to check i.e. 'Assignment' or 'Review',
            by default "Login".
        """
        self.currentTimeUpdate()
        localTokenPath = f"{self.tokenPath}/.token{tokenType}.txt"
        core.writeToFile(self.currentTime, localTokenPath)
        self.status = False


    def tokenCheck(self, tokenType="Login"):
        """
        Check the status of the specified token.

        Parameters
        ----------
        tokenType : str
            The type of token to check i.e. 'Assignment' or 'Review',
            by default "Login".

        Returns
        -------
        tokenStatus : bool
            The status of the check. True if valid, False if invalid.
        """
        self.currentTimeUpdate()
        localTokenPath = self.tokenPath + f"/.token{tokenType}.txt"
        try:
            tokenData = core.readFromFile(localTokenPath)
            tokenData = datetime.strptime(
                    tokenData, "%Y-%m-%d %H:%M:%S")
        except:
            core.writeToFile(self.currentTime, localTokenPath)
            self.status = False
            return self.status

        if (tokenData + timedelta(weeks=1)) < datetime.strptime(
                    self.currentTime, "%Y-%m-%d %H:%M:%S"):
            core.writeToFile(self.currentTime, localTokenPath)
            self.status = False
            return self.status

        self.status = True
        return self.status
