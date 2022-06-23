import random
import array
# before i had "import numpy" but it cause an error for some reason

NOUNS = ("cat", "dog", "snake", "wind", "globe", "world", "snow", "rain", "sun", "movie", "song", "demon",
         "eyes", "voice", "mouth", "smile", "heart", "soul", "house", "home", "life", "eyelash", "star", "pencil",
         "paper", "tv", "belief", "hand", "butt", "headphone", "sound", "sight", "feel", "ground", "fear",
         "love", "school", "shoe", "eraser", "head", "thought", "mind", "legs", "tree", "ocean", "water",
         "sky", "river", "moon", "hockey stick", "puck", "shirt", "shorts", "hat", "umbrella", "highlighter",
         "marker", "glass", "trophy", "plate", "drawer", "mirror", "flower", "plant", "chimney", "roof", "computer",
         "phone", "frying pan", "dress", "blanket", "money", "location", "field", "street", "match", "card",
         "table", "chair", "calculator", "chicken", "tuna", "candy", "sugar", "bitterness", "girl", "man", "bride", "meaning of life") # noun options

QUESTIONWORDS = ("who", "what", "where", "when", "why", "how", "wherever", "whenever")

NAME = ("Ariana Grande", "Santa Clause", "Jim Carrey", "Mr. Bean", "you", "them", "her", "him", "Jack", "Emily",
        "Brad", "Beatrice", "Jolene", "Madison", "Jake", "Jamie", "Jessica", "Heather", "Rick", "Michael", "Lisa",
        "Erica", "Melisa", "Pauline", "Theebika", "Mercedes", "Evelyn", "Anahita", "Dom", "Vanessa", "Philip",
        "Polly", "Ella", "Max", "Sam", "Alex", "Ben", "No one") # name options

PRONOUNSWITHNOS = ("I", "you") # pronoun options
PRONOUNSWITHS = ("he", "she", "it")

TRANSITIONWORDS = ("but", "to", "while", "for", "meanwhile", "therefore", "since", "obviously", "unlike",
                   "if", "even if", "even though",  "although", "...well maybe,", "however") # transition words options

ADJECTIVES = ("big", "small", "tiny", "huge", "so", "fast", "slow", "creepy", "annoying", "flat", "shaky",
              "cute", "adorable", "average", "clueless", "dirty", "clean", "fancy", "mean", "happy", "lively",
              "delightful", "helpless", "itchy", "defeated", "smooth", "dark", "light", "bright", "shiny",
              "moldy", "slippery", "slimy", "fluffy", "ugly", "beautiful", "kind", "crazy", "hurtful", "funny", "most") # adjective word option

ADVERBS = ("accidentally", "quickly", "slowly", "loudly", "quietly", "intensely", "lyrically", "dreamily", "actually",
           "angrily", "oddly", "forcefully", "furiously", "closely", "anxiously", "amazingly", "abruptly", "cooly",
           "mostly", "mentally", "gently", "clearly", "daily", "obviously", "accidentally", "gracefully",
           "mysteriously", "greedily", "boldly", "jokingly", "closely", "nervously", "energetically", "innocently") # adverb word options

TITLEFIRSTWORDS = ("Wow, ", "Lovey ", "Incredible ", "Stupid Stupid ", "Intensified ", "", "Invented ", "Playful ",
                   "Condescending ", "Irritable ", "Hello ", "C'mon ", "Jolly Old ", "Cruel ", "Melodramatic ", "The Eighth Wonder: The ",
                   "The Effect of ", "For the Love of ", "God's ", "Space ", "Empty ", "Half-Hearted ", "Poetic ",
                   "Tough ", "BAD ") # first word title options

TITLELASTWORDS = (" Gone Wrong", " Mania", " Repeated", ", But How?", " Chicken", " Dance", " Evolution", " Mood",
                  "?", "!", " Hello?", "??? no\n...but maybe", " Intensifies.", " Y'all", " Under the Rug",
                  " of the World", " in the Night", " After Autumn",
                    " Restaurant", " the Movie", " by the Way", " Appliances", ", eh?", " amiright?", " Reinvented",
                  " or Not", " ...") # last word title options

ONESPRESENTVERBS = ("go to ", "love", "dance to", "twirl to", "ponder", "wake up to", "dare to", "fly to", "fail to",
                    "hope", "leave to", "hate", "despise", "lie to", "like", "scream", "don't see", "know", "don't know",
                    "start", "advance toward", "squint at", "ponder", "find", "cast a spell on", "cry about", "become",
                    "catch", "imagine", "spin in", "see in", "end in", "swim in", "cook in", "speak",
                    "bring in", "crie in", "orbit around", "hang in", "grow in", "lead in", "jump in", "lie in",
                    "do", "create", "eat", "have", "watch", "try", "make", "like", "can do", "despise", "touche",
                    "love")

UNCONJUGATEDVERBS = ("going", "having", "knowing", "sewing", "living", "breathing", "thriving", "farting", "glowing",
                     "flowing", "dancing", "prancing", "running", "shaking", "pondering", "wondering", "humming",
                     "processing", "calculating", "recalculating", "loving", "laughing", "mocking", "rushing", )

# verb options are in if statements after tense is chosen

computerVerb = ["" for x in range (3)]

print('Welcome to poem collab, where you can collaborate with the computer to write an award winning poem!')

theme = input('\nWhat theme is your poem? ')

title = random.choice(TITLEFIRSTWORDS) + theme + random.choice(TITLELASTWORDS)

verbTense = int(input('Choose a verb tense. Enter 1 for present, 2 for past, 3 for future: '))

verbChosen = input('Choose one verb you would like to use in your poem (in the tense you chose): ')

