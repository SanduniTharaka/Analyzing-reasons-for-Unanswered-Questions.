import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import re
from collections import Counter 

text="සති ගණනවක් එක දිගට තදින් පායන්නට විය. මහ පොළොව වියළී ඉරි තලා ගොසිනි. දිය කඩිති සිඳි ගොසිනි. වාලුකා කාන්තාර සේ පෙනෙයි. නියගයට අසු වූ ගහ කොළ වියලි ගොස් දර අකුල් බවට පත්ව තිබේ. ගොවි තැන් පාලු වී යාම නිසා මහ ජනතාව අසිරුතාවන්ට මුහුණ දෙති. ඔවුහු පානිය ජලය සොයා ගව් ගණන් දුර ඇවිද යති. විඩාවට පත් ජනතාව වැසි ඉල්ලා දෙවියන්ට කන්නල්ව් කරති. රජයේ නිලධාරිහු පැමිණ ගමට නියං සහනාධාර බෙදති. වියලි ආහාරයන්ට අමතරව පැතිර යන රෝග වළක්වා ගැනීමට උපදෙස් සපයති."

sentencesList=sent_tokenize(text)
wordList=[]
for sentence in sentencesList:
    a = re.sub(r'[,.)(\']','',sentence)
    wordList.extend(word_tokenize(a))

print(sentencesList)

print(wordList)

word_length=len(wordList)

plt.rcParams["font.family"]= "Iskoola Pota"

fdist = FreqDist(wordList)
print(fdist)
fdist.plot()
fdist.plot(word_length, cumulative=True)

