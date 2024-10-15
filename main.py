import streamlit as st
import subprocess
import os

# Titre de l'application
st.title("Exécution de code C avec Streamlit")

# Téléchargement du fichier C
uploaded_file = st.file_uploader("Télécharger votre fichier C (code.c)", type=["c"])

if uploaded_file is not None:
    # Sauvegarde du fichier téléchargé
    with open("code.c", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("Fichier téléchargé et enregistré avec succès")

    # Compilation du fichier C
    compile_command = ["gcc", "code.c", "-o", "code_executable"]
    compilation_result = subprocess.run(compile_command, capture_output=True, text=True)

    # Vérification si la compilation a réussi
    if compilation_result.returncode == 0:
        st.success("Compilation réussie")

        # Exécution du fichier compilé
        execution_result = subprocess.run(["./code_executable"], capture_output=True, text=True)
        
        # Affichage de la sortie du programme C
        st.subheader("Sortie du programme :")
        st.text(execution_result.stdout)
    else:
        # Affichage des erreurs de compilation
        st.error("Erreur de compilation")
        st.text(compilation_result.stderr)

