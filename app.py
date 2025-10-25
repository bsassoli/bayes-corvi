import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Set page config for a wider layout
st.set_page_config(layout="wide")

st.title('Bayes e 🐦‍⬛ corvi')
st.divider()
# Create two columns
left_column, right_column = st.columns([5, 4], gap="large")


with left_column:
    st.markdown("""
    Ricordiamo la formulazione del [**teorema di Bayes**](https://it.wikipedia.org/wiki/Teorema_di_Bayes) e vediamone a un caso pratico (ispirato da Michael Strevens, [Notes on Bayesian Confirmation Theory](https://www.strevens.org/bct/BCT.pdf)(2017))
    """)


    st.latex('''
    \\begin{align}
    P(h\mid e) = \dfrac{P(e \mid h)P(h)}{P(e)}
    \end{align}
            ''')


    st.markdown('''
                Ora immaginiamo di avere tre ipotesi in competizione tra loro, e di non avere ancora alcuno tipo di riscontro empirico:

    * $h_1$ = tutti i corvi sono neri

    * $h_2$ = metà dei corvi è nera

    * $h_3$ = nessun corvo è nero

    Dato che non ho ancora raccolto alcuna evidenza, assegno alle tre ipotesi la stessa probabilità a priori:
    $P(h_1)=P(h_2)=P(h_3) = \dfrac{1}{3}$''')

    st.markdown('''
                ## 🐦‍⬛ 1. Osservo un corvo nero''')

    st.markdown('''
                Al tempo $t_1$ osservo un corvo nero. Come cambiano le mie credenze nelle tre ipotesi? Cioè, applicando il teorema di Bayes, quale sarà la probabilità $P(h|e)$ dato $e=\ ho \ osservato\ un\ corvo \ nero$ per ognuna di $h_1, h_2, h_3$?

    Iniziamo osservando che:
    * $P(e\mid h_1) = 1.0$ -  la probabilità di osservare un corvo nero dato che so che tutti i corvi sono neri
    * $P(e\mid h_2) = 0.5$ -  la probabilità di osservare un corvo nero dato che so che che metà dei corvi sono neri
    * $P(e \mid h_3) = 0.0$ -  la probabilità di osservare un corvo nero dato che so che che nessun corvo è nero


    A questo punto per applicare il teorema di Bayes mi manca solo il denominatore, cioè $P(e)$, la probabilità di osservare un corvo nero. Per calcolare $P(e)$ posso applicare il [teorema della probabilità totale](https://it.wikipedia.org/wiki/Teorema_della_probabilit%C3%A0_totale):''')
    st.latex(r'''
    \begin{align*}
    P(e) &= P(e | h_1)P(h_1) + P(e | h_2)P(h_2) + P(e | h_3)P(h_3)\\
    &= 1 \times \frac{1}{3} + \frac{1}{2} \times \frac{1}{3} + 0 \times \frac{1}{3}\\
    &= \frac{1}{2}
    \end{align*}
    ''')

    st.markdown(r'''
    Di conseguenza, dopo aver osservato un corvo avrò:
    * $P(h_1\mid e) = \dfrac{1 \times \dfrac{1}{3}}{\dfrac{1}{2}}=\dfrac{2}{3}$
    * $P(h_2\mid e) = \dfrac{\dfrac{1}{2} \times \dfrac{1}{3}}{\dfrac{1}{2}}=\dfrac{1}{3}$
    * $P(h_3\mid e) = \dfrac{0\times \dfrac{1}{3}}{\dfrac{1}{2}}=0$


    La probabilità della prima ipotesi $h_1$, che tutti i corvi siano neri, è raddoppiata, passando da 1/3 a 2/3; quella dell'ipotesi che metà dei corvi siano neri, $h_2$, è rimasta immutata; mentre la probabilità dell'ipotesi $h_3$, che nessun corvo sia nero è ora  pari a 0 (come intuitivamente ci aspettiamo che sia), e possiamo di conseguenza scartarla.
    ''')

    st.markdown('''
                ### 🐦‍⬛🐦‍⬛ 2. Osservo un secondo corvo nero
    Cosa succede se a questo punto osservo un secondo corvo nero?
    Per prima cosa dovrò calcolare qual è $P(e)$ a questo stadio utilizzando di nuovo il teorema della probabilità totale:''')

    st.latex(r'''
    \begin{align*}
    P(e) &= P(e \mid h_1)P(h_1) + P(e \mid h_2)P(h_2)\\&= 1 \times \frac{2}{3} + \frac{1}{2} \times \frac{1}{3}\\&= \frac{5}{6}
    \end{align*}
    ''')

    st.markdown(r'''
                E, applicando nuovamente il teorema di Bayes, avrò:

    * $P(h_1\mid e) = \dfrac{1 \times \dfrac{2}{3}}{\dfrac{5}{6}}=\dfrac{4}{5}$
    * $P(h_2\mid e) = \dfrac{\dfrac{1}{2} \times \dfrac{1}{3}}{\dfrac{5}{6}}=\dfrac{1}{5}$
    Da notare che la probabilità di  
    h
    1
    questa volta aumenta ma non raddoppia, e la probabilità di $h_2$ invece diminuisce sensibilmente.
                ''')

    st.markdown(r'''
                ### 3. 🐦‍⬛🐦‍⬛🐦‍⬛ Terza (e successive) osservazione di un corvo nero
    Dopo la seconda volta che osservo un corvo nero la probabilità 
    che il prossimo corvo sarà nero è salita a:''')

    st.latex(r'''
            \begin{align*}
    P(e)&= 1\times\frac{4}{5} + \frac{1}{2}\times\frac{1}{5}\\&=\frac{9}{10}
    \end{align*}''')

    st.markdown(r'''
            Di conseguenza (saltando questa volta i calcoli espliciti):
            La probabilità della terza ipotesi resta zero, la probabilità della prima continua ad avvicinarsi a 1
            ma in modo sempre meno drammatico e la probabilità della seconda ipotesi si avvicina a sua volta a zero. La tabella successiva riassume come l'evoluzione delle credenze nelle tre ipotesi.''')


