import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)
def get_year_from_date(row):
    return row['date'][0:4]
df['years'] = df.apply(get_year_from_date, axis=1)

def get_big_mac_price_by_year(year,country_code):
    country_code = country_code.upper()
    query = f"years == '{year}' and iso_a3 == '{country_code}'"
    df2 = df.query(query)
    average = df2['dollar_price'].mean()
    rounded = round(average, 2)
    return rounded

def get_big_mac_price_by_country(country_code):
    country_code = country_code.upper()
    query = f"iso_a3 == '{country_code}'"
    df2 = df.query(query)
    average = df2['dollar_price'].mean()
    rounded = round(average, 2)
    return rounded

def get_the_cheapest_big_mac_price_by_year(year):
    query = f"years == '{year}'"
    df2 = df.query(query)
    min = df2['dollar_price'].idxmin()
    min_loc = df2.loc[min]
    message = f"{min_loc['name']}({min_loc['iso_a3']}): ${min_loc['dollar_price'].round(2)}"
    return message

def get_the_most_expensive_big_mac_price_by_year(year):
    query = f"years == '{year}'"
    df2 = df.query(query)
    max = df2['dollar_price'].idxmax()
    max_loc = df2.loc[max]
    message = f"{max_loc['name']}({max_loc['iso_a3']}): ${max_loc['dollar_price'].round(2)}"
    return message

if __name__ == "__main__":
    per_year3 = get_the_most_expensive_big_mac_price_by_year('2014')
    print(per_year3)
    # git
    #hello