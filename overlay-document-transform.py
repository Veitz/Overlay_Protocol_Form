# pip install pillow pypdf2

from PIL import Image
import os

def overlay_document_on_letterhead(scan_path, letterhead_path, output_path):
    """
    Überlagert ein gescanntes Dokument auf ein Firmenpapier und speichert das Ergebnis ab.

    :param scan_path: Pfad zum gescannten Dokument (JPEG/PNG/PDF).
    :param letterhead_path: Pfad zum Firmenpapier (JPEG/PNG).
    :param output_path: Pfad, wo das kombinierte Bild gespeichert werden soll.
    """
    # Öffne das Firmenpapier und das gescannte Dokument
    letterhead = Image.open(letterhead_path).convert("RGBA")
    scan = Image.open(scan_path).convert("RGBA")

    # Skaliere das gescannte Dokument auf die Größe des Firmenpapiers
    scan = scan.resize(letterhead.size, Image.ANTIALIAS)

    # Kombiniere beide Bilder
    combined = Image.alpha_composite(letterhead, scan)

    # Speichere das kombinierte Bild als PNG
    combined.save(output_path, format="PNG")
    print(f"Das kombinierte Dokument wurde unter {output_path} gespeichert.")


def batch_process_scans(scan_folder, letterhead_path, output_folder):
    """
    Verarbeitet alle Scans in einem Ordner und legt sie auf das Firmenpapier.

    :param scan_folder: Ordner, der die Scans enthält.
    :param letterhead_path: Pfad zum Firmenpapier (JPEG/PNG).
    :param output_folder: Ordner, in dem die kombinierten Dokumente gespeichert werden sollen.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Liste alle Dateien im Scan-Ordner
    for scan_file in os.listdir(scan_folder):
        scan_path = os.path.join(scan_folder, scan_file)

        # Überprüfe, ob die Datei ein Bild ist
        if scan_file.lower().endswith((".png", ".jpg", ".jpeg")):
            output_path = os.path.join(output_folder, f"combined_{scan_file}")
            overlay_document_on_letterhead(scan_path, letterhead_path, output_path)

if __name__ == "__main__":
    # Beispielaufruf
    letterhead_path = "firmenpapier.png"  # Firmenpapier
    scan_folder = "scans"  # Ordner mit eingescannten Dokumenten
    output_folder = "output"  # Ordner für die Ergebnisse

    batch_process_scans(scan_folder, letterhead_path, output_folder)
