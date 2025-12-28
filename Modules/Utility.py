import random

def InputInDictionaryKeys(t: dict, prompt: str, MsgOnIncorrect: str): # asks user for an input until it is in the given dictionary
    while True:
        InputV = input(prompt).strip() # define output
        if InputV in t.keys(): # check if in dictionary keys
            return InputV,t[InputV] # return key and value
        print(MsgOnIncorrect) # warn about input
def InputInList(t: list, prompt: str, MsgOnIncorrect):
    while True:
        InputV = input(prompt).strip() # define output
        if InputV in t: # check if in dictionary keys
            return InputV # return key and value
        print(MsgOnIncorrect) # warn about input

def GetRandomNumbers(IntRangeMin: int, IntRangeMax: int, Doubles: bool, Amount: int):
    if Doubles:
        return [random.randint(IntRangeMin,IntRangeMax) for _ in range(Amount)]
    else:
        Nums = []
        for i in range(Amount):
            rng = random.randint(IntRangeMin,IntRangeMax)
            if not rng in Nums:
                Nums.append(rng)
                continue
            i -= 1
        return Nums
        
    
print(GetRandomNumbers(0,100,False,83))