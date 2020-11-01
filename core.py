from collections import Counter
from functools import reduce
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from nltk.text import Text
from collections import OrderedDict
import sys


def most_freq(text: dict, most_common: int = 5):
    try:
        # pre process text
        processed_text = {file: pre_process_text(words) for file, words in text.items()}
        freq_list = most_frequent_words(processed_text, most_common)
        merged_text = " ".join(list(text.values()))
        freq_dict = OrderedDict()
        for word, freq in freq_list:
            # Get the sentences where the most frequent words are found
            word_occurrences = get_concordance(merged_text, word)
            document_list = []
            # get the document names where the most frequent words are found
            for file, words in processed_text.items():
                if word in words:
                    document_list.append(file)

            # combine everything together
            freq_dict[word] = [freq, word_occurrences, document_list]
    except Exception as e:
        print(e)
    return freq_dict


def most_frequent_words(processed_text: dict, most_common: int):
    # returns the most frequent words from a list of words
    counter_list = []
    for _, text in processed_text.items():
        counter_list.append(Counter(text.split(" ")))

    # merge all the counters and get the top most common words
    merged_counter = reduce(lambda x, y: x + y, counter_list)
    return merged_counter.most_common(most_common)


def pre_process_text(text: str) -> str:
    # Remove end lines
    text = text.replace("\n", " ").replace(".", "")
    # get only alphabets and numbers
    text = re.sub('[^a-zA-Z0-9 .]', '', text)

    # remove stop words
    filtered_text = remove_stop_words(text)
    return filtered_text


def remove_stop_words(text: str, stop_words=set(stopwords.words('english'))) -> str:
    """

    removes stop words from a text corpus
    """
    stop_words.add('The')
    text_tokens = word_tokenize(text)
    tokens_without_sw = [word for word in text_tokens if word not in stop_words]
    filtered_sentence = " ".join(tokens_without_sw)
    return filtered_sentence


def get_concordance(text: list, word: str):
    """
    Gets the sentences where the word occurs
    """
    tokenizer = nltk.tokenize.WhitespaceTokenizer()
    nltk_text = Text(tokenizer.tokenize(text))
    concordance_list = nltk_text.concordance_list(word, lines=sys.maxsize)
    return [concordance.line for concordance in concordance_list]


