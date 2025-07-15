import streamlit as st
import requests
import json

st.title("Assistente AI per appunti")

# Dropdown per selezionare la pagina
pagina = st.selectbox("Seleziona la pagina", ["I Segreti dei Giganti", "Pagina 2", "Pagina 3"])

# Upload multiplo di immagini
uploaded_files = st.file_uploader(
    "Carica immagini JPG o PNG", 
    type=["jpg", "jpeg", "png"], 
    accept_multiple_files=True
)

# Endpoint OCR (modifica con il tuo endpoint reale)
OCR_ENDPOINT = "http://192.168.1.135:5004/ocr"
# N8N_ENDPOINT = "http://192.168.1.135:5678/webhook-test/a26452cf-7193-4f13-883f-58f4ec65dea4" #test
N8N_ENDPOINT = "http://192.168.1.135:5678/webhook/a26452cf-7193-4f13-883f-58f4ec65dea4" #prod

results = []

if st.button("Esegui OCR sui file caricati") and uploaded_files:
    for uploaded_file in uploaded_files:
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        response = requests.post(OCR_ENDPOINT, files=files)

        if response.status_code == 200:
            testo = response.json().get("response", "") 
        else:
            testo = f"Errore OCR: {response.status_code}"
        results.append({
            "nomefile": uploaded_file.name,
            "testo": testo,
            "pagina": pagina
        })
        
    #send results json to n8n
    response = requests.post(N8N_ENDPOINT, json=results)
    if response.status_code == 200:
        st.success("Risultati inviati a n8n con successo!")
    else:
        st.error(f"Errore nell'invio a n8n: {response.status_code}")
    
    st.subheader("Risultato JSON")
    st.code(json.dumps(results, ensure_ascii=False, indent=2), language="json")