st.markdown(r'''
            | 🐦‍⬛ | $P(h_1)$ | $P(h_2)$ | $P(h_3)$ | $P(e)$ |
| --- | --- | --- | --- |---|
|$0$ | $1/3$ | $1/3$ | $1/3$|$1/2$
|$1$| $2/3$ | $1/3$ | $0$ | $5/6$|
|$2$| $4/5$ | $1/5$ | $0$ | $9/10$|
|$3$| $8/9$ | $1/9$ | $0$ | $17/18$|
|$\dots$|$\dots$|$\dots$|$\dots$|$\dots$|''')

st.markdown('''
            ### 4. E quindi?

Il teorema di Bayes, che come abbiamo visto è una sorta di conseguenza banalissima delle leggi fondamentali della probabilità (ricordate che la sua dimostrazione non chiede altro che la definizione di probabilità condizionata), cattura moltissime delle nostre intuizioni sulla relazione tra evidenza empirica ed evoluzione delle credenze nella probabilità di un'ipotesi.

Più specificamente, per esempio:

1.  Se un’ipotesi è logicamente incoerente con l’evidenza, la sua probabilità va a zero.
2.	Una volta che la probabilità di un’ipotesi scende a zero, non può mai risalire. L’ipotesi viene eliminata.
3.	L’ipotesi che assegna la più alta probabilità all’evidenza osservata ($h_1$ nel nostro esempio) riceve il maggior incremento di probabilità dall’osservazione dell’evidenza. Un’ipotesi che assegna probabilità 1 all’evidenza riceverà il massimo incremento possibile nelle circostanze.
4.	Se un’ipotesi è coerente con l’evidenza, la sua probabilità non può mai scendere a zero, anche se può avvicinarsi a zero quanto si desidera (come accadrebbe alla probabilità di $h_{2}$ se venissero osservati solo corvi neri).
5.	A mano a mano che un’ipotesi diventa dominante, nel senso che la sua probabilità si avvicina a uno, il suo incremento di probabilità derivante da ulteriori predizioni di successo diminuisce (anche se c’è sempre un incremento).
            ''')


def update_probabilities(hypotheses, num_observations):
    probabilities = np.ones(3) / 3  # Initial equal probabilities
    probability_history = [probabilities.copy()]
    c_e_history = [0.5]  # Initial C(e)

    for _ in range(num_observations):
        c_e = np.sum(hypotheses * probabilities)
        probabilities = hypotheses * probabilities / c_e
        probability_history.append(probabilities.copy())
        c_e_history.append(c_e)

    return np.array(probability_history), np.array(c_e_history)


def plot_probabilities(num_observations):
    hypotheses = np.array([1.0, 0.5, 0.0])  # h1, h2, h3
    prob_history, c_e_history = update_probabilities(hypotheses, num_observations)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Plot probabilities
    ax1.plot(prob_history[:, 0], label='h1 (tutti neri)', marker='o')
    ax1.plot(prob_history[:, 1], label='h2 (metà neri)', marker='s')
    ax1.plot(prob_history[:, 2], label='h3 (zero neri)', marker='^')
    ax1.set_ylabel('Probabilità')
    ax1.set_title('Evoluzione della probabilità delle ipotesi')
    ax1.legend()
    ax1.grid(False)

    # Plot C(e)
    ax2.plot(c_e_history, label='C(e)', marker='o', color='purple')
    ax2.set_xlabel('Numero di corvi neri osservati')
    ax2.set_ylabel('C(e)')
    ax2.set_title('Evoluzione di C(e)')
    ax2.legend()
    ax2.grid(False)

    plt.tight_layout()
    return fig, prob_history, c_e_history


with right_column:
    st.write("Questo è un'applicazione interattiva per simulare il teorema di Bayes con un esempio pratico realizzata per il corso di Introduzione al Ragionamento Scientifico, A.A. 2025/2026, Università di Milano.")
    st.html('<a href="mailto:bernardino.sassoli@unimi.it">Bernardino Sassoli !</a>')
    num_observations = st.slider('Numero di corvi neri osservati:', min_value=0, max_value=20, value=4, step=1)

    fig, prob_history, c_e_history = plot_probabilities(num_observations)
    st.pyplot(fig)

    st.write(f"Probabilità dopo {num_observations} osservazioni:")
    st.write(f"$h_1$ (tutti neri): {prob_history[-1, 0]:.10f}")
    st.write(f"$h_2$ (metà neri): {prob_history[-1, 1]:.10f}")
    st.write(f"$h_3$ (nessuno nero): {prob_history[-1, 2]:.10f}")

    hypotheses = np.array([1.0, 0.5, 0.0])
    next_raven_black_prob = np.sum(hypotheses * prob_history[-1])
    st.write(f'Credenza che il prossimo corvo sarà nero: {next_raven_black_prob:.10f}')
