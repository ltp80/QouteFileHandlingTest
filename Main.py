import Modules
import os
import Config
from Modules import FileUtility
from Modules import Utility

QuotesPath = Config.DirPath + r"/Quotes.txt"

def Start():
    FilePath = input("AbsolutePathToFile ?: \n")
    if os.path.exists(FilePath):
        print("You Are about to overwrite a file are you sure you want to continue ?")
        Key,Val=Utility.InputInDictionaryKeys(
            {"1": True,"2": False},
            "1: I am sure\n2: Rather not actually\n?:",
            "Invalid choice")
        if not Val: return 0
    lines = FileUtility.GetLinesOfInTable(QuotesPath)

    QuoteCount = None

    Key,HasDoubles = Utility.InputInDictionaryKeys(
        {"1": True, "2": False},
        "Can you're files have doubles ?\n1) yes\n2) no\nanswer:",
        "Please select either one or two"
        )
    

    while not QuoteCount:
        UsrInput = input("How many qoutes do you wish for ?\n").strip()
        QuoteCount = int(UsrInput) if UsrInput.isdigit() and not int(UsrInput) <= 0 else None
        if not HasDoubles and QuoteCount > len(lines):
            print("Select number between one and "+str(len(lines)))
            QuoteCount = None

    QuoteLines = Utility.GetRandomNumbers(0,len(lines)-1,HasDoubles,QuoteCount)

    FileUtility.AddContentToFile(Config.LogPath,f"opening file: {FilePath}")
    print(FilePath)

    folder = os.path.dirname(FilePath)
    
    if folder and not os.path.exists(folder):
        print(f"Creating missing directory: {folder}")
        os.makedirs(folder)

    f=open(FilePath,"+w")
    for line in QuoteLines:
        FileUtility.AddContentToFile(Config.LogPath,f"Adding Qoute {line}")
        f.write(lines[line])
    f.close()
Start()

#/home/ltp/Documents/My programming projects/Python/FileHandling/RandomQuotes/QouteFileHandlingTest/output.txt