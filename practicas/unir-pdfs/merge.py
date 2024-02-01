from PyPDF2 import PdfMerger, PdfReader
import os

# directorio donde estan los pdfs a unir
lista_pdfs = os.listdir('./listapdfs')
# objeto para unir los pdfs
merger = PdfMerger()
# ciclo para recorrer los pdfs dentro del directorio donde estan los
for pdf in lista_pdfs:
    merger.append(PdfReader('./listapdfs/' + pdf))

merger.write('./pdfs_unidos/noticia8-GualitoVazquezJoseManuel.pdf')
merger.close()