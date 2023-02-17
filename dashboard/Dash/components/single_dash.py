import pandas as pd
import plotly.express as px
from twint_search import transform_twint_data as ttd
from twint_search import analyze_twint_data as atd


CAR_MAKE_LIST = ['mercedes', 'bmw', 'lexus', 'ford', 'honda', 'toyota', 'chevrolet', 'audi', 'nissan', 'land rover',
                 'subaru', 'tesla', 'hyundai', 'GMC', 'jaguar', 'volvo', 'volkswagen', 'rivian', 'dodge', 'jeep']

FULL_DATA_PATH = '/dashboard/Dash/data/september_data.csv'
MAIN_DATA_PATH = '/Users/rohit/PycharmProjects/PersonalProjects/twintProject/search_app/dashboard/Dash/data/september_data_cleaned.csv'
FREQ_DATA_PATH = '/Users/rohit/PycharmProjects/PersonalProjects/twintProject/search_app/dashboard/Dash/data/word_frequency_table.csv'


main_df = pd.read_csv(MAIN_DATA_PATH)
freq_df = pd.read_csv(FREQ_DATA_PATH)


def make_vs_likes_plot():
    df = main_df['make', 'likes_count'].value_counts().rename_axis('likes_count').reset_index(name='likes_count')
    fig = px.bar(df, x='make', y='likes_count', color='make')
    fig.show()


def make_vs_mention_plot():
    df = main_df['make'].value_counts().rename_axis('make').reset_index(name='mentions')
    fig = px.bar(df, x='make', y='mentions', color='make')
    fig.show()


make_vs_likes_plot()
# make_vs_mention_plot()





