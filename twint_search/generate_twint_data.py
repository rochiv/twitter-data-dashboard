import twint
# import nest_asyncio
# nest_asyncio.apply()


CAR_MAKE_LIST = ['mercedes', 'bmw', 'lexus', 'ford', 'honda', 'toyota', 'chevrolet', 'audi', 'nissan', 'land rover',
                 'subaru', 'tesla', 'hyundai', 'GMC', 'jaguar', 'volvo', 'volkswagen', 'rivian', 'dodge', 'jeep']


CITIES_LIST = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego',
               'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'Indianapolis', 'Charlotte',
               'San Francisco', 'Seattle', 'Denver', 'Washington, DC', 'Nashville-Davidson', 'Oklahoma City', 'El Paso',
               'Boston', 'Portland', 'Las Vegas', 'Detroit', 'Memphis', 'Louisville', 'Baltimore', 'Milwaukee',
               'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Kansas City', 'Mesa', 'Atlanta', 'Omaha',
               'Colorado Springs', 'Raleigh', 'Long Beach', 'Virginia Beach', 'Miami', 'Minneapolis', 'Oakland',
               'Tulsa', 'Bakersfield', 'Wichita', 'Arlington']


# twint twitter scraper
def scrape_by_city(keyword: str, since: str, outfile_csv_path: str):

    unique_cities = set(CITIES_LIST)
    cities = sorted(unique_cities)      # Sort & convert datatype to list
    for city in cities:
        print(city)
        c = twint.Config()
        c.Search = keyword     # search keywords
        c.Since = since     # date since
        c.Near = city       # city searched from
        c.Count = True      # shows number of tweets scraped
        c.Stats = False     # count likes, replies, retweets
        c.Verified = True       # searches from verified accounts
        c.Store_csv = True      # Store tweets in .csv file
        c.Output = outfile_csv_path      # location of .csv file
        c.Hide_output = True    # hides output in console; toggle to print tweet in console
        c.Lang = 'en'       # english tweets

        twint.run.Search(c)


# uses scrape_by_city for each car make
def car_makes(date_since: str, store_csv_path: str):
    for car in CAR_MAKE_LIST:
        scrape_by_city(car, date_since, store_csv_path)


def main():
    car_makes('2022-10-12', '../data/new_random.csv')
