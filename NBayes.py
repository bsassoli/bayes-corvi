from collections import Counter

emails = [
    {'testo': ['offerta', 'gratis', 'vinci'], 'spam': True},
    {'testo': ['buongiorno', 'appuntamento', 'domani'], 'spam': False},
    {'testo': ['offerta', 'esclusiva', 'subito'], 'spam': True},
    {'testo': ['ciao', 'come', 'stai'], 'spam': False},
    {'testo': ['vincere', 'grande', 'premio'], 'spam': True},
    {'testo': ['appuntamento', 'lavoro', 'oggi'], 'spam': False},
]

num_spam = len([email for email in emails if email['spam']])
num_non_spam = len(emails) - num_spam
parole_spam = Counter([word for email in filter(lambda email: email["spam"], emails) for word in email["testo"]])
parole_non_spam = Counter([word for email in filter(lambda email: not email["spam"], emails) for word in email["testo"]])

prob_spam = num_spam / (num_spam + num_non_spam)
