from Bible import Bible
b = Bible()

with open("/Users/song-yeji/Desktop/p/FinalExam/bible-3letter.txt", "rt") as fin:
    book_abbr_names = fin.read().splitlines()


with open("/Users/song-yeji/Desktop/p/FinalExam/bible-fullname.txt", "rt") as fin:
    book_full_names = fin.read().splitlines()



full2abbrev = {}

for i in range(66):
    full2abbrev[book_full_names[i]] = book_abbr_names[i]

# print(full2abbrev)


abbrev2full = {}

for i in range(66): 
    abbrev2full[book_abbr_names[i]] = book_full_names[i]

print(abbrev2full["Zep"])