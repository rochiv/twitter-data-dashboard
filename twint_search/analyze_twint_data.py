import string
import pandas as pd

from collections import Counter


path = '../data/september_data_cleaned.csv'

CAR_MAKE_LIST = ['mercedes', 'bmw', 'lexus', 'ford', 'honda', 'toyota', 'chevrolet', 'audi', 'nissan', 'land rover',
                 'subaru', 'tesla', 'hyundai', 'GMC', 'jaguar', 'volvo', 'volkswagen', 'rivian', 'dodge', 'jeep']

# Stop Words for omission during Lexical Frequency Counts
stopwords = ['a', 'about', 'above', 'across', 'after', 'afterwards']
stopwords += ['again', 'against', 'all', 'almost', 'alone', 'along']
stopwords += ['already', 'also', 'although', 'always', 'am', 'among']
stopwords += ['amongst', 'amoungst', 'amount', 'an', 'and', 'another']
stopwords += ['any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere']
stopwords += ['are', 'around', 'as', 'at', 'back', 'be', 'became']
stopwords += ['because', 'become', 'becomes', 'becoming', 'been']
stopwords += ['before', 'beforehand', 'behind', 'being', 'below']
stopwords += ['beside', 'besides', 'between', 'beyond', 'bill', 'both']
stopwords += ['bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant']
stopwords += ['co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de']
stopwords += ['describe', 'detail', 'did', 'do', 'done', 'down', 'due']
stopwords += ['during', 'each', 'eg', 'eight', 'either', 'eleven', 'else']
stopwords += ['elsewhere', 'empty', 'enough', 'etc', 'even', 'ever']
stopwords += ['every', 'everyone', 'everything', 'everywhere', 'except']
stopwords += ['few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first']
stopwords += ['five', 'for', 'former', 'formerly', 'forty', 'found']
stopwords += ['four', 'from', 'front', 'full', 'further', 'get', 'give']
stopwords += ['go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her']
stopwords += ['here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers']
stopwords += ['herself', 'him', 'himself', 'his', 'how', 'however']
stopwords += ['hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed']
stopwords += ['interest', 'into', 'is', 'it', 'its', 'itself', 'keep']
stopwords += ['last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made']
stopwords += ['many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine']
stopwords += ['more', 'moreover', 'most', 'mostly', 'move', 'much']
stopwords += ['must', 'my', 'myself', 'name', 'namely', 'neither', 'never']
stopwords += ['nevertheless', 'next', 'nine', 'no', 'nobody', 'none']
stopwords += ['noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of']
stopwords += ['off', 'often', 'on', 'once', 'one', 'only', 'onto', 'or']
stopwords += ['other', 'others', 'otherwise', 'our', 'ours', 'ourselves']
stopwords += ['out', 'over', 'own', 'part', 'per', 'perhaps', 'please']
stopwords += ['put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed']
stopwords += ['seeming', 'seems', 'serious', 'several', 'she', 'should']
stopwords += ['show', 'side', 'since', 'sincere', 'six', 'sixty', 'so']
stopwords += ['some', 'somehow', 'someone', 'something', 'sometime']
stopwords += ['sometimes', 'somewhere', 'still', 'such', 'system', 'take']
stopwords += ['ten', 'than', 'that', 'the', 'their', 'them', 'themselves']
stopwords += ['then', 'thence', 'there', 'thereafter', 'thereby']
stopwords += ['therefore', 'therein', 'thereupon', 'these', 'they']
stopwords += ['thick', 'thin', 'third', 'this', 'those', 'though', 'three']
stopwords += ['three', 'through', 'throughout', 'thru', 'thus', 'to']
stopwords += ['together', 'too', 'top', 'toward', 'towards', 'twelve']
stopwords += ['twenty', 'two', 'un', 'under', 'until', 'up', 'upon']
stopwords += ['us', 'very', 'via', 'was', 'we', 'well', 'were', 'what']
stopwords += ['whatever', 'when', 'whence', 'whenever', 'where']
stopwords += ['whereafter', 'whereas', 'whereby', 'wherein', 'whereupon']
stopwords += ['wherever', 'whether', 'which', 'while', 'whither', 'who']
stopwords += ['whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with']
stopwords += ['within', 'without', 'would', 'yet', 'you', 'your']
stopwords += ['yours', 'yourself', 'yourselves']

# Additional Stop Words for omission during Lexical Frequency Counts
stopwords += ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', ]
stopwords += ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
stopwords += ['time', 'yesterday', 'today', 'tomorrow', 'day', 'week', 'month', 'year', 'years',]
stopwords += ['say', 'new', 'like', 'just', 'says', 'said', 'know', 'going',  "it’s", '—']
stopwords += ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
stopwords += ['look', 'got']
stopwords += CAR_MAKE_LIST

stopwords = set(stopwords)


# Lexical Frequency Functions
def fast_strip_punctuation(s: str) -> str:
    return s.translate(str.maketrans('', '', string.punctuation))


def count_word_frequency(s: str) -> list:
    s = fast_strip_punctuation(s)
    w_list = s.split()

    # Prune Stop Words and lower case
    w_list = [w.lower() for w in w_list if (w.lower() not in stopwords)
              and (w.lower().isalnum() and not w.lower().isnumeric())]

    # Count Frequencies
    freq = Counter(w_list).most_common(50)

    return freq


def read_tweets(csv_path: str) -> pd.DataFrame:
    tweet_df = pd.read_csv(csv_path)

    tweets = tweet_df['tweet']
    input_string = ''

    for tweet in tweets:
        input_string += ' ' + tweet

    dict_make_tweets = dict()

    for car in CAR_MAKE_LIST:
        dict_make_tweets[car] = ''

    for df_index, row in tweet_df.iterrows():
        for car in CAR_MAKE_LIST:
            if tweet_df.at[df_index, 'make'] == car:
                dict_make_tweets[car] += tweet_df.at[df_index, 'tweet']

    for car in CAR_MAKE_LIST:
        local_list = count_word_frequency(dict_make_tweets[car])
        dict_make_tweets[car] = local_list

    word_freq_list = list()

    for key, value in dict_make_tweets.items():
        for tup in value:
            word_freq_list.append([key, tup[0], tup[1]])

    word_freq_df = pd.DataFrame(data=word_freq_list, columns=['make', 'word', 'count'])

    word_freq_df.to_csv('word_frequency_table.csv', index=False)

    return word_freq_df


# read_tweets(path)
