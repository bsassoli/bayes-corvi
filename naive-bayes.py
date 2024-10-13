# Training set: email con le loro parole e classificazione spam/non-spam
emails = [
    {'testo': ['offerta', 'gratis', 'vinci'], 'spam': True},
    {'testo': ['buongiorno', 'appuntamento', 'domani'], 'spam': False},
    {'testo': ['offerta', 'esclusiva', 'subito'], 'spam': True},
    {'testo': ['ciao', 'come', 'stai'], 'spam': False},
    {'testo': ['vincere', 'grande', 'premio'], 'spam': True},
    {'testo': ['appuntamento', 'lavoro', 'oggi'], 'spam': False},
]

# Conta quante volte appare una parola nelle email spam e non spam
def conta_parole(emails):
    parole_spam = list(set([word for email in filter(lambda email: email["spam"], emails) for word in email["testo"]]))
    parole_non_spam = list(set([word for email in filter(lambda email: not email["spam"], emails) for word in email["testo"]]))
    spam_totale = [email['spam'] for email in emails].count(True)
    non_spam_totale = len(emails) - spam_totale

    return parole_spam, parole_non_spam, spam_totale, non_spam_totale


# Calcola la probabilità che una nuova email sia spam
def calcola_probabilita(email_test, parole_spam, parole_non_spam, spam_totale, non_spam_totale):
    probabilita_spam = spam_totale / (spam_totale + non_spam_totale)
    probabilita_non_spam = non_spam_totale / (spam_totale + non_spam_totale)

    for parola in email_test:
        if parola in parole_spam:
            probabilita_spam *= (parole_spam[parola] / spam_totale)
        else:
            probabilita_spam *= 1 / (spam_totale + 1)  # L'approssimiamo con Laplace smoothing

        if parola in parole_non_spam:
            probabilita_non_spam *= (parole_non_spam[parola] / non_spam_totale)
        else:
            probabilita_non_spam *= 1 / (non_spam_totale + 1)  # L'approssimiamo con Laplace smoothing

    return probabilita_spam, probabilita_non_spam

# Funzione per classificare una nuova email
def classifica_email(email_test):
    parole_spam, parole_non_spam, spam_totale, non_spam_totale = conta_parole(emails)
    prob_spam, prob_non_spam = calcola_probabilita(email_test, parole_spam, parole_non_spam, spam_totale, non_spam_totale)

    if prob_spam > prob_non_spam:
        return "Spam"
    else:
        return "Non Spam"

# Proviamo a classificare una nuova email
nuova_email = ['offerta', 'esclusiva', 'gratis']
risultato = classifica_email(nuova_email)

print(f"La nuova email è classificata come: {risultato}")
