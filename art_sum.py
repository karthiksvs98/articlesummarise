from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk import pos_tag
import nltk

text = """Independence Day in India is celebrated as national holiday every year on 15th of August when people remember the long event of independence of our Nation from the British rule. India got independence on August 15th in 1947 after lots of movement of Independence during which many freedom fighters sacrificed their lives. After independence, Jawaharlal Nehru became first Indian Prime Minister on 17th of August in 1947 who raised the National Flag at Red Fort near Lahore Gate in Delhi.

Students, teachers, parents and other people come together to celebrate the Independence Day by unfurling the National Flag and singing National Anthem. Out tricolour National Flag is also hosted by the Indian prime minster in the National capital, New Delhi at Red Fort. After that the salute is given by firing 21 guns and tricolour flower showering is held on the flag with helicopter. The tricolour of our Flag represents saffron for courage and sacrifice, white for peace and truth and green for faith and chivalry.

There is an Ashok chakra in the centre of our Flag which contains 24 spikes distributed evenly. At this special day we remember the great sacrifices of Bhagat Singh, Sukhdev, Raj Guru, Gandhiji and other dared freedom fighters for their unforgettable contribution in the independence of India. Students give speech on the subjects of freedom fighters on the Independence day celebration in schools.

They also involve in parade, march past, singing patriotic songs, etc. Other people celebrate this day according to their own way such as watching patriotic movies, going outside to home with family, meet with friends or participate in the events organized in public places.

"""

stemmer = SnowballStemmer("english")
stopWords = stopwords.words("english")
words = word_tokenize(text)
originlen = len(words)

freqTable = dict()
for word in words:
	word = word.lower()
	if word in stopWords:
		continue

	word = stemmer.stem(word)

	if word in freqTable:
		freqTable[word] += 1
	else:
		freqTable[word] = 1

#print(freqTable)
sentences = sent_tokenize(text)
sentenceValue = dict()
#print(sentences)

for sentence in sentences:
	for word, freq in freqTable.items():
		if word in sentence.lower():
			if sentence in sentenceValue:
				sentenceValue[sentence] += freq
			else:
				sentenceValue[sentence] = freq


sumValues = 0
for sentence in sentenceValue:
	sumValues += sentenceValue[sentence]

average = int(sumValues / len(sentenceValue))


summary = ''
for sentence in sentences:
	if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
		summary += " " + sentence

finallen = len(word_tokenize(summary))
pcnt = (finallen/originlen)*100

print(summary)
print(originlen,"words originally")
print(finallen,"words after reduction")
print(pcnt,"% decrease") 
#print(pos_tag(word_tokenize(summary)))
