from Countries import Countries
import pandas as pd

countries = Countries()

def process_data(data_regions):
    if len(data_regions) > 0:
        df = pd.DataFrame.from_dict(data_regions)
        total=df['Time'].sum()
        _max=df['Time'].max()
        _min=df['Time'].min()
        _mean=df['Time'].mean()

        values_time=(total,_max,_min,_mean)
        #TODO Enviar a sqlite

        df.to_json('data.json',indent=2,force_ascii=False,orient='records')
    else:
        print("No se proceso por que la longitud es 0")

def main():
    iterations=[]
    for number in range(10):
        regions = countries.get_lenguages("Angola") 
        if 'error' in list(regions.keys()):
            print(f'Error en {regions["error"]}')
        iterations.append(regions)
    
    process_data(iterations)

if __name__ == "__main__":
    
    main()
