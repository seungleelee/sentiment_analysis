# sentiment_analysis

What we are doing
=================
Under guidance from Prof. Jo Guldi from Southern Methodist University, Katherine and I are collaborating on a program of exploring sentiment in 19th century Hansard texts. For more info, check out our blog https://parliasent.wordpress.com/. This repo is mainly for applying queries to Hansard and adjusting them with guidance from Katherine. 

Current Progress
================
Right now we have a parser that has parsed the complete Hansard, stored as a tsv file, into separate text files according to its date. Currently the directory is sorted by decade, and we believe examining the change in sentiment by decade would be most efficient. 

We currently have two text files that have a list of positive and negative words each. We are giving positive words a score of +1 and negative words a score of -1. With this preliminary data I have currently implemented a very simple tracker that determines if a text is leaning toward positive or negative sentiments. 

Upcoming Tasks
==============
Our current data have several flaws, including a lexicon of sentimental terms that doesn't pick up all the sentimental terms and that misclassifies forms of address such as "honorable" and ironic words such as "pretty." We are currently working on improving our lexicon.

To help improve our lexicon, I am planning to examine words adjacent to the current "negative" and "positive" words in the Hansard. 

Final Goal
==========   
Ultimately, we would like to able to tell: the most emotional speech of every decade; the least emotional speech of every decade; the relative proportion of emotionality that we guess to be positive or negative in each year; whether certain topics or speeches are more emotional than others; whether there are speakers whose speeches regularly change the emotional tenor of a debate (for example they make a negative room more calm).  
