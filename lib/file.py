def readlines(filename: str) -> list[str]:
    '''Read and return all lines of text from a file'''
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]
