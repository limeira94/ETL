import cx_Oracle
import pandas as pd


class ExcelToOracleETL:

    @staticmethod
    def load_excel(file_path):
        try:
            df = pd.read_excel(file_path)
            return df
        except Exception as e:
            print(f"Erro ao carregar o arquivo Excel: {str(e)}")
            return None

    @staticmethod
    def connect_oracle():
        try:
            conn = cx_Oracle.connect(user="system", password="1234", dsn="*****", encoding="UTF-8")
            return conn
        except Exception as e:
            raise ConnectionError(f"Não foi possível conectar ao banco de dados - {e}")

    def insert_data(self, df):
        data = df
        for d in data:
            cursor.execute("INSERT INTO ")
