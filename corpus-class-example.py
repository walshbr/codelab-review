import glob
import nltk

class Corpus:
    def __init__(self, corpus_dir):
        self.corpus_directory = corpus_dir
        # self.attribute = something_you_give_it
        # that becomes available downstream as object.attribute
        self.filenames = glob.glob(self.corpus_directory + '*.txt')
        # produce texts from those filenames
        # make a list of text objects using all of our filenames
        self.texts = [Text(filename) for filename in self.filenames]

class Text:
  #copy from lesson doc
    def __init__(self, filename):
        self.filename = filename
        # raw text inside of it
        self.text = open(self.filename, 'r').read()
        # individual words
        self.words = nltk.word_tokenize(self.text)
        self.nltk = nltk.Text(self.words)

corpus_dir = 'corpus/'

our_corpus = Corpus(corpus_dir)

print(our_corpus.corpus_directory)
print(our_corpus.filenames)
print(our_corpus.texts)
for text in our_corpus.texts:
    print('======')
    print(text.text[0:1000])
for text in our_corpus.texts:
    print('=====')
    print(text.words[0:100])

for text in our_corpus.texts:
    print('======')
    print(text.nltk.vocab().most_common(10))