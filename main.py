import defusedxml.ElementTree as ET
from xml.etree.ElementTree import ElementTree
import json
import methods


def writeJsonFile():
    outJson = {
        "components": [],
        "wires": []
    }

    circTree: ElementTree = ET.parse("test.circ")
    circProject = circTree.getroot()
    circCircuit = circProject.find("circuit")

    compCount = 0

    for child in circCircuit:
        if child.tag == "comp":
            comp = methods.convertDictCoordStringToArr(child.attrib)
            attrs = []
            for attr in child.findall("a"):
                attrs.append(attr.attrib)
            comp["attributes"] = methods.convertDictArrayToDict(attrs)
            if "inputs" in comp["attributes"]:
                comp["attributes"]["inputs"] = int(
                    comp["attributes"]["inputs"])
            comp["id"] = "comp" + str(compCount)

            outJson["components"].append(comp)
            compCount += 1

        elif child.tag == "wire":
            wire = methods.convertDictCoordStringToArr(child.attrib)
            attrs = []
            for attr in child.findall("a"):
                attrs.append(attr.attrib)
            wire["attributes"] = methods.convertDictArrayToDict(attrs)
            outJson["wires"].append(wire)

    with open("test.json", "w") as outFile:
        outFile.write(json.dumps(outJson, indent=2))

    print("JSON file written!")

    return outJson


def writeLogicFile(circuitData: dict[str, list]):
    compMap = methods.mapCompLocationsToId(circuitData["components"])
    wireMap = methods.mapWireLocationsByFrom(circuitData["wires"])

    output = ""

    output += methods.addPreambleDefinitions(circuitData["components"])
    output += "\n"
    output += methods.connectComponents(circuitData, compMap, wireMap)

    with open("test.logic", "w") as outFile:
        outFile.write(output)


if __name__ == "__main__":
    circuitData = writeJsonFile()
    writeLogicFile(circuitData)
