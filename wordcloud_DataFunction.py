#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from os import path, getcwd
import matplotlib.pyplot as plt

def wordcloud_data(df , title , minfreq , maxwords):
    
    choice = input("Data or wordcloud or both?")
    
    if choice == 'Data':
        df_1 = df.loc[df['Title'] == str(title)]
        
        
        text = " ".join(review for review in df_1.Clean_Text)
        
        wordlist = text.split()
        
        wordfreq = [wordlist.count(p) for p in wordlist]
        
        dict = {'Words': wordlist, 'Frequency': wordfreq}
        
        Dict = dict
        
        freq_data = pd.DataFrame.from_dict(Dict)
        
        fd = freq_data.loc[freq_data['Frequency'] >= minfreq]
        
        return fd.head()
        
    elif choice == 'wordcloud':
        df_1 = df.loc[df['Title'] == str(title)]
        
        text = " ".join(review for review in df_1.Clean_Text)
        
        WC = WordCloud(background_color="white" , max_font_size = 50,max_words = maxwords, height = 400, width = 700, collocations = False)
        
        dic = WC.process_text(text)

        test = {}
        for k, v in dic.items():
            if v >= minfreq:
                test.update({k:v})


        img = WC.fit_words(test)  #buiding the wordcloud with the updated frequency dictinary

        plt.imshow(img)
        plt.axis('off')
        plt.tight_layout(pad=0)
        plt.show()
    
    else:
        
        df_1 = df.loc[df['Title'] == str(title)]
        
        text = " ".join(review for review in df_1.Clean_Text)
        
        wordlist = text.split()
        
        wordfreq = [wordlist.count(p) for p in wordlist]
        
        dict = {'Words': wordlist, 'Frequency': wordfreq}
        
        Dict = dict
        
        freq_data = pd.DataFrame.from_dict(Dict)
        
        fd = freq_data.loc[freq_data['Frequency'] >= minfreq]
        
        fd.to_csv("Frequency_Data.csv")
        
        print(fd.head())
        
        text = " ".join(review for review in df_1.Clean_Text)
        
        
        WC = WordCloud(background_color="white" , max_font_size = 50,max_words = maxwords, height = 400, width = 700, collocations = False)
        
        dic = WC.process_text(text)

        test = {}
        for k, v in dic.items():
            if v >= minfreq:
                test.update({k:v})


        img = WC.fit_words(test)  #buiding the wordcloud with the updated frequency dictinary

        plt.imshow(img)
        plt.axis('off')
        plt.tight_layout(pad=0)
        plt.show()
    
    
        
        
        

