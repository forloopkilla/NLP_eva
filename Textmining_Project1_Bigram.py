
# coding: utf-8

# # Implement a program in java or python that contains a .txt file and the 20 statistically significant most common bigrams (by definition the lecture) on the console.

# In[117]:


import os 
os.getcwd()
os.chdir("C:\\Users\jiany\Documents\School\Speech & Textmining\Project_Aufgabe")


# In[118]:


# -*- coding: utf-8 -*-

text = open('effie.txt')
data = text.read() # turns text into list


# ### Use a tokenizer that only takes words that have no umlauts and language-dependent special characters such as ß or é included. Punctuation marks, as well Uppercase and lowercase letters should also be ignored. Furthermore, everyone should Words that are in the given stopword list stopwords.txt are also availablebe ignored 

# In[119]:


# -*- coding: utf-8 -*-

len(data)
print(data[1:1000])


# In[62]:


type(stopwords)


# In[70]:


stopwords = open('stopwords.txt').readlines() # load in stopwords
len(stopwords)
stopwords[1:10]


# In[63]:


from nltk.tokenize import sent_tokenize, word_tokenize #load in tokenizer


# In[90]:


words = word_tokenize(str(data))
len(words)
stopwords = word_tokenize(str(stopwords))
len(stopwords)


# In[91]:


# cut the stop words
filter_words = []
for w in words:
    if w not in stopwords:
        filter_words.append(w)

#filter_words = str(filter_words)
len(filter_words)


# In[73]:


filter_words[1:100]


# In[74]:


# cut the punctuation and numbers
import re
regex = r"(?<!\d)[.,;:](?!\d)"
word_list = re.sub(regex, "", filter_words, 0)
len(word_list)


# # Likelihood Estimation

# In[ ]:


bigram = pd.frame()
def dunning(p1,k1,n1,p2,k2,n2,data):
    for word in filter_words:
    2[(k1*log(k1/n2)+(n1-k1)*log(1-(k1/n1)))+(k2*log(k2/n2)+(n2-k2)*log(1-(k2/n2)))-(k1*log(((k1+k2)/(n1+n2)))+(n1-k1)*log(1-(k1+k2)/(n1+n2)))-(k2*log((k1+k2)/(n1+n2))+(n2-k2)*log(1-(k1+k2)/(n1+n2)))]
    bigrams.append
    print[bigrams]


# # Log Likelihood Rato Statistics from Github: https://github.com/rsennrich/ParZu/blob/master/preprocessor/punkt_tokenizer.py

# In[75]:


from __future__ import unicode_literals
import re
import sys
import math
#import punkt_data_german
import codecs
from collections import defaultdict


# In[76]:


#{ Log Likelihoods

    #////////////////////////////////////////////////////////////



    # helper for _reclassify_abbrev_types:


def _dunning_log_likelihood(count_a, count_b, count_ab, N):

        """

        A function that calculates the modified Dunning log-likelihood

        ratio scores for abbreviation candidates.  The details of how

        this works is available in the paper.

        """

        p1 = float(count_b) / N

        p2 = 0.99



        null_hypo = (float(count_ab) * math.log(p1) +

                     (count_a - count_ab) * math.log(1.0 - p1))

        alt_hypo  = (float(count_ab) * math.log(p2) +

                     (count_a - count_ab) * math.log(1.0 - p2))



        likelihood = null_hypo - alt_hypo



        return (-2.0 * likelihood)

    


# In[77]:


def _col_log_likelihood(count_a, count_b, count_ab, N):

        """

        A function that will just compute log-likelihood estimate, in

        the original paper it's described in algorithm 6 and 7.



        This *should* be the original Dunning log-likelihood values,

        unlike the previous log_l function where it used modified

        Dunning log-likelihood values

        """

        import math



        p = 1.0 * count_b / N

        p1 = 1.0 * count_ab / count_a

        p2 = 1.0 * (count_b - count_ab) / (N - count_a)



        summand1 = (count_ab * math.log(p) +

                    (count_a - count_ab) * math.log(1.0 - p))



        summand2 = ((count_b - count_ab) * math.log(p) +

                    (N - count_a - count_b + count_ab) * math.log(1.0 - p))



        if count_a == count_ab:

            summand3 = 0

        else:

            summand3 = (count_ab * math.log(p1) +

                        (count_a - count_ab) * math.log(1.0 - p1))



        if count_b == count_ab:

            summand4 = 0

        else:

            summand4 = ((count_b - count_ab) * math.log(p2) +

                        (N - count_a - count_b + count_ab) * math.log(1.0 - p2))

        likelihood = summand1 + summand2 - summand3 - summand4

        return (-2.0 * likelihood)


# In[78]:


_col_log_likelihood(3,4,2,1100)


# ### Pseudocode

# In[ ]:


# Must run the dunning_func for every combination and sequence of words
# outter loop: raps around the 
#
#   1   2   3      4     n position
#  Ich bin ein Berliner  
#   a ->b               1st Iteration
#       a ->b           2nd Iteration
#           a  ->  b    3rd Iteration

Ratios = []
for j in 1:len(filter_words):
    _col_log_likelihood(filter_words.count(j),filter_words.count(j+1),filter_words.count('ich'+'bin'),len(filter_words))
                                # count_a                count_b               count_ab


# In[87]:


import re
from itertools import islice, izip  # Why can't python import izip???!! I need this to count the number of ngrams a+b
from collections import Counter
words = re.findall("\w+", 
   "the quick person did not realize his speed and the quick person bumped")
Counter(izip(words, islice(words, 1, None))) 


# In[84]:


get_ipython().magic('pinfo Counter')

