import pandas as pd
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import unidecode
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


def get_data():
    """method to load lyrics dataset """

    df = pd.read_csv('data/tcc_ceds_music_cleaned.csv')
    return df



def cleaning(lyric):
# Basic cleaning
    sentence = sentence.strip() ## remove whitespaces
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



def vectorizing(cleaned_sentence):
    vectorizer = TfidfVectorizer(max_df = 0.5, max_features = 5000, ngram_range=(1,2))
    vectorized_lyrics = pd.DataFrame(vectorizer.fit_transform(cleaned_sentence).toarray(),
                                columns = vectorizer.get_feature_names_out())
    return vectorized_lyrics

if '__name__' == '__main__':
    df = read_csv()
    df['lyrics_cleaned'] = df['lyrics'].apply(cleaning)
    df_input = input()
    vectorize_input(df_input)
    print(find_cosine_distance())

#process new data, text prompt
#in case of text promt: accept string and return a vector
#in case of new data: read new file (csv) and return
