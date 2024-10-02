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
st.write(f"$h_1$ (tutti neri): {prob_history[-1, 0]:.3f}")
st.write(f"$h_2$ (metà neri): {prob_history[-1, 1]:.3f}")
st.write(f"$h_3$ (nessuno nero): {prob_history[-1, 2]:.3f}")

hypotheses = np.array([1.0, 0.5, 0.0])
next_raven_black_prob = np.sum(hypotheses * prob_history[-1])
st.write(f'Credenza che il prossimo corvo sarà nero: {next_raven_black_prob:.3f}')
