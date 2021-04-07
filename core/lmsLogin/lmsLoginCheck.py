import PySimpleGUI as sg

from os import path
from os import sys
from sys import argv

from core import systemCallClose, grepSystemCall, lmsCall, systemCallComms
from core import dirCheck, writeToFile

from classTemplates import baseWindowClass


class manageLogin(baseWindowClass):
    """
    A class to create a wtc-lms login or server error window.

    Methods
    -------
        lmsLoginCheck()
            Check if the user is logged into lms using the respons
            from lms.
    """
    def __init__(self):
        """
        The constructor for manageLogin.
        """
        super().__init__()
        self.size = (400, 110)
        self.location = (500, 300)


    def run(self):
        status = self.lmsLoginCheck()
        if status == "passed": return True

        if status == "login":
            self.title = "wtc-lms login required"
            self.layout = [
                [ sg.Text(f"\n\nPlease login on wtc-lms commandline tool.") ],
                [ sg.Button("Retry"), sg.Button("Cancel") ] ]

        if status == "server error":
            self.title = "wtc-lms server error"
            self.layout = [
                [ sg.Text(f"\nCould not connect to the wtc-lms server.") ],
                [ sg.Text(
                    f"The server might be down for maintance or your lms") ],
                [ sg.Text(f"configuration file might have some issues.") ],
                [ sg.Button("Retry"), sg.Button("Cancel") ] ]

        if status == "internet error":
            self.title = "wtc-lms connection error"
            self.layout = [
                [ sg.Text(f"\nCould not connect to the wtc-lms server.") ],
                [ sg.Text("Your internet might be offline or the servers") ],
                [ sg.Text("might be down for maintance or your lms") ],
                [ sg.Text(f"configuration file might have some issues.") ],
                [ sg.Button("Retry"), sg.Button("Cancel") ] ]


        self.window = sg.Window(self.title, self.layout,
                element_justification=self.elementJustification,
                location=self.location, size=(400, 130)).finalize()

        while self.running:
            canceledStatus = self.read()
        return canceledStatus


    def read(self):
        self.event, self.values = self.window.read(timeout=600000)

        if self.lmsLoginCheck() == "passed":
            self.close()
            return True

        elif self.event == "Retry":
            if self.lmsLoginCheck() == "passed":
                self.close()
                return True

        elif self.event in (sg.WIN_CLOSED, "Cancel"):
            self.close()
            return False


    def lmsLoginCheck(self):
        """
        Check if the user is logged into lms using the respons from
        lms.
        """
        modulesDataPath = dirCheck(
            f"{dirCheck(f'{path.dirname(argv[0])}/.save_data')}/modulesData")

        modulesDataProcess = lmsCall("modules")
        loginGrepProcess = grepSystemCall("-i","Token expired",
            modulesDataProcess)
        systemCallClose(modulesDataProcess)
        (lmsLoginData, loginErr) = systemCallComms(loginGrepProcess)

        secondModulesDataProcess = lmsCall("modules")
        traceGrepProcess = grepSystemCall("-i","thread 'main' panicked",
            secondModulesDataProcess)
        systemCallClose(secondModulesDataProcess)
        (lmsTraceData, traceErr) = systemCallComms(traceGrepProcess)

        modulesProcess = lmsCall("modules")
        (moduleData, moduleErr) = systemCallComms(modulesProcess)

        if lmsLoginData != "":
            return "login"
        if lmsTraceData != "":
            return "server error"
        if lmsLoginData == "" and lmsTraceData == "" and moduleData == "":
            return "internet error"
        return "passed"