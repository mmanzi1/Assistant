#### skills.py
#### Matt Manzi
#### 2018-03-19
#### Skills are the collection of abilities that Assistant can do (represented as
#### one function per skill).  Skills match up with Knowledge.
import json
import constants as c

# add finds the sum of param0 and param1
def add(param0, param1):
    sum = param0 + param1
    return sum

# learn creates a new skill named by param0
def learn(param0):

    # open Knowledge
    try:
        knowledgeFile = open(c.KNOWLEDGE, "r")
    except:
        # LOG.error("Unable to load Knowledge, ensure that \"%s\" is in the current directory.", c.KNOWLEDGE)
        raise
    # else:
        # LOG.debug("Opened Knowledge from: %s", c.KNOWLEDGE)

    try:
        knowledge = json.load(knowledgeFile)
    except:
        # LOG.error("Unable to load Knowledge, ensure that the JSON file is properly formatted.")
        raise
    finally:
        knowledgeFile.close()

    # new skill
    skillAttrs = {}
    knowledge[param0] = skillAttrs

    # ask how to do it
    rawTask = input("How can I do that based on what I already know how to do? ")






# help displays a help dialog
def help():
    print("I am Assistant. I can help you with a variety of simple tasks.")
    print("These are the things I know how to do:")

    with open(c.KNOWLEDGE, "r") as knowledgeFile:
        skills = json.load(knowledgeFile)
        for s in skills:
            print("\t", s.capitalize(), "-", skills[s][c.DESC])
            print("\t\tIn:", skills[s][c.NUM_PARAM], skills[s][c.TYPE_PARAM],
                "=> Out:", skills[s][c.NUM_RET], skills[s][c.TYPE_RET])
        print("\t Exit")
