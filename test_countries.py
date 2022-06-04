import pytest
import pandas as pd
from countries import Countries
from app import get_information
from app import process_data

def test_get_lenguages():
    countries=Countries()
    response=countries.get_lenguages('Angola')
    assert type(response)== dict
    assert response['Language']=='dfc8646749106ed5ac8a42a2f48251bd1df3cbe7'
    assert response['Time'] < 1

def test_get_information():
    response = get_information()
    assert type(response) == list
    assert response[0]['City Name'] == 'Angola'
    assert len(list(response[0].keys())) == 4

def test_process_data_empty():
    response = process_data([])
    assert response=='Data empty'

def test_process_data_with_information():
    data=pd.read_csv('mock_countries.csv')
    data.to_dict('records')
    response = process_data(data)
    assert response=='Data insert'