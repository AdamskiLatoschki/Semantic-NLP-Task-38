# Compulsory Task 1

""" 1) Write a note about what you found interesting about the similarities between cat, monkey and banana and think of an example of your own.
 
 I was impressed how smartly those 3 words (cat, monkey, banana) have been categorised, clasified by the computer. Cat and monkey have high similarity because they are both animals. Its commonly known that monkey eat bananas and thats why both words have got high similarity but who would think that the computer is able to recognise differences and similarities between them ? I am personally shocked !. Thats really interesting how computer recognise transitive relationships in the calculation. 

Below you can see my own example, where I was a bit dissapointed to be honest. I was expecting better resultsor maybe different results. """
import spacy
nlp = spacy.load('en_core_web_md')

word_one = nlp('Mars')
word_two = nlp('Earth')
word_three = nlp('Animals')

print(word_one.similarity(word_two))
print(word_three.similarity(word_two))
print(word_three.similarity(word_one))



""" 2) Run the example file with the simpler language model 'en_core_web_sm' and write anote what you notice is different from model 'en_core_web_md'

sm/md/lg refer to the sizes of the models (small, medium, large respectively). Generally larger models are expected to be "better" and more accurate overall but sometimes it depends on case and requirements and I have noticed that difference when I run an example file where similarity was higher on 'MD' mode than 'SM'. I noticed also that comparing similarity works slightly better on shorter pieces of text in my opinion, if I am not wrong or is it depending on the text content ?. Hopefully it is an answer you are expecting :)"""
