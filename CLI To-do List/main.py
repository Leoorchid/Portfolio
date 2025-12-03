import json
import os

fileName = "task.json"
try:
    with open(fileName, "r") as f:
        taskDict = {int(key): value for key, value in json.load(f).items()}
except json.decoder.JSONDecodeError:
    taskDict = {}


print("[Todo List]")


while True:
    action = input("\n1. Add Task\n2. List Task\n3. Delete a Task\nQ. Quit\n>")
    match action:
        case "1":
            print(f"\n[Adding Task]\n")
            task = input("\n>")
            taskDict[len(taskDict) + 1] = task
            with open(fileName, "w") as f:
                json.dump(taskDict, f)
        case "2":
            print("\n[Task List]\n")
            if taskDict != {}:
                for i, task in taskDict.items():
                    print(f"{i}. {task}")
            else:
                print("Nothing TODO!!!")

        case "3":
            print("\n[Delete Task]\n")
            for i, task in taskDict.items():
                print(f"{i}. {task}")

            choice = input("\nSelect which to Delete(Q to exit)")

            sure = input(f"You are deleting ({taskDict[int(choice)]}) | (y/n)")

            if sure in ("y,Y"):
                tempDict = {}

                del taskDict[int(choice)]

                for i, task in enumerate(taskDict.values()):

                    tempDict[i + 1] = task

                taskDict = tempDict
                with open(fileName, "w") as f:
                    json.dump(taskDict, f)
                print("Deleted")

            else:
                print("Saved")

        case "Q" | "q":
            break

        case _:
            print("Please enter (1,2,3, or (Q,q))")
