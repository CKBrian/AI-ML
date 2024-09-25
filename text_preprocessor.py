#!/usr/bin/env python3
'''Defines a TextPreprocessor class'''

import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk

# Download necessary resources for NLTK
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

class TextPreprocessor:
    '''Defines a class that preprocesses text to NLP accepted format'''
    
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()

    def convert_to_lowercase(self, text):
        '''Converts all text to lowercase'''
        return text.lower()

    def remove_punctuation(self, text):
        '''Removes punctuation from text'''
        return re.sub(r'[^\w\s]', '', text)

    def tokenize_text(self, text):
        '''Splits the text into individual words or tokens'''
        return word_tokenize(text)

    def remove_stopwords(self, words):
        '''Removes common stopwords like and, the'''
        return [word for word in words if word not in self.stop_words]

    def apply_stemming(self, words):
        '''Reduces words to their base form using stemming'''
        return [self.stemmer.stem(word) for word in words]

    def apply_lemmatization(self, words):
        '''Reduces words to their dictionary form using lemmatization'''
        return [self.lemmatizer.lemmatize(word) for word in words]

# Example usage:
preprocessor = TextPreprocessor()
text = "This is an example sentence, with some punctuation!"
lower_text = preprocessor.convert_to_lowercase(text)
no_punctuation_text = preprocessor.remove_punctuation(lower_text)
tokens = preprocessor.tokenize_text(no_punctuation_text)
no_stopwords = preprocessor.remove_stopwords(tokens)
stemmed_words = preprocessor.apply_stemming(no_stopwords)
lemmatized_words = preprocessor.apply_lemmatization(no_stopwords)

print(text, '\n', lower_text, '\n', no_punctuation_text, '\n', tokens, '\n', no_stopwords, '\n', stemmed_words, '\n', lemmatized_words)
