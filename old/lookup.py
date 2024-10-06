import sys

# This is a listing of all the words we have learned!
vocab_words = {"perusal": "Survey or reading.",
    "impetuous": "having a sudden or rash action.",
    "implicate": "to show or be involved.", 
    "inherent":"existing as an inseparable quality or element.",
    "tenable": "cabable of being maintauned against attack or dispute.",
    "tenet": "a princible held as true by a group or movement.",
    "lament": "to feel or express sorrow or grief.",
    "superfluous": "more than sufficient or required.",
    "complacent": "pleased with oneself.",
    "laud": "to praise.",
    "languid": "lacing energy or vitality.",
    "substantiate": "to entablish by proof or evidence.",
    "underscore": "to stress or emphasize.",
    "moderate": "not extreme, excessive, or intense.",
    "implacable": "not to be appeased or pacified.",
    "definitive": "complete, satisfying all criteria",

}

# Make sure there is a word that the user typed for us to look up!
print(f"There are {len(sys.argv)} arguments.")

if len (sys.argv) == 1:
    print(vocab_words.keys())
    
    sys.exit(0)
elif len(sys.argv) != 2:
    print("""lookup: Use lookup to look up the definition of a word.
To use, type "lookup <word>".""")
    sys.exit(0)


# Lookup the word as the first argument
word = sys.argv[1]
word = word.lower()



# Excepting the keyerror so that if there is a word that isn't in the dict it says "that def is unknown"
try:
    print(f"lookup: The definition of the word '{word}' is {vocab_words[word]}.")
except KeyError:
    print(f"That defintion is unknown so far.") 