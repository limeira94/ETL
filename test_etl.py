import pandas as pd
import pytest
from etl import ExcelToOracleETL

@pytest.fixture()
def etl():
    return ExcelToOracleETL

def test_load_excel(etl):
    file_path = "./dados/dados_mercado.xlsx"
    result = etl.load_excel(file_path)
    assert result is not None

def test_connection(etl):
    result = etl.connect_oracle()
    assert result

def test_insert_data_oracle():
    data = {'coluna1': [1, 2, 3], 'coluna2': ['A', 'B', 'C']}
    df = pd.DataFrame(data)

    result = etl.insert_data(df)
    assert result is True