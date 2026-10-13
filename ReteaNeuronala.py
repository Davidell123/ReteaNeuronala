import streamlit as st 
import math

st.title("Retea Neuronala")
st.sidebar.title("Setari Retea")



# Stratul de intrare
st.sidebar.header("1. Stratul de intrare")

numar_neuroni_intrare = st.sidebar.number_input("Numar de neuroni in stratul de intrare", min_value=1, step=1, value=2)


st.header("1. Valori de intrare")

valori_intrare = []
for i in range(numar_neuroni_intrare):
    val = st.number_input(f"Valoarea de intrare pentru neuronul {i+1}", key=f"val_in_{i}")
    valori_intrare.append(val)
    st.divider()




#Straturile ascunse
st.sidebar.header("2. Straturi ascunse")

numar_straturi_ascunse = st.sidebar.number_input("Numar de straturi ascunse", min_value=1, max_value=3, step=1)

neuroni_strat_anterior = numar_neuroni_intrare


st.header("2. Straturi ascunse (Conexiuni)")

for i in range(numar_straturi_ascunse):
    st.sidebar.subheader(f"Setari Strat ascuns {i+1}")
    
    neuroni_curenti = st.sidebar.number_input(f"Numar de neuroni in stratul ascuns {i+1}", min_value=1, step=1, value=2, key=f"neuroni_ascunsi_{i}")
   
    operatie_gin = st.sidebar.selectbox(f"Selecteaza operatia GIN pentru stratul ascuns {i+1}:", ["Suma", "Prod", "Min", "Max"], key=f"operatie_gin_{i}")
   
    functie_activare = st.sidebar.selectbox("Functie de activare:", ["Liniara", "Sigmoidala", "Semn", "Tanh", "Treapta"], key=f"functie_activare_{i}")
   
    prag = st.sidebar.number_input("Prag:", value=0.0, step=0.1, key=f"prag_{i}")
   
    tip_iesire = st.sidebar.selectbox("Tip iesire:", ["Binar", "Real"], key=f"tip_iesire_{i}")
   
    st.subheader(f"Stratul ascuns {i+1}")
   
    iesire_strat_nou = []

    for j in range(neuroni_curenti):
        st.write(f"Conexiunile pentru neuronul {j+1}")
        termeni = []
        tarii_sinaptice_neuron = []
        
        for k in range(neuroni_strat_anterior):
            val = st.number_input(f"Taria sinaptica de la neuronul {k+1} (stratul anterior):", key=f"taria_{i}_{j}_{k}")
            tarii_sinaptice_neuron.append(val)

            termen_curent = valori_intrare[k] * val
            termeni.append(termen_curent)
            
        st.divider()

        if operatie_gin == "Suma":
            GIN = sum(termeni)
        elif operatie_gin == "Prod":
            GIN = math.prod(termeni)
        elif operatie_gin == "Min":
            GIN = min(termeni)
        elif operatie_gin == "Max":
            GIN = max(termeni)
            
        st.write(f"Rezultatul GIN pentru neuronul {j+1} este: {GIN}")
        
        if functie_activare == "Treapta":
            if GIN >= prag:
                iesire = 1
            else:
                iesire = 0
        elif functie_activare == "Semn":
            if GIN >= prag:
                iesire = 1
            else:
                iesire = -1
        elif functie_activare == "Liniara":
            iesire = GIN
        elif functie_activare == "Sigmoidala":
            iesire = 1 / (1 + math.exp(-GIN))
        elif functie_activare == "Tanh":
            iesire = math.tanh(GIN)

        if tip_iesire == "Binar":
            if iesire >= 0.5:
                    iesire = 1
            else:
                    iesire = 0
            
        st.write(f"Rezultatul functiei de activare pentru neuronul {j+1} este: {iesire}")

        rezultat_neuron = iesire
        iesire_strat_nou.append(rezultat_neuron)

    neuroni_strat_anterior = neuroni_curenti  
    valori_intrare = iesire_strat_nou  






#Stratul de iesire
st.sidebar.header("3. Stratul de iesire")


numar_neuroni_iesire = st.sidebar.number_input("Numar de neuroni in stratul de iesire", min_value=1, step=1, value=1)  


gin_iesire = st.sidebar.selectbox("Selecteaza operatia GIN pentru stratul de iesire:", ["Suma", "Prod", "Min", "Max"])

functie_activare_iesire = st.sidebar.selectbox("Selecteaza functia de activare pentru stratul de iesire:", ["Liniara", "Sigmoidala", "Semn", "Tanh", "Treapta"])

prag_iesire = st.sidebar.number_input("Prag pentru stratul de iesire:", value=0.0, step=0.1)

tip_iesire_final = st.sidebar.selectbox("Tip iesire final:", ["Binar", "Real"], key="tip_iesire_final")



st.header("3. Stratul de iesire (Conexiuni)")

for i in range(numar_neuroni_iesire):
    st.write(f"Conexiunile pentru neuronul de iesire {i+1}")
    tarii_sinaptice_neuron_iesire = []
    termeni_iesire = []

    for j in range(neuroni_strat_anterior):
        val = st.number_input(f"Taria sinaptica de la neuronul {j+1} (stratul anterior):", key=f"taria_iesire_{i}_{j}")
        termen_curent = valori_intrare[j] * val
        termeni_iesire.append(termen_curent)
        tarii_sinaptice_neuron_iesire.append(val)
        
    st.divider()

    if gin_iesire == "Suma":
        GIN_iesire = sum(termeni_iesire)
    elif gin_iesire == "Prod":
        GIN_iesire = math.prod(termeni_iesire)
    elif gin_iesire == "Min":
        GIN_iesire = min(termeni_iesire)
    elif gin_iesire == "Max":
        GIN_iesire = max(termeni_iesire) 
        
    st.write(f"Valoarea GIN calculata: {GIN_iesire}")

    if functie_activare_iesire == "Treapta":
        if GIN_iesire >= prag_iesire:
            iesire_finala = 1
        else:
            iesire_finala = 0  
    elif functie_activare_iesire == "Semn":
        if GIN_iesire >= prag_iesire:
            iesire_finala = 1
        else:
            iesire_finala = -1
    elif functie_activare_iesire == "Liniara":
        iesire_finala = GIN_iesire
    elif functie_activare_iesire == "Sigmoidala":
        iesire_finala = 1 / (1 + math.exp(-GIN_iesire))
    elif functie_activare_iesire == "Tanh":
        iesire_finala = math.tanh(GIN_iesire)

    if tip_iesire_final == "Binar":
        if iesire_finala >= 0.5:
            iesire_finala = 1
        else:
            iesire_finala = 0



    st.write(f"Rezultatul GIN pentru neuronul de iesire {i+1} este: {GIN_iesire}")
    st.write(f"Rezultatul functiei de activare pentru neuronul de iesire {i+1} este: {iesire_finala}")