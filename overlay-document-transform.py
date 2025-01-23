# pip3 install PyPDF2

from PyPDF2 import PdfReader, PdfWriter, PageObject
import os

def overlay_document_on_letterhead(scan_path, letterhead_path, output_path):
    """
    Überlagert jede Seite eines gescannten Dokuments auf das Firmenpapier (PDF) und behält die Seitenanzahl des Scans bei.

    :param scan_path: Pfad zum gescannten Dokument (PDF).
    :param letterhead_path: Pfad zum Firmenpapier (PDF).
    :param output_path: Pfad, wo das kombinierte PDF gespeichert werden soll.
    """
    # Öffne das Firmenpapier und das gescannte Dokument
    letterhead_reader = PdfReader(letterhead_path)
    scan_reader = PdfReader(scan_path)
    writer = PdfWriter()

    # Verwendet die erste Seite des Firmenpapiers als Hintergrund
    letterhead_page = letterhead_reader.pages[0]

    # Überlagere jede Seite im Scan
    for scan_page in scan_reader.pages:
        # Erstelle eine neue Seite basierend auf den Abmessungen des Firmenpapiers
        combined_page = PageObject.create_blank_page(width=letterhead_page.mediabox.width, height=letterhead_page.mediabox.height)

        # Füge das Firmenpapier hinzu
        combined_page.merge_page(letterhead_page)

        # Füge die Scan-Seite hinzu
        combined_page.merge_page(scan_page)

        # Füge die kombinierte Seite zum Writer hinzu
        writer.add_page(combined_page)

    # Speichere das kombinierte PDF
    with open(output_path, "wb") as output_file:
        writer.write(output_file)

    print(f"Das kombinierte PDF wurde unter {output_path} gespeichert.")

def batch_process_scans(scan_folder, letterhead_path, output_folder):
    """
    Verarbeitet alle Scans in einem Ordner und legt sie auf das Firmenpapier.

    :param scan_folder: Ordner, der die Scans enthält.
    :param letterhead_path: Pfad zum Firmenpapier (PDF).
    :param output_folder: Ordner, in dem die kombinierten Dokumente gespeichert werden sollen.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Liste alle Dateien im Scan-Ordner
    for scan_file in os.listdir(scan_folder):
        scan_path = os.path.join(scan_folder, scan_file)

        # Überprüfe, ob die Datei ein PDF ist
        if scan_file.lower().endswith(".pdf"):
            output_path = os.path.join(output_folder, f"combined_{scan_file}")
            overlay_document_on_letterhead(scan_path, letterhead_path, output_path)

if __name__ == "__main__":
    # Aufruf
    letterhead_path = "background.pdf"  # Firmenpapier (PDF)
    scan_folder = "scans"  # Ordner mit eingescannten Dokumenten (PDFs)
    output_folder = "output"  # Ordner für die Ergebnisse

    print("Ordnerstruktur: \n"
          "scans = Ordner der die Scans enthält. \n"
          "background.pdf = Hintergrund_PDF muss diesen Namen tragen. \n"
          "output = Ordner, in dem die kombinierten Dokumente gespeichert werden, wird automatisch angelegt. \n"
          )
    str(input("Drücke Enter zum fortfahren..."))
    print("")
    try:
        batch_process_scans(scan_folder, letterhead_path, output_folder)
    except Exception as e:
        print("fehler: ", e)
    print("")
    str(input("Drücke Enter zum beenden..."))
