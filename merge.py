import os
import fnmatch
import logging
import json
from argparse import ArgumentParser

version = "0.0.1"
parser = ArgumentParser(prog="lab1", description="Laboratory work 1.", epilog="Приятного пользования!")
parser.add_argument("-v", "--version", action="version", version=version)
parser.add_argument("--debug", action="store_true", help="enable debug mode")
parser.add_argument("--root", help="Принимает папку для обработки")
parser.add_argument('output', help="выходной файл")  # positional argument
args = parser.parse_args()
defaultPath = os.path.dirname(__file__)+"\ROOT"
outputFile = "output.json"

logger = logging.getLogger()
logger.name = "Lab"
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s %(name)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

if args.debug:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

if args.root:
    defaultPath = args.root

if args.output:
    outputFile = args.output

def find_files(catalog, mask):
    found_files = []
    for root, dirs, files in os.walk(catalog):
        logger.info(root)
        logger.info(dirs)
        logger.info(files)
        for name in files:
            if fnmatch.fnmatch(name, mask):
                #todo check on mask
                found_files.append({"path": root, "name": name})
    return found_files

def loadFileData(array):
    for fileData in array:
        with open(fileData['path'] + "\\" + fileData['name']) as file:
            data = file.readline()
            fileData['data'] = data

def createJson(array):
    json = {"VectorTelemetry": {}}
    for data in array:
        indexDot = data['name'].index(".")
        json['VectorTelemetry'][data['name'][:indexDot]] = float(data['data'])
    return json

def saveJsonToFile(jsondata):
    with open(outputFile, 'w') as file:
        json.dump(jsondata, file, indent=4)

def main():
    files = find_files(defaultPath, "*")
    loadFileData(files)
    json = createJson(files)
    saveJsonToFile(json);

main()

