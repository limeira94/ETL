import os

import cx_Oracle
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


class ExcelToOracleETL:
    def __init__(self, fp):
        self.file_path = fp

    def load_excel(self):
        try:
            df = pd.read_excel(self.file_path)
            return df
        except Exception as e:
            print(f'Erro ao carregar o arquivo Excel: {str(e)}')
            return None

    @staticmethod
    def connect_oracle():
        try:
            conn = cx_Oracle.connect(
                user=os.getenv('DB_USERNAME'),
                password=os.getenv('DB_PASSWORD'),
                dsn=os.getenv('DB_HOST'),
                encoding='UTF-8',
            )
            return conn
        except Exception as e:
            raise ConnectionError(
                f'Não foi possível conectar ao banco de dados - {e}'
            )

    def insert_data(self, df):
        try:
            conn = self.connect_oracle()
            cursor = conn.cursor()
            data = df.to_dict(orient='records')
            for d in data:
                insert = 'INSERT INTO quantidade (codigo, quantidade) VALUES (:1, :2)'
                cursor.execute(insert, tuple(d.values()))
            conn.commit()
            cursor.close()
            conn.close()
            return True

        except Exception as e:
            print(
                f'Erro ao inserir os dados no banco de dados Oracle: {str(e)}'
            )
            return False


def main():
    fp = './dados/dados_mercado.xlsx'
    etl = ExcelToOracleETL(fp)
    df = etl.load_excel()
    etl.insert_data(df)


if __name__ == '__main__':
    main()
