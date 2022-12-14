Medium article is about classifying youtube comments into 5 classes based on sentiment analysis and sentence types.
https://medium.com/@ananya.joshi_70890/classification-of-youtube-comments-based-on-sentiments-and-sentence-types-80cc05514052

Presentation link on slideshare:
https://www.slideshare.net/AnanyaJoshi38/shortstorypptpptx-254903672


The article talks about classifying youtube comments into 5 classes - Imperative, Interrogative, Positive, Negative, Miscellaneous, Corrective.

The experiment is done on 10,000 random comments collected from tutorial videos from youtube using youtube API.
comments are cleaned by removing stop words, urls, punctuations, numbers retaining some stop words like how, what, why etc. 
Tf-idf and document frequency techniques are used to vectorize the words.

Performances are measured by using cross-validation score and F1-score. % models were trained using different ML algorithms, Linear SVC, 
Logistic regression, Multinomial NB, Random Forest classifier and Decision tree classifier.