nounChosen1 = input('Choose one noun related to your theme that you would like to use: ')
nounChosen2 = input('Choose one more noun: ')

adjectiveChosen = input('Finally, choose a relevant adjective: ')

if verbTense == 1:  # present tense
    VERBS = ("goes to ", "loves", "dances to", "twirls to", "ponders", "wakes up to", "dares to", "flies to", "fails to",
             "hopes", "leaves to", "hates", "despises", "lies to", "likes", "screams at", "doesn't see", "knows", "doesn't know",
             "starts", "advances toward", "squints at", "ponders", "finds", "casts a spell on", "cries about", "becomes",
             "catches", "imagines", "spins in", "sees in", "ends in", "swims in", "cooks in", "speaks",
             "brings in", "cries in", "orbits around", "hangs in", "grows in", "leads in", "jumps in", "lies in",
             "does", "creates", "eats", "has", "watches", "tries", "makes", "likes", "can do", "despises", "touches",
             "loves", "gallops", "hoards", "touches", "ponders", "empowers")

elif verbTense == 2:  # past tense
    VERBS = ("went to", "loved", "danced to", "twirled to", "pondered", "woke up to", "dared to", "flew to",
             "failed to", "hoped to", "left", "hated", "despised", "lied to", "liked", "screamed at", "didn't see",
             "knew", "didn't know", "started", "advanced toward", "squinted at", "pondered", "found",
             "casted a spell on", "cried about", "became", "wondered what", "cought", "imagined", "spun in", "saw",
             "ended", "swam in", "cooked up", "spoke in", "brought", "cried", "orbited around", "hung to",
             "grew", "lead", "jumped in", "lied in", "loved", "did", "created", "ate", "had", "watched", "tried to",
             "made", "liked", "could do", "despised", "touched", "galloped", "hoarded", "touched", "pondered", "empowered")

elif verbTense == 3:  # future tense
    VERBS = ("will go to", "will love", "will dance to", "will twirl to", "will ponder", "will wake up to",
               "will dare to", "will fly to", "will fail to", "will hope to", "will leave", "will hate", "will despise",
               "will lie to", "will like to", "will scream at", "will don't see", "will know", "will don't know",
               "will start", "will advance towards", "will squint at", "will ponder", "will find",
               "will cast a spell on", "will cry about", "will become", "will spin in", "will see", "will end",
               "will swim in", "will cook", "will speak in", "will bring in", "will cry", "will orbit around",
               "will hang", "will grow", "will lead", "will jump in", "will lie to" "will do", "will create",
               "will eat", "will have", "will watch", "will try to", "will make", "will like", "can do",
               "will despise","will touch", "will love", "will gallop", "will hoard", "will touch", "will ponder", "will empower")


for i in range(0, 3):

    # choose the random verbs
    computerVerb[i] = (random.choice(VERBS))

formatNum = random.randint(1, 2)    # choose a random format for the poem

# different formats of the poem
if formatNum == 1:

    name = random.choice(NAME)
    if verbTense == 3:
        Line1 = (name + ' will ' + random.choice(ADVERBS) + ' ' + computerVerb[0][5:] + ' the ' +
                nounChosen1)
    else:
        Line1 = (name + ' ' + random.choice(ADVERBS) + ' ' + computerVerb[0] + ' the ' +
                nounChosen1)

    Line2 = ('But ' + name + ' ' + verbChosen + ' so much')
    Line3 = ("Only the " + nounChosen2 + ' ' + computerVerb[1] + " the " + random.choice(NOUNS))

    if verbTense == 3:
        Line4 = (random.choice(PRONOUNSWITHS) + ' will ' + random.choice(ADVERBS) + ' ' + computerVerb[2][5:]
                 + ' the ' + random.choice(NOUNS))
    else:
        Line4 = (random.choice(PRONOUNSWITHS) + ' ' + random.choice(ADVERBS) + ' ' + computerVerb[2] + ' the ' +
                 random.choice(NOUNS))



elif formatNum == 2:

    name = random.choice(NAME)

    ("who", "what", "where", "why", "how", "wherever", "whenever")
    if QUESTIONWORDS == "who":
        ANSWERWORD = "they"
    elif QUESTIONWORDS == "what":
        ANSWERWORD = "that"
    elif QUESTIONWORDS == "where":
        wordsWhere= ("there", "wherever")
        ANSWERWORD = random.choice(wordsWhere)
    elif QUESTIONWORDS == "when":
        wordsWhen = ("then", "whenever")
        ANSWERWORD = random.choice(wordsWhen)
    elif QUESTIONWORDS == "why":
        ANSWERWORD = "because"
    elif QUESTIONWORDS == "how":
        ANSWERWORD = ""

    Line1 = name + ' ' + random.choice(VERBS) + ' the '  + random.choice(ADJECTIVES) + ' ' + nounChosen1
    Line2 = 'In the ' + adjectiveChosen + ' ' + random.choice(NOUNS) + ', for the ' +  ' ' + random.choice(NOUNS)
    if verbTense==3:
        Line3 = random.choice(QUESTIONWORDS) + ' will ' + name + ' ' + random.choice(ADVERBS) + ' '+ verbChosen[4:] + '?'
    else:
        Line3 = random.choice(QUESTIONWORDS) + ' will ' + name + ' ' + random.choice(ADVERBS) + ' ' +\
                random.choice(ONESPRESENTVERBS) + '?'
    Line4 = 'To ' + random.choice(ONESPRESENTVERBS) + ' a ' + nounChosen2 + '.'

elif formatNum == 3:
    print()

elif formatNum == 4:
    print()

elif formatNum == 5:
    print()

elif formatNum == 6:
    print()

print('\n\n' + title + '\n\n' + Line1 + '\n' + Line2 + '\n' + Line3 + '\n' + Line4)
