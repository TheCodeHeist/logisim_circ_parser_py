import json


if __name__ == "__main__":
    print("This file is not meant to be run directly. Please run main.py instead.")
    exit(1)

visitedNodes = []


def convertDictArrayToDict(dictArray):
    outDict = {}
    for item in dictArray:
        if item["val"] == "true":
            outDict[item["name"]] = True
        elif item["val"] == "false":
            outDict[item["name"]] = False
        else:
            outDict[item["name"]] = item["val"]
    return outDict


def convertDictCoordStringToArr(refDict):
    outDict = {}
    for item in refDict:
        if item == "loc" or item == "from" or item == "to":
            outDict[item] = refDict[item][1:(
                len(refDict[item]) - 1)].split(",")
            outDict[item][0] = int(outDict[item][0])
            outDict[item][1] = int(outDict[item][1])
        else:
            outDict[item] = refDict[item]

    return outDict


def calculateAllInputCoords(comp):
    inputCoords = []

    if comp["name"] == "AND Gate" or comp["name"] == "OR Gate":
        if "facing" not in comp["attributes"]:
            if "inputs" not in comp["attributes"]:
                inputCoords.append(
                    [comp["loc"][0] - 30, comp["loc"][1] - 10])
                inputCoords.append(
                    [comp["loc"][0] - 30, comp["loc"][1] + 10])
            elif comp["attributes"]["inputs"] % 2 == 0:
                for i in range(int(comp["attributes"]["inputs"] / 2)):
                    inputCoords.append(
                        [comp["loc"][0] - 30, comp["loc"][1] - (10 * (i + 1))])
                    inputCoords.append(
                        [comp["loc"][0] - 30, comp["loc"][1] + (10 * (i + 1))])
            else:
                inputCoords.append(
                    [comp["loc"][0] - 30, comp["loc"][1]])
                for i in range(int((comp["attributes"]["inputs"] - 1) / 2)):
                    inputCoords.append(
                        [comp["loc"][0] - 30, comp["loc"][1] - (10 * (i + 1))])
                    inputCoords.append(
                        [comp["loc"][0] - 30, comp["loc"][1] + (10 * (i + 1))])

        elif comp["attributes"]["facing"] == "west":
            if "inputs" not in comp["attributes"]:
                inputCoords.append(
                    [comp["loc"][0] + 30, comp["loc"][1] - 10])
                inputCoords.append(
                    [comp["loc"][0] + 30, comp["loc"][1] + 10])
            elif comp["attributes"]["inputs"] % 2 == 0:
                for i in range(int(comp["attributes"]["inputs"] / 2)):
                    inputCoords.append(
                        [comp["loc"][0] + 30, comp["loc"][1] - (10 * (i + 1))])
                    inputCoords.append(
                        [comp["loc"][0] + 30, comp["loc"][1] + (10 * (i + 1))])
            else:
                inputCoords.append(
                    [comp["loc"][0] + 30, comp["loc"][1]])
                for i in range(int((comp["attributes"]["inputs"] - 1) / 2)):
                    inputCoords.append(
                        [comp["loc"][0] + 30, comp["loc"][1] - (10 * (i + 1))])
                    inputCoords.append(
                        [comp["loc"][0] + 30, comp["loc"][1] + (10 * (i + 1))])

        elif comp["attributes"]["facing"] == "north":
            if "inputs" not in comp["attributes"]:
                inputCoords.append(
                    [comp["loc"][0] - 10, comp["loc"][1] + 30])
                inputCoords.append(
                    [comp["loc"][0] + 10, comp["loc"][1] + 30])
            elif comp["attributes"]["inputs"] % 2 == 0:
                for i in range(int(comp["attributes"]["inputs"] / 2)):
                    inputCoords.append(
                        [comp["loc"][0] - (10 * (i + 1)), comp["loc"][1] + 30])
                    inputCoords.append(
                        [comp["loc"][0] + (10 * (i + 1)), comp["loc"][1] + 30])
            else:
                inputCoords.append(
                    [comp["loc"][0], comp["loc"][1] + 30])
                for i in range(int((comp["attributes"]["inputs"] - 1) / 2)):
                    inputCoords.append(
                        [comp["loc"][0] - (10 * (i + 1)), comp["loc"][1] + 30])
                    inputCoords.append(
                        [comp["loc"][0] + (10 * (i + 1)), comp["loc"][1] + 30])

        elif comp["attributes"]["facing"] == "south":
            if "inputs" not in comp["attributes"]:
                inputCoords.append(
                    [comp["loc"][0] - 10, comp["loc"][1] - 30])
                inputCoords.append(
                    [comp["loc"][0] + 10, comp["loc"][1] - 30])
            elif comp["attributes"]["inputs"] % 2 == 0:
                for i in range(int(comp["attributes"]["inputs"] / 2)):
                    inputCoords.append(
                        [comp["loc"][0] - (10 * (i + 1)), comp["loc"][1] - 30])
                    inputCoords.append(
                        [comp["loc"][0] + (10 * (i + 1)), comp["loc"][1] - 30])
            else:
                inputCoords.append(
                    [comp["loc"][0], comp["loc"][1] - 30])
                for i in range(int((comp["attributes"]["inputs"] - 1) / 2)):
                    inputCoords.append(
                        [comp["loc"][0] - (10 * (i + 1)), comp["loc"][1] - 30])
                    inputCoords.append(
                        [comp["loc"][0] + (10 * (i + 1)), comp["loc"][1] - 30])

    elif comp["name"] == "NAND Gate" or comp["name"] == "NOR Gate" or comp["name"] == "XOR Gate":
        if "facing" not in comp["attributes"]:
            if "inputs" not in comp["attributes"]:
                inputCoords.append(
                    [comp["loc"][0] - 40, comp["loc"][1] - 10])
                inputCoords.append(
                    [comp["loc"][0] - 40, comp["loc"][1] + 10])
            elif comp["attributes"]["inputs"] % 2 == 0:
                for i in range(int(comp["attributes"]["inputs"] / 2)):
                    inputCoords.append(
                        [comp["loc"][0] - 40, comp["loc"][1] - (10 * (i + 1))])
                    inputCoords.append(
                        [comp["loc"][0] - 40, comp["loc"][1] + (10 * (i + 1))])
            else:
                inputCoords.append(
                    [comp["loc"][0] - 40, comp["loc"][1]])
                for i in range(int((comp["attributes"]["inputs"] - 1) / 2)):
                    inputCoords.append(
                        [comp["loc"][0] - 40, comp["loc"][1] - (10 * (i + 1))])
                    inputCoords.append(
                        [comp["loc"][0] - 40, comp["loc"][1] + (10 * (i + 1))])

        elif comp["attributes"]["facing"] == "west":
            if "inputs" not in comp["attributes"]:
                inputCoords.append(
                    [comp["loc"][0] + 40, comp["loc"][1] - 10])
                inputCoords.append(
                    [comp["loc"][0] + 40, comp["loc"][1] + 10])
            elif comp["attributes"]["inputs"] % 2 == 0:
                for i in range(int(comp["attributes"]["inputs"] / 2)):
                    inputCoords.append(
                        [comp["loc"][0] + 40, comp["loc"][1] - (10 * (i + 1))])
                    inputCoords.append(
                        [comp["loc"][0] + 40, comp["loc"][1] + (10 * (i + 1))])
            else:
                inputCoords.append(
                    [comp["loc"][0] + 40, comp["loc"][1]])
                for i in range(int((comp["attributes"]["inputs"] - 1) / 2)):
                    inputCoords.append(
                        [comp["loc"][0] + 40, comp["loc"][1] - (10 * (i + 1))])
                    inputCoords.append(
                        [comp["loc"][0] + 40, comp["loc"][1] + (10 * (i + 1))])

        elif comp["attributes"]["facing"] == "north":
            if "inputs" not in comp["attributes"]:
                inputCoords.append(
                    [comp["loc"][0] - 10, comp["loc"][1] + 40])
                inputCoords.append(
                    [comp["loc"][0] + 10, comp["loc"][1] + 40])
            elif comp["attributes"]["inputs"] % 2 == 0:
                for i in range(int(comp["attributes"]["inputs"] / 2)):
                    inputCoords.append(
                        [comp["loc"][0] - (10 * (i + 1)), comp["loc"][1] + 40])
                    inputCoords.append(
                        [comp["loc"][0] + (10 * (i + 1)), comp["loc"][1] + 40])
            else:
                inputCoords.append(
                    [comp["loc"][0], comp["loc"][1] + 40])
                for i in range(int((comp["attributes"]["inputs"] - 1) / 2)):
                    inputCoords.append(
                        [comp["loc"][0] - (10 * (i + 1)), comp["loc"][1] + 40])
                    inputCoords.append(
                        [comp["loc"][0] + (10 * (i + 1)), comp["loc"][1] + 40])

        elif comp["attributes"]["facing"] == "south":
            if "inputs" not in comp["attributes"]:
                inputCoords.append(
                    [comp["loc"][0] - 10, comp["loc"][1] - 40])
                inputCoords.append(
                    [comp["loc"][0] + 10, comp["loc"][1] - 40])
            elif comp["attributes"]["inputs"] % 2 == 0:
                for i in range(int(comp["attributes"]["inputs"] / 2)):
                    inputCoords.append(
                        [comp["loc"][0] - (10 * (i + 1)), comp["loc"][1] - 40])
                    inputCoords.append(
                        [comp["loc"][0] + (10 * (i + 1)), comp["loc"][1] - 40])
            else:
                inputCoords.append(
                    [comp["loc"][0], comp["loc"][1] - 40])
                for i in range(int((comp["attributes"]["inputs"] - 1) / 2)):
                    inputCoords.append(
                        [comp["loc"][0] - (10 * (i + 1)), comp["loc"][1] - 40])
                    inputCoords.append(
                        [comp["loc"][0] + (10 * (i + 1)), comp["loc"][1] - 40])

    elif comp["name"] == "XNOR Gate":
        if "facing" not in comp["attributes"]:
            if "inputs" not in comp["attributes"]:
                inputCoords.append(
                    [comp["loc"][0] - 50, comp["loc"][1] - 10])
                inputCoords.append(
                    [comp["loc"][0] - 50, comp["loc"][1] + 10])
            elif comp["attributes"]["inputs"] % 2 == 0:
                for i in range(int(comp["attributes"]["inputs"] / 2)):
                    inputCoords.append(
                        [comp["loc"][0] - 50, comp["loc"][1] - (10 * (i + 1))])
                    inputCoords.append(
                        [comp["loc"][0] - 50, comp["loc"][1] + (10 * (i + 1))])
            else:
                inputCoords.append(
                    [comp["loc"][0] - 50, comp["loc"][1]])
                for i in range(int((comp["attributes"]["inputs"] - 1) / 2)):
                    inputCoords.append(
                        [comp["loc"][0] - 50, comp["loc"][1] - (10 * (i + 1))])
                    inputCoords.append(
                        [comp["loc"][0] - 50, comp["loc"][1] + (10 * (i + 1))])

        elif comp["attributes"]["facing"] == "west":
            if "inputs" not in comp["attributes"]:
                inputCoords.append(
                    [comp["loc"][0] + 50, comp["loc"][1] - 10])
                inputCoords.append(
                    [comp["loc"][0] + 50, comp["loc"][1] + 10])
            elif comp["attributes"]["inputs"] % 2 == 0:
                for i in range(int(comp["attributes"]["inputs"] / 2)):
                    inputCoords.append(
                        [comp["loc"][0] + 50, comp["loc"][1] - (10 * (i + 1))])
                    inputCoords.append(
                        [comp["loc"][0] + 50, comp["loc"][1] + (10 * (i + 1))])
            else:
                inputCoords.append(
                    [comp["loc"][0] + 50, comp["loc"][1]])
                for i in range(int((comp["attributes"]["inputs"] - 1) / 2)):
                    inputCoords.append(
                        [comp["loc"][0] + 50, comp["loc"][1] - (10 * (i + 1))])
                    inputCoords.append(
                        [comp["loc"][0] + 50, comp["loc"][1] + (10 * (i + 1))])

        elif comp["attributes"]["facing"] == "north":
            if "inputs" not in comp["attributes"]:
                inputCoords.append(
                    [comp["loc"][0] - 10, comp["loc"][1] + 50])
                inputCoords.append(
                    [comp["loc"][0] + 10, comp["loc"][1] + 50])
            elif comp["attributes"]["inputs"] % 2 == 0:
                for i in range(int(comp["attributes"]["inputs"] / 2)):
                    inputCoords.append(
                        [comp["loc"][0] - (10 * (i + 1)), comp["loc"][1] + 50])
                    inputCoords.append(
                        [comp["loc"][0] + (10 * (i + 1)), comp["loc"][1] + 50])
            else:
                inputCoords.append(
                    [comp["loc"][0], comp["loc"][1] + 50])
                for i in range(int((comp["attributes"]["inputs"] - 1) / 2)):
                    inputCoords.append(
                        [comp["loc"][0] - (10 * (i + 1)), comp["loc"][1] + 50])
                    inputCoords.append(
                        [comp["loc"][0] + (10 * (i + 1)), comp["loc"][1] + 50])

        elif comp["attributes"]["facing"] == "south":
            if "inputs" not in comp["attributes"]:
                inputCoords.append(
                    [comp["loc"][0] - 10, comp["loc"][1] - 50])
                inputCoords.append(
                    [comp["loc"][0] + 10, comp["loc"][1] - 50])
            elif comp["attributes"]["inputs"] % 2 == 0:
                for i in range(int(comp["attributes"]["inputs"] / 2)):
                    inputCoords.append(
                        [comp["loc"][0] - (10 * (i + 1)), comp["loc"][1] - 50])
                    inputCoords.append(
                        [comp["loc"][0] + (10 * (i + 1)), comp["loc"][1] - 50])
            else:
                inputCoords.append(
                    [comp["loc"][0], comp["loc"][1] - 50])
                for i in range(int((comp["attributes"]["inputs"] - 1) / 2)):
                    inputCoords.append(
                        [comp["loc"][0] - (10 * (i + 1)), comp["loc"][1] - 50])
                    inputCoords.append(
                        [comp["loc"][0] + (10 * (i + 1)), comp["loc"][1] - 50])

    elif comp["name"] == "NOT Gate":
        if "facing" not in comp["attributes"]:
            inputCoords.append([comp["loc"][0] - 20, comp["loc"][1]])

        elif comp["attributes"]["facing"] == "west":
            inputCoords.append([comp["loc"][0] + 20, comp["loc"][1]])

        elif comp["attributes"]["facing"] == "north":
            inputCoords.append([comp["loc"][0], comp["loc"][1] + 20])

        elif comp["attributes"]["facing"] == "south":
            inputCoords.append([comp["loc"][0], comp["loc"][1] - 20])

    elif comp["name"] == "Pin":
        inputCoords.append(comp["loc"])

    return inputCoords


