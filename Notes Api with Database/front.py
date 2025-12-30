import requests

baseurl = "http://127.0.0.1:8000"
urlp = f"{baseurl}/postNotes"
urlg = f"{baseurl}/getNotes"
urlpad = f"{baseurl}/getPads"
urlDelN = f"{baseurl}/delNote"
urlmakePad = f"{baseurl}/makePad"
urldelPad = f"{baseurl}/delPad"

padList = []


def __init__(name):
    padList.append = name


def makeNote(pad):
    note = input("Enter note:\n> ")
    try:
        re = requests.post(urlp, json={"note": note, "pad": pad})
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
    else:
        if re.ok:
            print("Saved")
        else:
            print("Error Not Saved")


def viewNote(pad):
    re = requests.get(urlg, params={"pad": pad})
    data = re.json()
    print()
    print("--------------------------------------")
    for note in data:
        print(note)


def viewNoteD(pad):
    re = requests.get(urlg, params={"pad": pad})
    data = re.json()
    print()
    noteObj = {}
    for i, note in enumerate(data):
        print(f"{i} - {note}")
        noteObj[i] = note
    return noteObj


def getPads():
    re = requests.get(urlpad)
    data = re.json()
    print(data)


def delNote(pad):
    noteObj = viewNoteD(pad)
    num = input("\npick number to del: ")
    note = noteObj[int(num)]
    re = requests.post(urlDelN, json={"pad": pad, "note": note})
    if re.ok:
        print("DELETED")
    else:
        print("something went wrong")


def makePad():
    name = input("New notepad Name: ")
    re = requests.post(urlmakePad, json={"name": name})
    if re.ok:
        print("Done")
    else:
        print(re)
        print("Something went wrong")


def delPad(name):
    re = requests.post(urldelPad, json={"name": name})
    if re.ok:
        print("Done")
    else:
        print(re)
        print("Something went wrong")


while True:
    print()
    getPads()
    pad = input("Pick a notpad: ")
    while True:
        print("--------------------------------------")
        print(
            "\n1. Make Note\n2.View Notes\n3.Delete Note\n4.New notepad\n5. Delete notepad\nQ. Quit"
        )
        action = input("> ")
        match action:
            case "1":
                makeNote(pad)
            case "2":
                viewNote(pad)
            case "3":
                delNote(pad)
            case "4":
                makePad()
            case "5":
                delPad(pad)
                break
            case "q" | "Q":
                break

    break
