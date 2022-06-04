from countries import Countries
from persistence import DB
import pandas as pd

db = DB()
countries = Countries()

def process_data(data_regions):
    if len(data_regions) > 0:
        df = pd.DataFrame.from_dict(data_regions)
        print(df)
        _total= "{0:.2f}".format(df['Time'].sum())
        _max= "{0:.2f}".format(df['Time'].max())
        _min="{0:.2f}".format(df['Time'].min())
        _mean="{0:.2f}".format(df['Time'].mean())
        values_time=(_total,_max,_min,_mean)
        db.insert_times(values_time)
        df.to_json('data.json',indent=2,force_ascii=False,orient='records')
        df.to_csv('mock_countries.csv',index=False)
        return 'Data insert'
    else:
        print("It is not processed because the length is 0")
        return 'Data empty'
def get_information(name_countrie='Angola'):
    iterations=[]
    for number in range(10):
        regions = countries.get_lenguages(name_countrie) 
        if 'error' in list(regions.keys()):
            print(f'Error en {regions["error"]}')
        iterations.append(regions)
    return iterations    

def main():
    information_countrie=get_information()
    process_data(information_countrie)

if __name__ == "__main__":
    main()
