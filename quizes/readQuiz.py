import glob
import json
import random
import os
from PIL import ImageTk, Image

QUIZ = "huntingLicenceAnimalRecognition"
CONF = f"{QUIZ}/conf.json"
PIX_PATH = f"{QUIZ}/pix"

pixesList = glob.glob(f"{PIX_PATH}/*.bmp")
pixesList.extend(glob.glob(f"{PIX_PATH}/*.jpg"))

entries = []
with open(CONF) as f:
    data = json.load(f)
    entries = data['GlossList']


def getRandomPrefix(prefixes):
    if len(prefixes) > 0:
        return prefixes[random.randint(0, len(prefixes) - 1)]["Prefix"]


def createAQuestion(questionType, animal):
    if questionType == 0:
        return animal["ID"]
    else:
        return getRandomPhotoOf(getRandomPrefix(animal["Prefixes"]))


def breakStringIntoWords(inputStr: str):
    inputStr.replace("/", " ")
    return inputStr.split(" ")


def createListOfEntriesThatFollowTheKeyWords(keyWords):
    limitedEntries = list()
    for entry in entries:
        entryKeyWords = list()
        entryKeyWords.extend(breakStringIntoWords(entry["ID"]))
        for p in entry["Prefixes"]:
            entryKeyWords.extend(breakStringIntoWords(p["Type"]))
        match = False
        for kw in keyWords:
            if match: break
            for ew in entryKeyWords:
                if match: break
                if kw == ew:
                    limitedEntries.append(entry)
                    match = True
    return limitedEntries


def createOptions(questionType, entry, amount=3):
    options = list()

    # Create list of words that represents the animal
    keyWords = list()
    keyWords.extend(breakStringIntoWords(entry["ID"]))
    for p in entry["Prefixes"]:
        keyWords.extend(breakStringIntoWords(p["Type"]))

    limitedEntries = createListOfEntriesThatFollowTheKeyWords(keyWords)

    for i in range(amount):
        # Try finding entry that has similar ID or prefix
        optionAnimal = getRandomEntry(tmpEntries=limitedEntries)
        # Repeat if same entry was found
        if optionAnimal is entry:
            optionAnimal = getRandomEntry(tmpEntries=limitedEntries)
        # If cant find try random entry from whole pool
        # Repeat also if the option is already in pool
        while optionAnimal is entry or optionAnimal is None or optionAnimal["ID"] in options:
            optionAnimal = getRandomEntry()
        # Finally add either the name of the photo to the options
        if questionType == 1:
            options.append(optionAnimal["ID"])
        else:
            options.append(getRandomPhotoOf(getRandomPrefix(optionAnimal["Prefixes"])))
    return options


def getPhoto(path, xSize=400, ySize=400):
    ph = Image.open(path)
    ph = ph.resize((xSize, ySize))
    return ImageTk.PhotoImage(ph)


def getAllPhotosOf(selectedPrefix):
    selections = []
    for p in pixesList:
        if os.path.basename(p).startswith(f"{selectedPrefix}_"):
            selections.append(getPhoto(p, 200, 200))
    return selections


def getRandomPhotoOf(selectedPrefix):
    selections = []
    for p in pixesList:
        if os.path.basename(p).startswith(f"{selectedPrefix}_"):
            selections.append(p)
    return getPhoto(selections[random.randint(0, len(selections) - 1)])


def getRandomEntry(tmpEntries=None):
    if tmpEntries and len(tmpEntries) > 0:
        return tmpEntries[random.randint(0, len(tmpEntries) - 1)]
    else:
        return entries[random.randint(0, len(entries) - 1)]


def getAnimal(animalName):
    for a in entries:
        if a["ID"] == animalName:
            return a


def createQuiz(questionsAmount = 20, questionOptions=4):
    quiz = dict()
    quiz["animals"] = list()
    quiz["questions"] = list()
    quiz["options"] = list()
    quiz["answers"] = list()
    for i in range(questionsAmount):
        questionType = random.randint(0, 1)
        questionAnimal = getRandomEntry()
        question = createAQuestion(questionType, questionAnimal)
        optionCandidates = createOptions(questionType, questionAnimal, amount=questionOptions - 1)
        options = list()
        correctToAddAt = random.randint(0, questionOptions - 1)
        for i in range(len(optionCandidates) + 1):
            if i == correctToAddAt:
                quiz["answers"].append(i)
                if questionType == 1:
                    options.append(questionAnimal["ID"])
                else:
                    options.append(getRandomPhotoOf(getRandomPrefix(questionAnimal["Prefixes"])))
            else:
                if len(optionCandidates) > 0:
                    options.append(optionCandidates.pop())

        quiz["animals"].append(questionAnimal)
        quiz["questions"].append(question)
        quiz["options"].append(options)

    return quiz


def createCatalog():
    for animal in entries:
        for i, prefix in enumerate(animal['Prefixes']):
            animal['Prefixes'][i]["Photos"] = getAllPhotosOf(prefix["Prefix"])
    return entries
