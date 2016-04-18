# Personality Detection Using Social Media Data

Team:
  1. Saurabh Mishra (9541758252) - saurabhm@usc.edu
  2. Anurag Shukla (6554545108) - anuragsh@usc.edu
  3. Anirudh Mukund Deshpande (2746365653) - deshpana@usc.edu
  4. Tejesh Shivanna (7690654807) - shivanna@usc.edu

# INTRODUCTION
In this project we are planning to deduce an individual’s personality by analyzing their social media data. Myers-Briggs Type Indicator is a very popular approach to identify psychological preferences of people. This method is based on introspective questionnaire and therefore can’t predict any user’s personality type without user’s direct involvement in the process. 

Many studies have found correlation between individual personality and differences in phrases used. This motivates our proposed statistical approach to learn and automatically predict the personality types of a user by analyzing their social media data. Social media platforms like Twitter has lot of tweets hashtagged with self identified MBTI personality types. Proposed model will train different classifiers on these self tagged tweets and predict the personality of users. We will also evaluate different classifiers and present a comparative analysis. Further we also present a correlation of user’s personality types and gender with the corresponding phrases used. We plan to use Arabic tweets for our study. Arabic is the largest member of the semitic language family  and is being spoken by more than 420 million people. It is morphologically and semantically rich. Arabic has many spoken dialects. They lack standardisation and are mostly written in free-text. In social media posts people tend to use informal writing style and mixture of related dialects which makes tweet based personality detection in Arabic very challenging  

# RELATED WORK

Previous researchers have attempted personality detection based on social media data. Most of these studies were conducted on English text. We plan to use Arabic language due to its challenges described in the project introduction. 
In research paper [1], the authors have studied the associations between personality and language use in a large sample of blog samples.  
In research paper [2], researchers at University of Pennsylvania used method of open-vocabulary analysis, to find language features across millions of Facebook posts that distinguish demographic and psychological attributes.

# METHOD AND IMPLEMENTATION

We will use Twitter search APIs to collect the MBTI tagged tweets. Extracted data will be preprocessed by removing the duplicates, normalising non arabic words, digits, links, tagged user handles etc.
We will train Naive Bayes and SVM classifier on MBTI tagged tweets. Following features have been identified:
  1. N-grams of words,  Compare different n-gram models.
  2. Bag of Words (BOW)
  3. POS tagging. To evaluate if POS tags' usage correlates with the personality traits.
  4. Social media features e.g. gender, age, number of followers, number of following, count of tweets etc.
  5. Stylistic Features (Emoticons etc.) 
  6. To analyze the correlation between phrases with personality types and gender we will use Latent Dirichlet Allocation (LDA).
  
We are planning to evaluate the classifier with 2 approaches, one classifier with 16 outcomes and also the other with four binary classifiers for each personality type (e.g. Introvert/Extrovert etc).

# Useful URLs:
  http://www.cs.cmu.edu/~ark/TweetNLP/     NLP package by CMU to process tweets
  http://www1.cs.columbia.edu/~rambow/software-downloads/MADA_Distribution.html
-Morphological Tagging for Arabic
  http://www.cs.brandeis.edu/~cs114/CS114_docs/SRILM_Tutorial_20080512.pdf - SRILM - n-gram model
  http://www.lrec-conf.org/proceedings/lrec2014/pdf/621_Paper.pdf  AraNLP for arabic text processing



