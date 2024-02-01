import streamlit as st
from PyPDF2 import PdfMerger, PdfReader

st.title("Unir PDF")

# subir los archivos pds con streamlit
lista_pdfs = st.file_uploader("Sube los archivos .PDF que quieras unir :rocket:", accept_multiple_files=True, type=["pdf"])



# objeto para unir los pdfs
merger = PdfMerger()

if st.button("Unir archivos"):
    if len(lista_pdfs) == 0:
        print(len(lista_pdfs))
        st.error("Por favor sube tus archivos en formato .PDF")
    else:
        st.success("Uniendo tus archivos")
        for pdf in lista_pdfs:
            merger.append(pdf)
        merger.write('./pdfs_unidos/trabajofinal-protocolo_investigacion-GualitoVazquezJoseManuel.pdf')
        merger.close()
        st.success("Se ha unido tu archivo")

# se recomienda subir primero la portada y posteriormente subir el archivo siguiente para que no modifique el orden de union