def mapCompLocationsToId(comps):
    locations: dict[str, str] = {}

    for comp in comps:
        inputCoords = calculateAllInputCoords(comp)

        for coord in inputCoords:
            locations[str(coord)] = str(comp["id"])

    return locations


def getTypeFromName(name):
    if name == "AND Gate":
        return "AND"
    elif name == "OR Gate":
        return "OR"
    elif name == "NAND Gate":
        return "NAND"
    elif name == "NOR Gate":
        return "NOR"
    elif name == "XOR Gate":
        return "XOR"
    elif name == "XNOR Gate":
        return "XNOR"
    elif name == "NOT Gate":
        return "NOT"
    elif name == "Pin":
        return "PIN"

    return "UNKNOWN"


def getNumInputs(comp):
    if "inputs" in comp["attributes"]:
        return int(comp["attributes"]["inputs"])
    elif comp["name"] == "NOT Gate":
        return 1
    elif comp["name"] == "Pin":
        return 1
    else:
        return 2


def addPreambleDefinitions(comps):
    output = ""

    for comp in comps:
        # Syntax: ;define <id> <type> <type = PIN ? (IN or OUT) : NONE> [no. of inputs] [name]

        output += ";define "
        output += comp["id"]
        output += " "
        output += getTypeFromName(comp["name"])
        output += " "
        if getTypeFromName(comp["name"]) == "PIN":
            if "output" in comp["attributes"]:
                output += "OUT "
            else:
                output += "IN "
        output += str(getNumInputs(comp))
        output += " \""
        output += comp["name"]
        output += "\"\n"

    return output


