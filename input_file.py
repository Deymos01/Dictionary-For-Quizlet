def input_data(filename):
    with open(filename, "r") as file:
        data = []
        ff = file.readlines()
        ff = [x.strip() for x in ff]
        if all(x[0] == x[-1] == '"' for x in ff):
            for chain in ff:
                line = chain.split(";")
                data.append(line[0][1:-1])
        else:
            for chain in ff:
                data.append(chain)
    return data


if __name__ == "__main__":
    pass
