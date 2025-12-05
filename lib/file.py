import sys

def readlines() -> list[str]:
    '''Read and return all lines of text from a file'''
    filename = sys.argv[0].split("\\")[-1]
    
    if not filename[-3:] == ".py":
        raise ValueError("Filename must end with .py")
    
    filename = filename[:-3]
    
    if len(sys.argv) > 1:
        filename += "-" + sys.argv[1]
    
    filename += ".txt"
    
    with open("input/" + filename, "r") as file:
        return [line.strip() for line in file.readlines()]


def readgrid() -> list[list[str]]:
    '''Read and return a grid of characters from a file'''
    lines = readlines()
    return [list(line) for line in lines]
