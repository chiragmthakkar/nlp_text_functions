import re
import pandas as pd
import contractions
import nltk
# nltk.download()
# from nltk.corpus import stopwords
# stopwords = set(stopwords.words('english'))
from spacy.lang.en import English
from spacy.lang.en.stop_words import STOP_WORDS


def remove_stopwords(text: str):
    """
    Removes stop words from a given string. NLTK stopwords are used for getting the list of stop words
    :param text: Takes in input as a  string
    :return: Returns string without any stopwords
    """

    # Load English tokenizer, tagger, parser, NER and word vectors
    nlp = English()

    #  "nlp" Object is used to create documents with linguistic annotations.
    my_doc = nlp(text)

    # Create list of word tokens
    token_list = []
    for token in my_doc:
        token_list.append(token.text)

    # Create list of word tokens after removing stopwords
    filtered_sentence = []

    for word in token_list:
        lexeme = nlp.vocab[word]
        if lexeme.is_stop is False:
            filtered_sentence.append(word)
    clean_text = ' '.join(filtered_sentence)
    return clean_text


def remove_email(text):
    """
    Removes email from the given string
    :param text: Takes in input as a string
    :return: Returns string without email address
    """

    e = '\S*@\S*\s?'
    clean_text = re.sub(e, '', text)
    return clean_text

def remove_brackets(text):
    """
    Removes brackets from a given string
    :param text: Takes in input as a string
    :return: Returns string without brackets
    """

    e = '[\([{})\]]'
    clean_text = re.sub(e, '', text)
    return clean_text

def remove_numbers(text):
    """
    Removes numbers from a given string
    :param text: Takes in input as a string
    :return: Returns string without numbers
    """

    e = r'[0-9]+'
    clean_text = re.sub(e, '', text)
    return clean_text

def remove_punctuations(text):
    """
    Removes punctutaions and replaces with a ' ' (space)
    :param text: Takes in input as a string
    :return: Returns string without any punctuations. Punctutaions are replaced by ' ' (space)
    """

    e = r'[^a-zA-Z0-9]'
    clean_text = re.sub(e, ' ', text)
    return clean_text

def remove_extraspace(text):
    """
    Removes extra space from
    :param text:
    :return:
    """
    e = '\n|\t'
    clean_text = re.sub(e, '', text)
    return clean_text

def remove_wideextraspace(text):
    # can also use \s\s+
    e = ' +'
    clean_text = re.sub(e, ' ', text)
    return clean_text

def expand_contractions(text):
    # This also expands slang's
    expanded_text = contractions.fix(text, slang=True)
    return expanded_text

def text_preprocessing(text):
    # text = remove_punctuations(text)
    text = expand_contractions(text)
    text = remove_brackets(text)
    text = remove_email(text)
    text = remove_numbers(text)
    text = text.lower()
    text = remove_extraspace(text)

    # Use this at last as in case of milk-shake --> milk shake
    text = remove_punctuations(text)

    text = remove_wideextraspace(text)
    # removes new lines, tab's at the start and end of the string
    text = text.strip()

    return text


if __name__ == '__main__':
    text = ['\tWh  ere \n 98 i2s "my"" Milk\tshake? I\'ll have it sdfs@fsdf.com\n', '\n{s2{}d]f[]ds()f sdf@sdf.com']
    df = pd.DataFrame(text, columns=['text'])
    print(df['text'])
    print(df['text'].apply(text_preprocessing))
    print(df['text'].apply(text_preprocessing).apply(remove_stopwords))

