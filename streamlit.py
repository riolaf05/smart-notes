import streamlit as st
import requests
import sys
# from dotenv import load_dotenv
import os
# load_dotenv(override=True)

st.title("Smart Notes")

OCR_WEBHOOK_PROD="http://localhost:5678/webhook/d0101d2d-9b12-4684-bc31-257f860f8eec"
NOTION_WEBHOOK_PROD="http://localhost:5678/webhook/3dbd12d0-0805-4fce-b924-868e2ccb5ff4"
OCR_API_KEY=os.getenv("API_KEY", "your_api_key_here")

uploaded_file = st.file_uploader("Carica una foto", type=["jpg", "jpeg", "png"])

ocr_text = ""
if uploaded_file is not None:
    if st.button("Invia per OCR"):
        try:
            uploaded_file.seek(0)
            files = {"file": (uploaded_file.name, uploaded_file.read(), uploaded_file.type)}
            headers = {
                "X-Api-Key": OCR_API_KEY
            }
            ocr_url = OCR_WEBHOOK_PROD
            response = requests.post(ocr_url, files=files, headers=headers)
            print(response.json(), file=sys.stderr)
            if response.ok:
                output = response.json()[0]['output']
                ocr_text = output.get("summary", "")
                title = output.get("title", "")
            else:
                st.error(f"Errore nell'OCR: {response.text}")
        except Exception as e:
            st.error(f"Errore di richiesta REST: {e}")

if ocr_text or st.session_state.get("ocr_text"):
    if ocr_text:
        st.session_state["ocr_text"] = ocr_text
        st.session_state["title"] = title
    text = st.text_area("Testo estratto (modificabile)", st.session_state.get("ocr_text", ""), height=200)
    title = st.text_input("Titolo", value=st.session_state.get("title", ""))
    st.session_state["ocr_text"] = text

    if st.button("Invia a Notion"):
        webhook_url = NOTION_WEBHOOK_PROD
        try:
            resp = requests.post(webhook_url, json={"summary": text, "title": title})
            if resp.status_code == 200:
                st.success("Testo inviato con successo!")
            else:
                st.error("Errore nell'invio del testo: " + resp.status_code + " " + resp.text)
        except Exception as e:
            st.error(f"Errore di richiesta REST: {e}")