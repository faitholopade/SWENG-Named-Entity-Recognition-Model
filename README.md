# SwEng-Group-1-NER

Named Entity Recognition (NER) involves automatically identifying and classifying named entities in text such as persons,
places, and organizations. NER is import for Natural Language Processing (NLP) tasks such as Query Understanding (QU),
Information Extraction (IE) and Question Answering (QA). Recent NER development efforts focus on deep learning
approaches. There are large number of open-source NER models available online that provides out-of-the-box capabilities for
entity detection.
Building on open-source NER models, this project aims to train a foundational NER model tuned to Dell data to recognize
important entities within customer support textual logs. The NER model should cater multiple use-cases:

1) identification of Personal Identifiable Information (PII) such as person names [name], addresses/locations [location],
phone numbers [phone], emails[email]
2) various identifiers (such as order ids, invoice numbers, service ids etc.) [id]
3) temporal information including relative dates/times (e.g. yesterday, a month from now) [relative_date], date/times (e.g.
January, 11:45pm, 23-12-2021) [date_time]
4) technical issues mentioned (e.g. Bluetooth not working) [tech_issue]
5) non-technical issues mentioned (e.g. warranty update, dispatch delay) [non_tech_issue]
5) possible resolutions for tech issues (e.g. reinstall windows) [tech_resolution]
6) possible resolutions for non-tech issues (e.g. arrange alternative delivery) [non_tech_resolution]
6) organizations or brands (e.g. microsoft, nvidia, dell) [org]
7) hardware/product/consumer model (e.g. ac adapter, gpu, laptop, ram, speaker, xps 13, latitude 3350, xbox) [hardware]
8) hardware or model specification (e.g. 13", intel i7, 15gb, 3w) [spec]
9) software mentioned (e.g. windows, ms win, antivirus, adobe) [software]
10) currencies ($1000, INR 12344) [currency]
11) Abbreviation/Acronym (e.g. CX, MOBO, HDD, BSOD) [short_form]

It is worthy to note that many state of the art open-source models such as Spacy, Flair etc. support most of the above
entities. Moreover, open-source Python libraries exist for extracting some entities present in text such as phone numbers
(https://pypi.org/project/phonenumbers/) and currencies (https://pypi.org/project/price-parser/ ).
This project aims to leverage such open-source implementation for building a labelled dataset for training a Dell NER model.
