#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from os import path, getcwd
import json

def wordcloud_data(data , choice):
    
   # with open('reviews.json', 'r') as myfile: #Reads the Json file 
        
        #data= myfile.read()
    
    obj = json.loads(data) 

    
    #df = pd.read_csv(str(csv))
    
    #choice = input("Data or wordcloud or both?")
    
    if choice == 'data':
        #df_1 = df.loc[df['Title'] == str(title)]
        
        
        #text = " ".join(review for review in df_1.Clean_Text)
        
        text = ' '.join(obj)
        
        wordlist = text.split()
        
        wordfreq = [wordlist.count(p) for p in wordlist]
        
        dict = {'Words': wordlist, 'Frequency': wordfreq}
        
        Dict = dict
        
        freq_data = pd.DataFrame.from_dict(Dict)
        
        fd = freq_data.loc[freq_data['Frequency'] >= 3]
        
        fd = fd.drop_duplicates(keep='first')
        
        print(fd.head())

        return fd.head()
        
    elif choice == 'wordcloud' :
        
        import matplotlib.pyplot as plt
        #df_1 = df.loc[df['Title'] == str(title)]
        
        #text = " ".join(review for review in df_1.Clean_Text)
        
        text = ' '.join(obj)
        
        WC = WordCloud(background_color="white" , max_font_size = 50,max_words = 200, height = 400, width = 700, collocations = False)
        
        dic = WC.process_text(text)

        test = {}
        for k, v in dic.items():
            if v >= 3:
                test.update({k:v})


        img = WC.fit_words(test)  #buiding the wordcloud with the updated frequency dictinary

        plt.imshow(img)
        plt.axis('off')
        plt.tight_layout(pad=0)
        plt.show()
    
    else:
        
        import matplotlib.pyplot as plt
        
        #df_1 = df.loc[df['Title'] == str(title)]
        
        #text = " ".join(review for review in df_1.Clean_Text)
        
        text = ' '.join(obj)
        
        
        wordlist = text.split()
        
        wordfreq = [wordlist.count(p) for p in wordlist]
        
        dict = {'Words': wordlist, 'Frequency': wordfreq}
        
        Dict = dict
        
        freq_data = pd.DataFrame.from_dict(Dict)
        
        fd = freq_data.loc[freq_data['Frequency'] >= 3]
        
        fd = fd.drop_duplicates(keep='first')
        
        print(fd.head())
        
        #text = " ".join(review for review in df_1.Clean_Text)
        
        WC = WordCloud(background_color="white" , max_font_size = 50,max_words = 200, height = 400, width = 700, collocations = False)
        
        dic = WC.process_text(text)

        test = {}
        for k, v in dic.items():
            if v >= 3:
                test.update({k:v})


        img = WC.fit_words(test)  #buiding the wordcloud with the updated frequency dictinary

        plt.imshow(img)
        plt.axis('off')
        plt.tight_layout(pad=0)
        plt.show()
    
    

        
if __name__ == '__main__':
    wordcloud_data(*sys.argv[1:])

