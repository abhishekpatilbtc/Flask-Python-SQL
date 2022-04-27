import sqlite3
import sys
import pandas as pd

temp = sys.argv
if len(sys.argv) != 2:
    raise ValueError('Please provide csv file.')
else:
    file = sys.argv[1]



conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute(
    '''CREATE TABLE MainDB (nr_cnpj text, nm_fantasia text, sg_uf text, in_cpf_cnpj text, nr_cpf_cnpj_socio text, cd_qualificacao_socio text, ds_qualificacao_socio text, nm_socio text)''')

df = pd.read_csv(file, sep='\t', error_bad_lines=False, dtype=str)
print(df.head(10))

df.to_sql('MainDB', conn, if_exists='append', index=False)
# Committing the changes
conn.commit()

# closing the database connection
conn.close()