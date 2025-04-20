import pandas as pd

WIKI_URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

def fetch_sp500_list() -> pd.DataFrame:
    tables = pd.read_html(WIKI_URL)
    dataframe = tables[0]
    dataframe = dataframe[['Symbol', 'Security', 'GICS Sector', 'GICS Sub-Industry']]
    dataframe.columns = ['symbol', 'name', 'sector', 'industry']
    return dataframe

if __name__ == "__main__":
    df = fetch_sp500_list()
    print(df.head())