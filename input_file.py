def input_data(filename):
    """
    Reads an input file and extracts data from it.
    :param filename: a directory where the input file is located.
    :return data: a list of words from file.
    """
    with open(filename, "r") as file:
        data = []
        for word in file.readlines():
            # Adding a word to a list from both a classic list file and a ReWord-style file
            data.append(word.strip().replace('"', '').split(";")[0])
    return data


if __name__ == "__main__":
    pass
