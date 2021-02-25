import PySimpleGUI as sg

import os

import core


def tabGroup():
    """
    generates a tabGroup that holds Tabs names after modules holding the problems for that module

    Returns
    -------
    tabGroupLayout : List
        The tabgroup holding tabs and listboxes for each assignment.
    """

    moduleDict = getAllProblems()
    layout = []
    i = 0
    for moduleName in moduleDict.keys():
        i += 1
        listboxLayout = []
        for item in moduleDict[moduleName]:
            listboxLayout.append(item)

        moduleName = moduleName.split(" [")

        layout.append( sg.Tab( moduleName[0], [ [ sg.Listbox( listboxLayout,
                key=f"-PROBLEM-{i}-", size=(40,22),) ] ], pad=(0, 20) ) )

    return [ [ sg.TabGroup( [layout] ) ] ]


def getAllProblems():
    """
    returns a dictionary of all the assignments linked to the module as akey

    :return assignments_list: the list of all the assignments
    """
    savePath = core.dirCheck(f"{os.getcwd()}/.save_data")
    if not os.path.exists(savePath + "/data_modules/.modules.txt"):
        core.populateSaveData.populateTopics()
        core.populateSaveData.populateProblems()

    lmsModulesGrep = core.grepCall("-i", " \[", f"{savePath}/data_modules/.modules.txt")
    (lmsModulesData, err) = core.systemCallComms(lmsModulesGrep)

    lmsModulesData = lmsModulesData.replace("\n", " (").replace(')', '')
    lmsModulesData = lmsModulesData.split(" (")

    modulesList = [ item for item in lmsModulesData[0::2] if item != '']

    modulesProblemsDict = {}
    for topicName in modulesList:
        savePath = f"{os.getcwd()}/.save_data/data_topics"
        lmsTopicsGrep = core.grepCall("-i", " \[", f"{savePath}/{topicName}.txt")
        (lmsTopicsData, err) = core.systemCallComms(lmsTopicsGrep)
        if lmsTopicsData == "": continue

        lmsTopicsData = lmsTopicsData.replace("\n", " (").replace(')', '')
        lmsTopicsdata = lmsTopicsData.split(" (")
        topicsList = [ item for item in lmsTopicsData[0::2] if item != '']

        savePath = f"{os.getcwd()}/.save_data/data_problems"
        problemsList = []
        for problemName in topicsList:
            lmsProblemsGrep = core.grepCall("-i", " \[", f"{savePath}/{problemName}.txt")
            (lmsProblemsData, err) = core.systemCallComms(lmsProblemsGrep)
            if lmsProblemsData == "": continue

            lmsProblemsData = lmsProblemsData.replace("\n", " (").replace(')', '')
            lmsProblemsData = lmsProblemsData.split(" (")

            for item in lmsProblemsData[0::2]:
                if item != "" and item != "Coding Clinic Booking System [In Progress]":
                    problemsList.append(item)
        modulesProblemsDict[f"{topic_name}"] = problemsList

    return modulesProblemsDict
