def display_banner():
    '''Display program name in a banner'''
    msg = 'Camel Case Generator Program'
    stars = '*' * len(msg)
    print('\n', stars, '\n', msg, '\n', stars, '\n')

def instructions():
    '''Display instructions'''
    msg = 'Please enter a sentence to convert to camel case'
    print('\n', msg, '\n')

# add input: done
def setup():
    display_banner()
    instructions()

    userInput = input(": ")

    return userInput

# TODO: add validation for userInput and don't allow special characters

# example = "fOnt proCESSOR and ParsER", originally used before input
def camel_case(userInput):

    inputList = userInput.lower().title().split(" ")

    inputList[0] = inputList[0].lower()

    camelCase = ""

    camelCase = camelCase.join(inputList)

    return camelCase

def main():

    original = setup()

    altered = camel_case(original)

    print("CamelCase-- ",altered)

#main()
