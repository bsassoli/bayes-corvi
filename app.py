import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.title('Bayes e corvi')
st.write("Questo è un'applicazione interattiva per simulare il teorema di Bayes con un esempio pratico realizzata per il corso di Introduzione al Ragionamento Scientifico, A.A. 2024/2025, Università di Milano.")

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


num_observations = st.slider('Numero di corvi neri osservati:', min_value=0, max_value=20, value=4, step=1)

fig, prob_history, c_e_history = plot_probabilities(num_observations)
st.pyplot(fig)

st.write(f"Probabilità dopo {num_observations} osservazioni:")
st.write(f"$h_1$ (tutti neri): {prob_history[-1, 0]:.6f}")
st.write(f"$h_2$ (metà neri): {prob_history[-1, 1]:.6f}")
st.write(f"$h_3$ (nessuno nero): {prob_history[-1, 2]:.6f}")

hypotheses = np.array([1.0, 0.5, 0.0])
next_raven_black_prob = np.sum(hypotheses * prob_history[-1])
st.write(f'Credenza che il prossimo corvo sarà nero: {next_raven_black_prob:.6f}')
'''
st.markdown("### 0. Il punto di partenza e le tre ipotesi iniziali. \nRicordiamo la formulazione del [**teorema di Bayes**](https://it.wikipedia.org/wiki/Teorema_di_Bayes) e vediamone a un caso pratico (ispirato da Michael Strevens, [Notes on Bayesian Confirmation Theory](https://www.strevens.org/bct/BCT.pdf) (2017)):')st.markdown('### 0. Il punto di partenza e le tre ipotesi iniziali. \nRicordiamo la formulazione del [**teorema di Bayes**](https://it.wikipedia.org/wiki/Teorema_di_Bayes) e vediamone a un caso pratico (ispirato da Michael Strevens, [Notes on Bayesian Confirmation Theory](https://www.strevens.org/bct/BCT.pdf) (2017)):")
st.latex("\\begin{align}P(h \mid e) = \dfrac{P(e \mid h)P(h)}{P(e)}\end{align}")
st.markdown('Ora immaginiamo di avere tre ipotesi in competizione tra loro, e di non avere ancora alcuno tipo di riscontro empirico:\n* $h_1$ = tutti i corvi sono neri\n* $h_2$ = metà dei corvi è nera\n* $h_3$ = nessun corvo è nero\n\nDato che non ho ancora raccolto alcuna evidenza, assegno alle tre ipotesi la stessa probabilità a priori:$P(h_1)=P(h_2)=P(h_3) =\dfrac{1}{3}$')
st.markdown('### 1. 🐦‍⬛ Osservo un corvo nero')
st.markdown('Al tempo $t_1$ osservo un corvo nero. Come cambiano le mie credenze nelle tre ipotesi? Cioè, applicando il teorema di Bayes, quale sarà la probabilità $P(h|e)$ dato $e=\ ho \ osservato\ un\ corvo \ nero$ per ognuna di $h_1, h_2, h_3$?')
st.markdown('Iniziamo osservando che:')
st.markdown('* $P(e\mid h_1) = 1.0$ -  la probabilità di osservare un corvo nero dato che so che tutti i corvi sono neri')
st.markdown('* $P(e\mid h_2) = 0.5$ -  la probabilità di osservare un corvo nero dato che so che che metà dei corvi sono neri')
st.markdown('* $P(e \mid h_3) = 0.0$ -  la probabilità di osservare un corvo nero dato che so che che nessun corvo è nero')

st.markdown('A questo punto per applicare il teorema di Bayes mi manca solo il denominatore, cioè $P(e)$, la probabilità di osservare un corvo nero. Per calcolare $P(e)$ posso applicare il [teorema della probabilità totale](https://it.wikipedia.org/wiki/Teorema_della_probabilit%C3%A0_totale):')
st.markdown('\\begin{align}P(e) &= P(e \mid h_1)P(h_1) + P(e \mid h_2)P(h_2) + P(e \mid h_3)P(h_3)\\&= 1 \times \frac{1}{3} + \frac{1}{2} \times \frac{1}{3} + 0 \times \frac{1}{3}\\&= \frac{1}{2}\end{align}')
st.markdown('Di conseguenza, dopo aver osservato un corvo avrò:')
st.markdown('* $P(h_1\mid e) = \dfrac{1 \times \dfrac{1}{3}}{\dfrac{1}{2}}=\dfrac{2}{3}$\n* $P(h_2\mid e) = \dfrac{\dfrac{1}{2} \times \dfrac{1}{3}}{\dfrac{1}{2}}=\dfrac{1}{3}$\n\n')
st.markdown("La probabilità della prima ipotesi $h_1$, che tutti i corvi siano neri, è raddoppiata, passando da 1/3 a 2/3; quella dell'ipotesi che metà dei corvi siano neri, $h_2$, è rimasta immutata; mentre la probabilità dell'ipotesi $h_3$, che nessun corvo sia nero è ora  pari a 0 (come intuitivamente ci aspettiamo che sia), e possiamo di conseguenza scartare tale ipotesi.")
'''