import streamlit as st
from streamlit.components.v1 import html

# Titre de l'application
st.title("Détection de changement de taille de fenêtre ou de focus")

# Instructions pour l'utilisateur
st.write("Cette application détecte si vous modifiez la taille de la fenêtre ou si vous changez d'onglet ou d'application.")

# JavaScript pour détecter les événements de redimensionnement et de perte de focus
js_code = """
<script>
    function sendEvent(eventType) {
        // Envoi de l'événement à Streamlit via un appel au script Python
        const iframe = document.getElementById('streamlit');
        iframe.contentWindow.postMessage({event: eventType}, '*');
    }

    // Détecter les changements de taille de la fenêtre
    window.addEventListener('resize', () => {
        sendEvent('resize');
    });

    // Détecter lorsque l'utilisateur change d'onglet ou passe à une autre application
    document.addEventListener('visibilitychange', () => {
        if (document.hidden) {
            sendEvent('hidden');
        } else {
            sendEvent('visible');
        }
    });
</script>
"""

# Fonctionnalité pour recevoir les événements depuis JavaScript
html(js_code)

# Afficher les événements reçus
event = st.empty()

# Python reçoit l'événement envoyé par JavaScript
st.session_state.event_log = []


def js_event_listener():
    js_event = st.experimental_get_query_params()
    if "event" in js_event:
        event_type = js_event["event"][0]
        st.session_state.event_log.append(event_type)
        event.write(f"Événement détecté : {event_type}")
