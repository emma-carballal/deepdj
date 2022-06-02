import pandas as pd
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import unidecode
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from scipy.spatial import distance
from deepdj_processing import deepdj_processing

def get_data():
    """method to load lyrics dataset """

    df = pd.read_csv('data/tcc_ceds_music_cleaned.csv')
    return df

def prompt():
    """input the prompt"""
    value = input('Please enter a string:\n')
    df = pd.DataFrame({'prompt':value}, index = pd.RangeIndex(0,1))
    return df



def cleaning(lyric):
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

     #def vectorizing_lyrics(df):
       # vectorizer = TfidfVectorizer(max_df = 0.5, max_features = 5000, ngram_range=(1,2))
        ##if df.shape[0] > 1:
        #vectorized_lyrics = pd.DataFrame(vectorizer.fit_transform(df).toarray(),
                                   # columns = vectorizer.get_feature_names_out())
       # return vectorized_lyrics

   # def vectorizing_prompt(df):
        #vectorizer = TfidfVectorizer(max_df = 0.5, max_features = 5000, ngram_range=(1,2))
       # vectorized_value = pd.DataFrame(vectorizer.transform(df).toarray(),
                                    #columns = vectorizer.get_feature_names_out())
        #return vectorized_value

def vectorizing_all(df,case,vectorizer=False):
    if case=='lyrics':
        vectorizer = TfidfVectorizer(max_df = 0.5, max_features = 5000, ngram_range=(1,2))
        vectorized_value = pd.DataFrame(vectorizer.fit_transform(df).toarray(),
                                columns = vectorizer.get_feature_names_out())
        return vectorized_value, vectorizer
    elif case =='prompt':
        vectorized_value = pd.DataFrame(vectorizer.transform(df).toarray(),
                                        columns = vectorizer.get_feature_names_out())
        return vectorized_value

def cos_distance(vectorized_lyrics, vectorized_value):
    df["distance"] = [distance.cosine(vectorized_lyrics.iloc[k], vectorized_value) for k in range(len(vectorized_lyrics))]
    closest = df["distance"].nsmallest(60)
    return closest



if __name__ == '__main__':
    #get, clean and vectorize data
    #df = get_data()
    #df_prompt = prompt()
    #df['cleaned'] = df['lyrics'].apply(cleaning)
    #df_prompt['cleaned'] = df_prompt['prompt'].apply(cleaning)
    #vectorized_lyrics = df['cleaned'].apply(vectorizing)
    #print(df['cleaned'])
    #vectorized_lyrics = vectorizing_lyrics(df['cleaned'])

    #vectorized_lyrics, vectorizer = vectorizing_all(df['cleaned'],'lyrics')
    #print(vectorized_lyrics)
    #vectorized_value = vectorizing_all(df_prompt['cleaned'],'prompt',vectorizer)
    #print(vectorized_value)

    #vectorized_value = df_prompt['cleaned'].apply(vectorizing)
    #vectorized_value = vectorizing_prompt(df_prompt['cleaned'])
    #print (cos_distance(vectorized_lyrics, vectorized_value))
    dj = deepdj_processing('data/tcc_ceds_music_cleaned.csv')
    res = dj.prompt_process()
    print(res)
    res = dj.prompt_process()
    print(res)

#process new data, text prompt
#in case of text promt: accept string and return a vector
#in case of new data: read new file (csv) and return
