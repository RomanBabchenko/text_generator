import nltk
import re
import random
from collections import Counter
from nltk.tokenize import WhitespaceTokenizer

f = open("corpus.txt", "r", encoding="utf-8").read()
tokens = WhitespaceTokenizer().tokenize(f)
trigrams = list(nltk.trigrams(tokens))
tokens_dict = {}

for fist, second, tail in trigrams:
    tokens_dict.setdefault(f"{fist} {second}", []).append(tail)

for token in tokens_dict:
    tokens_dict[token] = Counter(tokens_dict[token])


def generate():
    for n in range(0, 10):
        while True:
            head = random.choice(list(tokens_dict.keys()))
            first = head.split()[0]
            if first.istitle() and not re.match(r'.+[!?,.]$', first):
                break
        sentence = head.split()
        while True:
            next_word = random.choices(list(tokens_dict[head].keys()), weights=list(tokens_dict[head].values()))[0]
            sentence.append(next_word)
            head = ' '.join(sentence[-2:])
            if len(sentence) >= 5 and re.match(r'.+[!?.]$', head):
                break
        print(*sentence, sep=' ', end='\n')


if __name__ == '__main__':
    generate()
