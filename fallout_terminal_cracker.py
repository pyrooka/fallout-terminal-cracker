#!/usr/bin/python

import sys, re

basewords = [] #default list
answers = [] #list of possible codes

#print help for the lame guyz outside
def printHelp(case):
    if case == 1:
        print "Use from terminal/cmd with one parameter: list of the words separate by enter."
    if case == 2:
        print "Input format: \"yourword\" \"likeness\" (without qoutes)"

#narrow the answers list
def narrowList():

    global answers
    global basewords

    print "You can choose from these words: " + str(basewords)  # all remained words
    print ""
    print "The answer is in these words:    " + str(answers)  # possible asnwers
    print ""

    result = raw_input("Result(word likeness): ")  #prompt to input the last tries word and its likeness

    # check the input
    if not inputCheck(result):
        printHelp(2)
        return False

    # set the word and the likeness value from the user input
    if " " in result:
        temp_list = result.split(" ")
        word = temp_list[0]
        likeness = int(temp_list[1])
    else:
        word = result
        likeness = 0

    # delete all appereance of the input word from the answers list
    answers = filter(lambda a: a != word, answers)
    basewords = filter(lambda a: a != word, basewords)

    # if the likeness is 0, just deleted the word from the list, nothing else to do
    if likeness == 0:
        return

    # if likeness not 0 lets continue
    for answer in answers:
        like = 0  # if a letter equals, increase this by one
        for i in range(0,len(answer)):
            if(answer[i] == word[i]):
                like += 1
        # after get all of the equals return and the like is the same or bigger then the likeness let it in the list.
        # else delete it

        if like < likeness:
            answers = filter(lambda a: a != answer, answers)


# check is the user input correct..never trust in ppl.except urself. except if ur name anuka. meh never trust in anuka
def inputCheck(inp):
    global basewords

    if " " in inp:
        l = inp.split(" ")
        if l[0] not in basewords:
            return False
        r = re.match("[a-zA-Z]* [0-9]*", inp)
        if not r:
            return False
    r = re.match("[a-zA-Z]*", inp)
    if not r:
        return False

    return True

def main(file):

    global basewords
    global answers

    # open the word file for read
    try:
        f = open(file, "r")
    except:
        print "Cannot open %s." % file
        sys.exit()

    # fill up basewords list without the new line character
    for line in f:
        basewords.append(line.replace("\n", ""))

    answers = basewords # atm the possible answer is the default list
    printHelp(2)
    while True:
        narrowList() # lets start narrowing the our answer list

        # if only 1 answer left no more trying
        if len(answers) == 1:
            print "Congratulation! The solution is: %s" % (answers[0])
            break

    print "The possible answers are: " + str(answers)
    sys.exit()






if __name__ == "__main__":
    if len(sys.argv) != 2:
        printHelp(1)
        sys.exit()

    main(sys.argv[1])