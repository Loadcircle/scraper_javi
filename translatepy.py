import re
import pandas as pd
from googletrans import Translator
# from translate import Translator
# translator= Translator(to_lang="es")


df = pd.read_excel (r'C:\Users\PC\Desktop\International order Journal EXCEL.xlsx') #PARA LEER EXCEL

# df = pd.read_csv(r'C:\Users\PC\Desktop\CNKI_final_db.csv') #PARA LEER CSV



for i, row in df.iterrows():
    print('Linea :' + str(i))
    translator = Translator()
    try:
        titulo = row['Title']
        autor = row['Author']
        source = row['Source']

        df.at[i,'Translate_title'] = translator.translate(titulo, dest="es").text
        df.at[i,'Translate_author'] = translator.translate(autor, dest="es").text
        df.at[i,'Translate_source'] = translator.translate(source, dest="es").text


    except Exception as e:
        print(e) 

# print(df)
    

try:
    export_csv = df.to_csv (r'C:\Users\PC\Desktop\CNKI_CSV.csv', index = None, encoding='utf_32') #Don't forget to add '.csv' at the end of the path
    print('Csv exportado')

except Exception as e: 
    print(e)

try:
    export_excel = df.to_excel (r'C:\Users\PC\Desktop\CNKI_EXCEL.xlsx)', index = None, encoding='utf_32')
    print('Excel exportado')

except Exception as e:
    print(e)