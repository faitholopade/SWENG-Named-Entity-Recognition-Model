# Dell Customer Support NER Project

This repository contains the completed project for the Dell Customer Support Named Entity Recognition (NER) initiative. NER is a critical component in Natural Language Processing (NLP), essential for tasks like Query Understanding, Information Extraction, and Question Answering. Leveraging deep learning techniques, our project builds upon existing open-source NER models to create a specialized NER model designed for Dell's customer support text data.

Key objectives of this NER model include:

1) Detection of Personal Identifiable Information (PII) such as names, addresses, phone numbers, and email addresses.
2) Recognition of various unique identifiers (order ids, invoice numbers, service ids, etc.).
3) Identification of temporal expressions (dates, times, relative dates/times).
4) Classification of technical and non-technical issues mentioned in customer support logs.
5) Suggestion of possible solutions for both technical and non-technical issues.
6) Identification of organizations, brands, and hardware/products/models mentioned.
7) Recognition of hardware or model specifications.
8) Identification of software names.
9) Detection of currency values and abbreviations/acronyms.

It's important to note that many leading open-source models (like Spacy, Flair) already support many of these entities. Additionally, Python libraries for extracting specific entities (e.g., phone numbers, currencies) are available and have been utilized in this project. The primary aim was to create a labeled dataset using these resources to train a Dell-specific NER model tailored for analyzing customer support interactions.
