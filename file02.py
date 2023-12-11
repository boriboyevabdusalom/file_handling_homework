def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    return len(data) 
# Read data from file
f = open("data/data02.txt")
s = f.read()
print(main(s))