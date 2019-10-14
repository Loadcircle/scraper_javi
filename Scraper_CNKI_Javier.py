
# coding: utf-8

# In[74]:


from bs4 import BeautifulSoup
import pandas as pd


# In[53]:


soup = BeautifulSoup(open("CNKI-637066357426093750.html"), "xml")


# In[54]:


soup


# In[106]:


df2 = pd.DataFrame()

for d in soup.findAll('DATA'):
    try:
        title = (d.Title.text)
    except AttributeError:
        title = 'none'
        
    try:
        author = (d.Author.text)
    except AttributeError:
        author = ('none')
        
    try:
        src = (d.Source.text)
    except AttributeError:
        src =('none')
        
    try:
        year = (d.Year.text)
    except AttributeError:
        year = ('none')
        
    try:
        keyw = (d.Keyword.text)
    except AttributeError:
        keyw = ('none')
    
    try:
        summ = (d.Summary.text)
    except AttributeError:
        summ = ('none')
        
    try:
        db = (d.SrcDatabase.text)
    except AttributeError:
        db = ('none')
        
    try:
        organ = (d.Organ.text)
    except AttributeError:
        organ = ('none')
        
    try:
        link = (d.Link.text)
    except AttributeError:
        link = ('none')


    temp = pd.DataFrame({'Title': title, 'Author': author,'Source':src, 'Year': year,
                         'Keywords': keyw, 'Summary':summ, 'SourceDatabase':db,
                         'Organ':organ, 'Link': link}, index =[0])
    
    #print((temp))

    df2 = pd.concat([df2, temp])


# In[107]:


df2 = df2.reset_index(drop=True)


# In[108]:


df2


# In[109]:


df2.to_csv('cnki_results.csv')


# In[110]:


try:
    export_csv = df2.to_csv (r'CNKI_file.csv', index = None, encoding='utf_32') #Don't forget to add '.csv' at the end of the path
    print('Csv exportado')

except Exception as e: 
    print(e)

try:
    export_excel = df2.to_excel (r'CNKI_file.xlsx)', encoding='utf_32')
    print('Excel exportado')

except Exception as e:
    print(e)


# In[111]:


df2.to_excel (r'CNKI_file.xlsx)', encoding='utf_32')

