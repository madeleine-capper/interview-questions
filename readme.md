# Data Science Interview Questions Platform

## Contents presently:

### editme.py
 - a command line software appication that allows for review and tagging of logged data science interview questions.

### masterlist.pkl, cleaned_v0.pkl, templist.pkl
 - masterlist.pkl, the first catalogued and structured data version of data science interview questions, slightly less than 400 currently.
 - cleaned_v0, a slightly cleaned version of the above
 - templist.pkl, which contains any updated versions saved from editme.py.  masterlist.pkl should be replaced with templist.pkl presuming changes are valid and should cascade back

 ### interview_me:
    picks 20 questions based on topic tags selected by the user and presents those questions to the user.  contingent on proper tagging, which depends on usage of editme.py.
    - currently selects random questions, in the future will have the full functionality described above, once tags exist.