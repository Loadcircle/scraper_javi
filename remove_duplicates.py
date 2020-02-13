import re
import pandas as pd


df = pd.read_excel('CNKI_final_excel_2020.xlsx') #PARA LEER EXCEL

# df = pd.read_csv(r'C:\Users\PC\Desktop\CNKI_final_db.csv') #PARA LEER CSV


print(df.count())
    
    
df.drop_duplicates(subset=['Author', 'Title'])

print(df.count())


# try:
#     export_csv = df.to_csv (r'C:\Users\PC\Desktop\CNKI_CSV.csv', index = None, encoding='utf_32') #Don't forget to add '.csv' at the end of the path
#     print('Csv exportado')

# except Exception as e: 
#     print(e)

# try:
#     export_excel = df.to_excel (r'C:\Users\PC\Desktop\CNKI_EXCEL.xlsx)', index = None, encoding='utf_32')
#     print('Excel exportado')

# except Exception as e:
#     print(e)