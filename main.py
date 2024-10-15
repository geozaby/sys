import streamlit as st
import subprocess
import os

# Titre de l'application
st.title("Écrire, Compiler et Exécuter du Code C avec Streamlit")

# Champ de texte pour écrire du code C
code_c = st.text_area("Écris ton code C ici", value="""
#include <stdio.h>

int main() {
    printf("Hello, World!\\n");
    return 0;
}
""", height=200)

# Bouton pour compiler et exécuter le code
if st.button("Compiler et Exécuter"):
    # Sauvegarder le code dans un fichier temporaire
    with open("temp_code.c", "w") as f:
        f.write(code_c)
    
    # Compilation du fichier C
    compile_command = ["gcc", "temp_code.c", "-o", "temp_executable"]
    compilation_result = subprocess.run(compile_command, capture_output=True, text=True)

    # Vérification si la compilation a réussi
    if compilation_result.returncode == 0:
        st.success("Compilation réussie")

        # Exécution du fichier compilé
        execution_result = subprocess.run(["./temp_executable"], capture_output=True, text=True)
        
        # Affichage de la sortie du programme C
        st.subheader("Sortie du programme :")
        st.text(execution_result.stdout)
    else:
        # Affichage des erreurs de compilation
        st.error("Erreur de compilation")
        st.text(compilation_result.stderr)
