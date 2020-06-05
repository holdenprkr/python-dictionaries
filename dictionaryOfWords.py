word_definitions = dict()

word_definitions["Responsible"] = "having an obligation to do something, or having control over or care for someone, as part of one's job or role."
word_definitions["Discipline"] = "the practice of training people to obey rules or a code of behavior, using punishment to correct disobedience."
word_definitions["Consistency"] = "conformity in the application of something, typically that which is necessary for the sake of logic, accuracy, or fairness"

for (key, value) in word_definitions.items():
    print(f"{key}: {value}")

print("")

idioms = {
    "Penny": ["A", "penny", "for", "your", "thoughts"],
    "Injury": ["Add", "insult", "to", "injury"],
    "Moon": ["Once", "in", "a", "blue", "moon"],
    "Grape": ["I", "heard", "it", "through", "the", "grapevine"],
    "Murder": ["Kill", "two", "birds", "with", "one", "stone"],
    "Limbs": ["It", "costs", "an", "arm", "and", "a", "leg"],
    "Grain": ["Take", "what", "someone", "says", "with", "a", "grain", "of", "salt"],
    "Fences": ["I'm", "on", "the", "fence", "about", "it"],
    "Sheep": ["Pulled", "the", "wool", "over", "his", "eyes"],
    "Lucifer": ["Speak", "of", "the", "devil"],
}

separator = ' '

for (key, value) in idioms.items():
    print(f"{key}: {separator.join(value)}")

print("")

my_family = {
    "brother": {
        "name": "Faison",
        "age": 26
    },
    "mother": {
        "name": "Janet",
        "age": 54
    },
    "father": {
        "name": "David",
        "age": 57
    }
}

for (key, value) in my_family.items(): 
    print(f"{value['name']} is my {key} and is {str(value['age'])} years old.")

print("")

stockDict = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak"
} 

purchases = [
    ( 'GM', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'EK', 200, '1-jul-1998', 56 ),
    ( 'GM', 150, '30-aug-2001', 47 )
]

for tuple in purchases:
    print(f"I purchased {stockDict[tuple[0]]} stock for ${tuple[1] * tuple[3]}")

purchaseBlocks = dict();

for tuple in purchases:
    if tuple[0] in purchaseBlocks.keys():
        purchaseBlocks[tuple[0]].extend([tuple])
    else:
        purchaseBlocks[tuple[0]] = [tuple]


print("")

for (key, value) in purchaseBlocks.items():
    totalValue = 0

    print(f"------ {key} ------")
    for tuple in value:
        print(f"{tuple[1]} shares at {tuple[3]} dollars each on {tuple[2]}")
        totalValue += (tuple[1] * tuple[3])
    print("")
    print (f"Total value of stock in portoflo:  ${totalValue}")