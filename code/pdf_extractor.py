import PyPDF2

file = "KursbuchNiedersachsen"
pages = [[118,119], [299,300]]

# Öffne das PDF-Dokument, das du extrahieren möchtest
with open(f"code/pdfs/{file}.pdf", 'rb') as file:
    # Erstelle ein PyPDF2-PDF-Dokument-Objekt
    pdf = PyPDF2.PdfReader(file)

    # Erstelle ein leeres PDF-Dokument, das du für das extrahierte Dokument verwenden wirst
    output_pdf = PyPDF2.PdfWriter()

    for interval in pages:
    # Definiere die Seiten, die du extrahieren möchtest (hier extrahieren wir Seite 0 und Seite 1)
        pages_to_extract = range(interval[0]-1, interval[1])

        # Iteriere über die Seiten und füge sie dem neuen PDF-Dokument hinzu
        for page in pages_to_extract:
            output_pdf.add_page(pdf.pages[page])

    # Öffne eine Datei zum Schreiben des extrahierten PDF-Dokuments
    with open('output.pdf', 'wb') as output_file:
        # Schreibe das neue PDF-Dokument
        output_pdf.write(output_file)