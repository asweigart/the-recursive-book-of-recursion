import os

def filesWithOfEvenByteSizes(fullFilePath):
    """Returns True if fullFilePath has an even size in bytes, otherwise
    returns False."""
    fileSize = os.path.getsize(fullFilePath)
    return fileSize % 2 == 0


def filesWithAllVowelsInFilename(fullFilePath):
    """Returns True if the fullFilePath has a, e, i, o, and u, otherwise
    returns False."""
    name = os.path.basename(fullFilePath).lower()
    return ('a' in name) and ('e' in name) and ('i' in name) and ('o' in name) and ('u' in name)


def walk(folder, matchFunc):
    """Calls the match function with every file in the folder and its
    subfolders. Returns a list of files that the match function
    returned True for."""
    matchedFiles = []  # This list holds all the matches.
    folder = os.path.abspath(folder)  # Use the folder's absolute path.

    # Loop over every file and subfolder in the folder:
    for name in os.listdir(folder):
        filepath = os.path.join(folder, name)
        if os.path.isfile(filepath):
            # Call the match function for each file:
            if matchFunc(filepath):
                matchedFiles.append(filepath)
        elif os.path.isdir(filepath):
            # Recursively call walk for each subfolder, extending
            # the matchedFiles with their matches:
            matchedFiles.extend(walk(filepath, matchFunc))
    return matchedFiles


print('All files with even byte sizes:')
print(walk('.', filesWithOfEvenByteSizes))
print('All files with every vowel in their name:')
print(walk('.', filesWithAllVowelsInFilename))