def mapWireLocationsByFrom(wires):
    wireMap = {}

    for wire in wires:
        if str(wire["from"]) not in wireMap:
            wireMap[str(wire["from"])] = [str(wire["to"])]
        else:
            wireMap[str(wire["from"])].append(str(wire["to"]))

        if str(wire["to"]) not in wireMap:
            wireMap[str(wire["to"])] = [str(wire["from"])]
        else:
            wireMap[str(wire["to"])].append(str(wire["from"]))

    return wireMap


def trackWireDestinations(module, compMap, wireMap, isModuleComponent=True):
    destinations = []

    if not isModuleComponent:
        # If the module is not a component, it is a wire
        routes = module

        for route in routes:
            if str(route) in visitedNodes:
                continue

            if str(route) in compMap:
                destinations.append(compMap[str(route)])
            elif str(route) in wireMap:
                visitedNodes.append(str(route))
                destinations += trackWireDestinations(
                    wireMap[str(route)], compMap, wireMap, False)
            else:
                Exception("Route not connected to anything!")

    else:
        # If the module is a component, it is a component
        if str(module["loc"]) in wireMap:
            visitedNodes.append(str(module["loc"]))
            destinations = trackWireDestinations(
                wireMap[str(module["loc"])], compMap, wireMap, False)
        else:
            Exception("Component not connected to a wire!")

    return destinations


def connectComponents(circuitData, compMap, wireMap):
    output = ""

    for comp in circuitData["components"]:
        destinations = trackWireDestinations(
            comp, compMap, wireMap)

        print(json.dumps(destinations, indent=2))

        for dest in destinations:
            output += ";attach "
            output += comp["id"]
            output += " "
            output += dest
            output += "\n"

    return output
