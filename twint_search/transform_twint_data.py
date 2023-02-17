import pandas as pd


CAR_MAKE_LIST = ['mercedes', 'bmw', 'lexus', 'ford', 'honda', 'toyota', 'chevrolet', 'audi', 'nissan', 'land rover',
                 'subaru', 'tesla', 'hyundai', 'GMC', 'jaguar', 'volvo', 'volkswagen', 'rivian', 'dodge', 'jeep']


def transform_csv(data_csv_path: str, outfile_csv_path=None) -> pd.DataFrame:
    updated_twint_df = pd.read_csv(data_csv_path)

    # pd.set_option('display.max_rows', None)

    updated_twint_df.drop(
        ['id', 'conversation_id', 'created_at', 'time', 'timezone', 'user_id', 'place', 'language', 'mentions', 'urls',
         'photos', 'hashtags', 'cashtags', 'link', 'retweet', 'quote_url', 'video', 'thumbnail', 'geo', 'source',
         'user_rt_id', 'user_rt', 'retweet_id', 'reply_to', 'retweet_date', 'translate', 'trans_src', 'trans_dest'],
        axis=1, inplace=True)

    updated_twint_df['make'] = None

    for df_index, row in updated_twint_df.iterrows():
        index_tweet = updated_twint_df.at[df_index, 'tweet']
        update_make = search_car(index_tweet)
        updated_twint_df.at[df_index, 'make'] = update_make

        if updated_twint_df.at[df_index, 'make'] == 'None' or updated_twint_df.at[df_index, 'make'] is None:
            updated_twint_df = updated_twint_df.drop(index=df_index)

    print(updated_twint_df)

    if outfile_csv_path is not None:
        updated_twint_df.to_csv(outfile_csv_path, index=False)

    return updated_twint_df


def search_car(tweet):
    make = None
    for i in CAR_MAKE_LIST:
        if i.lower() in tweet.lower():
            make = i

    return make
