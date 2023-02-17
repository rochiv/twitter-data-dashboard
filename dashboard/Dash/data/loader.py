import pandas as pd

CAR_MAKE_LIST = ['mercedes', 'bmw', 'lexus', 'ford', 'honda', 'toyota', 'chevrolet', 'audi', 'nissan', 'land rover',
                 'subaru', 'tesla', 'hyundai', 'GMC', 'jaguar', 'volvo', 'volkswagen', 'rivian', 'dodge', 'jeep']


class DataSchema:
    DATE = "date",
    USERNAME = "username",
    NAME = "name",
    TWEET = "tweet",
    REPLIES_COUNT = "replies_count",
    RETWEETS_COUNT = "retweets_count",
    LIKES_COUNT = "likes_count",
    NEAR = "near",
    MAKE = "make"


def load_transaction_data(path: str) -> pd.DataFrame:
    # load the data from a CSV file
    data = pd.read_csv(
        path,
        dtype={
            DataSchema.DATE: str,
            DataSchema.USERNAME: str,
            DataSchema.NAME: str,
            DataSchema.TWEET: str,
            DataSchema.REPLIES_COUNT: str,
            DataSchema.RETWEETS_COUNT: str,
            DataSchema.LIKES_COUNT: str,
            DataSchema.NEAR: str,
            DataSchema.MAKE: str,
        }
    )
    # pd.set_option('display.max_rows', None)

    return data
