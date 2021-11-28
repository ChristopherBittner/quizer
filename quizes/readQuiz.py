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

animals = []
with open(CONF) as f:
    data = json.load(f)
    animals = data['GlossList']


def getRandomPrefix(prefixes):
    if len(prefixes) > 0:
        return prefixes[random.randint(0, len(prefixes) - 1)]["Prefix"]


def createAQuestion(questionType, animal):
    if questionType == 0:
        return animal["ID"]
    else:
        return getRandomPhotoOf(getRandomPrefix(animal["Prefixes"]))


def createOptions(questionType, animal, amount=3):
    options = list()
    for i in range(amount):
        optionAnimal = getRandomAnimal()
        while optionAnimal is animal:
            optionAnimal = getRandomAnimal()
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


def getRandomAnimal():
    return animals[random.randint(0, len(animals) - 1)]


def getAnimal(animalName):
    for a in animals:
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
        questionAnimal = getRandomAnimal()
        question = createAQuestion(questionType, questionAnimal)
        optionCandidates = createOptions(questionType, questionAnimal, amount=questionOptions - 1)
        options = list()
        correctAdded = False
        for i in range(len(optionCandidates) + 1):
            if random.randint(0, 1) == 0 and not correctAdded:
                correctAdded = True
                quiz["answers"].append(i)
                if questionType == 1:
                    options.append(questionAnimal["ID"])
                else:
                    options.append(getRandomPhotoOf(getRandomPrefix(questionAnimal["Prefixes"])))
            else:
                if len(optionCandidates) > 0:
                    options.append(optionCandidates.pop())
        if not correctAdded:
            quiz["answers"].append(questionOptions - 1)
            if questionType == 1:
                options.append(questionAnimal["ID"])
            else:
                options.append(getRandomPhotoOf(getRandomPrefix(questionAnimal["Prefixes"])))

        quiz["animals"].append(questionAnimal)
        quiz["questions"].append(question)
        quiz["options"].append(options)

    return quiz


def createCatalog():
    for animal in animals:
        for i, prefix in enumerate(animal['Prefixes']):
            animal['Prefixes'][i]["Photos"] = getAllPhotosOf(prefix["Prefix"])
    return animals
