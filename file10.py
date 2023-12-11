def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    data = data.split("\n")
    mx = len(data[0])

    for i in data:
        if mx <len(i):
            mx = len(i)
    return mx
# Read data from file
f = open("data/data10.txt")
s = f.read()
print(main(s))