
from unicodedata import name
import pandas as pd
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import unidecode
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.spatial import distance
import pickle

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

class deepdj_processing:

    def __init__(self, _name):
        self._name = _name

        # Read lyric data
        self.df = pd.read_csv(_name)

# #    STEP 1: PRODUCE PICKLE FILES OF VECTORIZER AND VECTORIZED LYRICS

        # self.create_pickles()


    #STEP 2: LOAD PICKLE FILES: VECTORIZER and VECTORIZED LYRICS
        self.vectorizer = pickle.load(open('tfidf.pickle','rb'))
        self.vectorized_lyrics = pd.DataFrame(pd.read_pickle('vectorized_lyrics.pickle'))

    def create_pickles(self):
        self.df = pd.read_csv(self._name)
        self.df['cleaned'] = self.df['lyrics'].apply(self.cleaning)
        self.pickle_vectorizer = TfidfVectorizer(max_df = 0.5, max_features = 5000, ngram_range=(1,2))
        self.vectorized_lyrics = pd.DataFrame(self.pickle_vectorizer.fit_transform(self.df['cleaned']).toarray(),
                                    columns = self.pickle_vectorizer.get_feature_names_out())

        self.vectorized_lyrics.to_pickle('vectorized_lyrics.pickle')
        pickle.dump(self.pickle_vectorizer, open('tfidf.pickle','wb'))


    def prompt_process(self, text_input):

        # Read text prompt
        self.prompt(text_input)

        # Clean data
        self.df_prompt['cleaned'] = self.df_prompt['prompt'].apply(self.cleaning)

        # READ VECTORIZER and vectorize prompt

        self.vectorized_prompt = pd.DataFrame(self.vectorizer.transform(self.df_prompt['cleaned']).toarray(),
                                            columns = self.vectorizer.get_feature_names_out())

        #output closest songs
        if text_input=='':
            return 0
        else:
            self.cos_distance()
            return self.closest


    def prompt(self, text_input):
        """input the prompt"""
        self.df_prompt= pd.DataFrame({'prompt':text_input}, index = pd.RangeIndex(0,1))

    def cleaning(self, lyric):
    # Basic cleaning
        sentence = lyric.strip() ## remove whitespaces
        print("remove whitespaces")
        sentence = sentence.lower() ## lowercasing
        print("lowercasing")
        sentence = ''.join(char for char in sentence if not char.isdigit()) ## removing numbers
        print("removing numbers")
        sentence = unidecode.unidecode(sentence) # remove accents
        print("removing accents")
        for punctuation in string.punctuation:
            sentence = sentence.replace(punctuation, '') ## removing punctuation
        print("removing punctuation")
    # Advanced cleaning
        tokenized_sentence = word_tokenize(sentence) ## tokenizing
        print("tokenizing")
        stop_words = set(stopwords.words('english')) ## defining stopwords
        print("defining stopwords")
        tokenized_sentence = [w for w in tokenized_sentence
                                    if not w in stop_words] ## remove stopwords
        print("removing stopwords")
        # lemmatized_sentence = [WordNetLemmatizer().lemmatize(word)  # v --> verbs
        #         for word in tokenized_sentence]
        # print("lemmatizing")
        # lemmatized_sentence_2 = [WordNetLemmatizer().lemmatize(word, pos = 'n')  # n --> nouns
        #         for word in lemmatized_sentence]
        # print("lemmatizing nouns")
        cleaned_sentence = ' '.join(word for word in tokenized_sentence)
        print("joining words in sentence")

        return cleaned_sentence


    def cos_distance(self):
        self.df["distance"] = [distance.cosine(self.vectorized_lyrics.iloc[k], self.vectorized_prompt) for k in range(len(self.vectorized_lyrics))]
        self.closest = self.df["distance"].nsmallest(20)
