import re
import pandas as pd


df = pd.read_excel (r'C:\Users\PC\Desktop\ILLAS_EXCEL.xlsx') #for an earlier version of Excel, you may need to use the file extension of 'xls'

# df = pd.read_csv(r'C:\Users\PC\Desktop\ILLAS_CSV.csv')

for i, row in df.iterrows():

    string = row['Titulo']
      
    match =         re.search(r'\bamerica\slatina|\blatinoamerica|\blatin\samerica|\bBrazil|\bPeru|\bPerú|\bMexico|\bColombia|\bArgentina|\bEcuador|\bBolivia|\bParaguay|\bUruguay|\bCosta\sRica|\bPanama|\bHaiti|\bHaiti|\bNicaragua|\bGuatemala|\bVenezuela|\bCuba', string, re.I)
    m_peru =        re.search(r'\blatinoamerica|\bcusco', string, re.I)
    m_brasil =      re.search(r'\bBrasil|\bbrasilian|\bBRICS', string, re.I)
    m_mexico =      re.search(r'\bMéxico|\bmexican|\bmexicanas', string, re.I)
    m_colombia =    re.search(r'\bcolombian', string, re.I)
    m_argentina =   re.search(r'\bargentine|\bbuenos\saires', string, re.I)
    m_ecuatorian =  re.search(r'\becuatorian', string, re.I)
    m_bolivia =     re.search(r'\bbolivian|\bla\spaz', string, re.I)
    m_paraguay =    re.search(r'\bparaguayan', string, re.I)
    m_andean =      re.search(r'\bAndean', string, re.I)
    m_uruguay =     re.search(r'\buruguayan', string, re.I)
    m_haiti =       re.search(r'\bhaitian', string, re.I)
    m_nicaragua =   re.search(r'\bnicaraguan', string, re.I)
    m_guatemala =   re.search(r'\bguatemalan', string, re.I)
    m_venezuela =   re.search(r'\bChavez', string, re.I)
    m_cuba =        re.search(r'\bCuban|\bHabana', string, re.I)
    m_chile =       re.search(r'\bChilean|\bChileno|\bChile', string, re.I)
    m_dominicana =  re.search(r'\bRepública\sDominicana', string, re.I)
    m_marxism =     re.search(r'\bMarxismo', string, re.I)

    if match:
        df.at[i,'Keyword'] = match.group()

    elif m_peru:
        df.at[i,'Keyword'] = 'Peru'

    elif m_brasil:
        df.at[i,'Keyword'] = 'Brazil '
        
    elif m_mexico:
        df.at[i,'Keyword'] = 'Mexico'
        
    elif m_colombia:
        df.at[i,'Keyword'] = 'Colombia'
        
    elif m_argentina:
        df.at[i,'Keyword'] = 'Argentina'
        
    elif m_uruguay:
        df.at[i,'Keyword'] = 'Uruguay'
        
    elif m_haiti:
        df.at[i,'Keyword'] = 'Haiti'
        
    elif m_nicaragua:
        df.at[i,'Keyword'] = 'Nicaragua'
        
    elif m_guatemala:
        df.at[i,'Keyword'] = 'Guatemala'
        
    elif m_venezuela:
        df.at[i,'Keyword'] = 'Venezuela'
        
    elif m_cuba:
        df.at[i,'Keyword'] = 'Cuba'
        
    elif m_chile:
        df.at[i,'Keyword'] = 'Chile'
        
    elif m_dominicana:
        df.at[i,'Keyword'] = 'Dominican Republic'
        
    elif m_marxism:
        df.at[i,'Keyword'] = 'Marxism'
        
    elif m_ecuatorian:
        df.at[i,'Keyword'] = 'Ecuador'
        
    elif m_bolivia:
        df.at[i,'Keyword'] = 'Bolivia'
        
    elif m_paraguay:
        df.at[i,'Keyword'] = 'Paraguay'
        
    elif m_andean:
        df.at[i,'Keyword'] = 'Andean Community'

    date_string = row['Fecha 2']

    match_date = re.search(r'(.{4})\s*$', date_string)

    if match_date:
        df.at[i,'Fecha 2'] = date_string[0:-6]

        df.at[i,'Año'] = match_date.group()



print(df)


try:
    export_csv = df.to_csv (r'C:\Users\PC\Desktop\ILLAS_added_keyword.csv', index = None, encoding='utf_32') #Don't forget to add '.csv' at the end of the path
    print('Csv exportado')

except Exception as e: 
    print(e)

try:
    export_excel = df.to_excel (r'C:\Users\PC\Desktop\ILLAS_added_keyword.xlsx)', index = None, encoding='utf_32')
    print('Excel exportado')

except Exception as e:
    print(e)