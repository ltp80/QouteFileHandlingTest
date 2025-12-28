def GetLinesOfInTable(FilePath: str):
    f = open(FilePath, "r")
    lines = f.readlines()
    f.close()
    return lines

def GetLineWithStringIn(Path: str,String: str):
    f = open(Path,"r")
    for line in f.readlines():
        if String in line:
            return line
        