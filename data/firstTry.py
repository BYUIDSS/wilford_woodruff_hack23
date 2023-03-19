# %%
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
import re
import string
from difflib import SequenceMatcher

# %%
def normalize(entry):
    def preserve_char(match_obj):
        mo_list = match_obj.group().split()
        return mo_list[-1]
    entry = re.sub("\\n", " ", entry)
    entry = re.sub(r"(\[\[).*?(\]\])", "", entry)
    entry = re.sub("&", "", entry)
    entry = re.sub(r"/.*?[a-zA-Z]", preserve_char, entry)
    entry = entry.translate(str.maketrans("", "", string.punctuation))
    entry = re.sub(r"  *", " ", entry)
    return entry.lower()

# %%
# Normalizes the text in a string
def translateText(text):
    text = re.sub("\\n", " ", text)
    text = re.sub(r"(\[\[).*?(\]\])", "", text)
    text = re.sub(r"&amp;", "", text)
    text = re.sub(r"/.*?[a-zA-Z]", "", text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub("  *", " ", text).lower()
    
    stringList = text.split(" ")
    return stringList

# Function to caompare phrases 
def compare(phrase_1, phrase_2):
    return SequenceMatcher(None, phrase_1, phrase_2).ratio()

# %%
# Set up dataBases
journalsData = pd.read_csv("journals.csv")
scriptureData = pd.read_csv("lds-scriptures.csv")

# %%

# Turns column into list
myList = scriptureData["scripture_text"].tolist()
newList = []
# Goes through each row and normalizes text
for i in myList:
    newList.append(translateText(i))
# Adds new text 
scriptureData["scripture_text_normalized"] = newList


# %%
myList = journalsData["text_only_transcript"].tolist()
newList = []
for i in myList:
    if type(i) == str:
        newList.append(translateText(i))
    else:
        newList.append(i)

journalsData["text_normalized"] = newList

# %%

longBookList = scriptureData.book_title.unique().tolist()
for i in range(len(longBookList)):
    longBookList[i] = longBookList[i].lower()

bookList = scriptureData.book_short_title.unique().tolist()
for i in range(len(bookList)):
    bookList[i] = bookList[i].translate(str.maketrans('', '', string.punctuation)).lower()
    bookList[i] = ''.join([i for i in bookList[i] if not i.isdigit()])
    bookList[i] = re.sub("  *", "", bookList[i])


# %%

matchDict = {}

for entry in journalsData["text_normalized"]:
    if type(entry) == list:
        for book in longBookList:
            if entry.count(book) > 0:
                #journalEntry = journalsData.loc[journalsData['text_normalized'] == entry]
                stringEntry = ' '.join(entry)
                if stringEntry not in matchDict.keys():
                    matchDict[stringEntry] = [book]
                else:
                    matchDict[stringEntry].append(book)
        for book in bookList:
            if entry.count(book) > 0:
                #journalEntry = journalsData.loc[journalsData['text_normalized'] == entry]
                stringEntry = ' '.join(entry)
                if stringEntry not in matchDict.keys():
                    matchDict[stringEntry] = [book]
                else:
                    matchDict[stringEntry].append(book)

# %%
columnList = journalsData["text_normalized"].tolist()

# %%
newList = []
for entryList in columnList:
    if type(entryList) == list:
        stringEntry = ' '.join(entryList)
        newList.append(stringEntry)
    else:
        newList.append(entryList)

journalsData["text_normalized_string"] = newList



# %%

scripturesAndJournal = journalsData[journalsData['text_normalized_string'].isin(matchDict.keys())]

# %%
scripturesAndJournal["book_ref"] = matchDict.values()
scripturesAndJournal.reset_index()

# %%
for entry, books in matchDict.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
    if books == ['job', 'daniel', 'john', 'job', 'john']:
        print(entry)



# %%

'''
for entry in smalljdb["text_normalized"]:
    matchScore = 0
    if type(entry) == list:
        for word in entry:
            for scripture in scriptureData["scripture_text_normalized"]:
                for holy_word in scripture:
                    if holy_word == word:
                        matchScore += 1
                    else:
                        matchScore = 0
                    if matchScore > 5:
                        if scripture not in matchDict.keys():
                            matchDict[scripture] = [entry]
                        else:
                            matchDict[scripture].append(entry) 
'''
# %%
scripturesAndJournal.reset_index().text_normalized_string[[0]].to_list()