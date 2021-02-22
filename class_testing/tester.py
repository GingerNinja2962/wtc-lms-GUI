#!/usr/bin/python3
import PySimpleGUI as sg

# import core.populateSaveData
# import core

def main():
    """
    The main entry point for the lms GUI application.
    """
    item = core.populateSaveData.dataHandelerClass()
    item.getModules()
    print(item.modulesList)

if __name__ == "__main__":
    main()
