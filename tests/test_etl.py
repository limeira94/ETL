import pandas as pd
import pytest

from etl.etl import ExcelToOracleETL


@pytest.fixture()
def etl():
    return ExcelToOracleETL


def test_load_excel():
    file_path = './dados/dados_mercado.xlsx'
    etl = ExcelToOracleETL(file_path)
    result = etl.load_excel()
    assert result is not None


def test_connection(etl):
    result = etl.connect_oracle()
    assert result


def test_insert_data_oracle():
    data = {'codigo': ['A', 'B', 'C'], 'quantidade': [1, 2, 3]}
    df = pd.DataFrame(data)
    etl = ExcelToOracleETL(df)
    result = etl.insert_data(df)
    assert result is True
