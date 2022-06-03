#from turtle import textinput
import pandas as pd
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import unidecode
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from scipy.spatial import distance

class deepdj_processing:

    def __init__(self, _name):

        # Read lyric data
        self.df = pd.read_csv(_name)

        # Clean data
        self.df['cleaned'] = self.df['lyrics'].apply(self.cleaning)

        # Vectoriye
        self.vectorizer = TfidfVectorizer(max_df = 0.5, max_features = 5000, ngram_range=(1,2))
        self.vectorizing('lyrics')


    def prompt_process(self, text_input):
        # Read text prompt
        self.prompt()

        # Clean data
        self.df_prompt['cleaned'] = self.df_prompt['prompt'].apply(self.cleaning)

        # Vectoriye
        self.vectorizing('prompt')

        # Return closest value
        self.cos_distance()
        return self.closest

    def prompt(self, text_input):
        """input the prompt"""
        self.df_prompt= pd.DataFrame({'prompt':text_input}, index = pd.RangeIndex(0,1))

    def cleaning(self, lyric):
    # Basic cleaning
        sentence = lyric.strip() ## remove whitespaces
        sentence = sentence.lower() ## lowercasing
        sentence = ''.join(char for char in sentence if not char.isdigit()) ## removing numbers
        sentence = unidecode.unidecode(sentence) # remove accents
        for punctuation in string.punctuation:
            sentence = sentence.replace(punctuation, '') ## removing punctuation
    # Advanced cleaning
        tokenized_sentence = word_tokenize(sentence) ## tokenizing
        stop_words = set(stopwords.words('english')) ## defining stopwords
        tokenized_sentence = [w for w in tokenized_sentence
                                    if not w in stop_words] ## remove stopwords
        lemmatized_sentence = [WordNetLemmatizer().lemmatize(word, pos = 'v')  # v --> verbs
                for word in tokenized_sentence]
        lemmatized_sentence_2 = [WordNetLemmatizer().lemmatize(word, pos = 'n')  # n --> nouns
                for word in lemmatized_sentence]

        cleaned_sentence = ' '.join(word for word in lemmatized_sentence_2)

        return cleaned_sentence


    def vectorizing(self, case):
        if case=='lyrics':
            self.vectorized_lyrics = pd.DataFrame(self.vectorizer.fit_transform(self.df['cleaned']).toarray(),
                                    columns = self.vectorizer.get_feature_names_out())
        elif case =='prompt':
            print(self.df_prompt)
            self.vectorized_prompt = pd.DataFrame(self.vectorizer.transform(self.df_prompt['cleaned']).toarray(),
                                            columns = self.vectorizer.get_feature_names_out())
            print(self.vectorized_prompt)


    def cos_distance(self):
        self.df["distance"] = [distance.cosine(self.vectorized_lyrics.iloc[k], self.vectorized_prompt) for k in range(len(self.vectorized_lyrics))]
        self.closest = self.df["distance"].nsmallest(60)
