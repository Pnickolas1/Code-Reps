

"""
given a string of numbers, create all variations of valid ip addresses


"""


def isValid(string):
    stringAsInt = int(string)
    if stringAsInt > 255:
        return False
    return len(string) == len(str(stringAsInt))


def validIPAddresses(string):

    ips = []

    for i in range(1, min(len(string), 4)):
        ipComponents= ["", "", "", ""]

        ipComponents[0] = string[:i]

        if not isValid(ipComponents[0]):
            continue

        for j in range(i + 1, i + min(len(string) - i, 4)):
            ipComponents[1] = string[i : j]

            if not isValid(ipComponents[1]):
                continue

            for k in range(j + 1, j + min(len(string)- j, 4)):
                ipComponents[2] = string[j:k]
                ipComponents[3] = string[k:]

                if isValid(ipComponents[2]) and isValid(ipComponents[3]):
                    ips.append(".".join(ipComponents))
    return ips
