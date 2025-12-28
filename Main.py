import Modules
import Config
from Modules import FileUtility
from Modules import Utility

QuotesPath = Config.DirPath + r"/Quotes.txt"
FilePath = input("AbsolutePathToFile ?: \n")

lines = FileUtility.GetLinesOfInTable(QuotesPath)

QuoteCount = None

Key,HasDoubles = Utility.InputInDictionaryKeys(
    {"1": True, "2": False},
    "Can you're files have doubles ?\n1) yes\n2) no\nanswer:",
    "Please select either one or two"
    )

while not QuoteCount:
    UsrInput = input("How many qoutes do you wish for ?\n").strip()
    QuoteCount = int(UsrInput) if UsrInput.isdigit and not int(UsrInput) <= 0 else None
    if not HasDoubles and QuoteCount > len(lines):
        print("Select number between one and "+str(len(lines)))
        QuoteCount = None

QuoteLines = Utility.GetRandomNumbers(0,len(lines)-1,HasDoubles,QuoteCount)

f=open(FilePath,"+w")
for line in QuoteLines:
    f.write(lines[line])