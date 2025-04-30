import pathlib
import os
import glob
import re
import shutil
from typing import Callable
from .logger import logger

def extractNameFromFile(filePath):
    return pathlib.Path(filePath).stem

def extractNameWithExtensionFromFile(filePath):
    return pathlib.Path(filePath).name

def extractNameFromDir(dirName):
    return pathlib.Path(dirName).stem

def check_dir_exists(dir_path) :
    dir = pathlib.Path(dir_path)
    return dir.exists() and dir.is_dir()

def identify_yaml_extension(file_path: str) -> str:
    """
    Takes file_path and check if it exists either with .yml or .yaml extension and returns existing file
    """
    file_root, _ = os.path.splitext(file_path)
    possible_files = [file_root + ext for ext in ['.yml', '.yaml']]
    for file in possible_files:
        if os.path.isfile(file):
            return file
    raise FileNotFoundError(f"Neither of these files: {possible_files} exist.") 

def find_all_sub_dir(dir_path):
    return os.walk(dir_path)

def check_file_exists(file_path) :
    file = pathlib.Path(file_path)
    return file.exists() and file.is_file()

def check_dir_exist_and_create(dir_path) :
    logger.debug(f'Checking that dir exists or create dir in path: {dir_path}')
    os.makedirs(dir_path, exist_ok=True)

def delete_dir(path) :
    try:
        shutil.rmtree(path)
    except:
        logger.info(f'{path} directory does not exist')

def copy_path(source_path, target_path) :
    # check that we are not trying to copy file to itself, or 'cp' will exit with error
    if getDirName(source_path) == getDirName(target_path) and (check_file_exists(source_path) and source_path == target_path + extractNameWithExtensionFromFile(source_path)):
        logger.info(f"Trying to copy {source_path} to itself (target path: {target_path}). Skipping...")
    elif glob.glob(source_path) : 
        logger.info(f'Copying from {source_path} to {target_path}')
        logger.debug(f'Checking target path {target_path} exists: {os.path.exists(target_path)}')
        if not os.path.exists(target_path) :
            if os.path.isdir(target_path) :
                dirPath = target_path
            else :
                dirPath = os.path.dirname(target_path)
            logger.debug(f'Creating dir {dirPath}')
            os.makedirs(dirPath, exist_ok=True)
        exit_code = os.system(f"cp -rf {source_path} {target_path}")
        if (exit_code) :
            logger.error(f"Error during copying from {source_path} to {target_path}")
            exit(1)
    else :
        logger.info(f"Path {source_path} doesn't exist. Skipping...")

def move_path(source_path, target_path) :
    if glob.glob(source_path) : 
        logger.info(f'Moving from {source_path} to {target_path}')
        logger.debug(f'Checking target path {target_path} exists: {os.path.exists(target_path)}')
        if not os.path.exists(target_path) :
            if os.path.isdir(target_path) :
                dirPath = target_path
            else :
                dirPath = os.path.dirname(target_path)
            logger.debug(f'Creating dir {dirPath}')
            os.makedirs(dirPath, exist_ok=True)
        exit_code = os.system(f"mv -f {source_path} {target_path}")
        if (exit_code) :
            logger.error(f"Error during Moving from {source_path} to {target_path}")
            exit(1)
    else :
        logger.info(f"Path {source_path} doesn't exist. Skipping...")


def openFileAsString(filePath):
    with open(filePath, 'r') as f:
        result = f.read()
    return result

def deleteFile(filePath):
    os.remove(filePath)

def writeToFile(filePath, contents):
    os.makedirs(os.path.dirname(filePath), exist_ok=True)
    with open(filePath, 'w+') as f:
        f.write(contents)
    return

def getAbsPath(path):
    return os.path.abspath(path)

def getRelPath(path, start_path=None):
    if start_path:
        return os.path.relpath(path, start_path)
    return os.path.relpath(path, os.getenv('CI_PROJECT_DIR'))

def get_parent_dir_for_dir(dirPath):
    path = pathlib.Path(dirPath)
    return str(path.parent.absolute())

def getDirName(filePath):
    return os.path.dirname(filePath)

def getParentDirName(filePath):
    return os.path.dirname(getDirName(filePath))

def get_files_with_filter(path_to_filter: str, filter: Callable[[str], bool]) -> set[str]:
    matching_files = set()
    for root, _, files in os.walk(path_to_filter):
        for file in files:
            filepath = os.path.join(root, file)
            if filter(filepath):
                matching_files.add(filepath)
    return matching_files

def findAllFilesInDir(dir, pattern, notPattern="", additionalRegexpPattern="", additionalRegexpNotPattern=""):
    result = []
    dirPointer = pathlib.Path(dir)
    fileList = list(dirPointer.rglob("*.*"))
    for f in fileList:
        result.append(str(f))
    return findFiles(result, pattern, notPattern, additionalRegexpPattern, additionalRegexpNotPattern)

def findFiles(fileList, pattern, notPattern="", additionalRegexpPattern="", additionalRegexpNotPattern="") :
    result = []
    for filePath in fileList:
        if (
            pattern in filePath 
            and (notPattern=="" or notPattern not in filePath) 
            and (additionalRegexpPattern=="" or re.match(additionalRegexpPattern, filePath))
            and (additionalRegexpNotPattern=="" or not re.match(additionalRegexpNotPattern, filePath))
        ):
            result.append(filePath)
            logger.debug(f"Path {filePath} match pattern: {pattern} or notPattern: {notPattern} or additionalPattern: {additionalRegexpPattern}")
        else:
            logger.debug(f"Path {filePath} doesn't match pattern: {pattern} or notPattern: {notPattern} or additionalPattern: {additionalRegexpPattern}")
    return result

def removeAnsibleTrashFromFile(filePath) :
    ansible_trash = [
        "# BEGIN ANSIBLE MANAGED BLOCK\n---",
        "# END ANSIBLE MANAGED BLOCK",
        "# BEGIN ANSIBLE MANAGED BLOCK"
    ]
    with open(filePath, 'r') as f:
        fileContent = f.read()
        for trash in ansible_trash:
            fileContent = fileContent.replace(trash, "")
    with open(filePath, 'w') as f:
        f.write(fileContent)


def get_all_files_in_dir(dir, pathToRemove=""):
    result = []
    dirPath = pathlib.Path(dir)
    for item in dirPath.rglob("*"):
        if item.is_file():
             itemStr = str(item)
             if pathToRemove:
                 itemStr = itemStr.replace(pathToRemove, "")
             result.append(itemStr)
    return result
