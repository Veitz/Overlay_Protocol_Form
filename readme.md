# Anleitung: Überlagern von Scans mit Firmenpapier (PDF)

Dieses Python-Programm ermöglicht es, ein Firmenpapier (PDF) als Hintergrund auf jede Seite eines gescannten Dokuments (ebenfalls im PDF-Format) anzuwenden. Dabei bleibt die Seitenanzahl und Reihenfolge des gescannten Dokuments unverändert.

## Voraussetzungen

1. **Python-Installation**: Stelle sicher, dass Python 3.x auf deinem System installiert ist.
2. **Abhängigkeiten**: Installiere die benötigte Bibliothek `PyPDF2` mit folgendem Befehl:
   ```bash
   pip install PyPDF2
   ```
3. **Dateien vorbereiten**:
   - Ein PDF mit deinem Firmenpapier (z. B. `firmenpapier.pdf`).
   - Ein Ordner mit eingescannten PDF-Dokumenten (z. B. im Ordner `scans`).

## Programmfunktionen

### 1. Einzelne Datei überlagern

Die Funktion `overlay_document_on_letterhead` überlagert jede Seite eines gescannten Dokuments mit der ersten Seite des Firmenpapiers.

#### Parameter:
- `scan_path`: Pfad zum gescannten PDF-Dokument.
- `letterhead_path`: Pfad zum Firmenpapier (PDF).
- `output_path`: Pfad, unter dem das kombinierte PDF gespeichert wird.

### 2. Batch-Verarbeitung mehrerer Dateien

Die Funktion `batch_process_scans` verarbeitet alle PDF-Dokumente in einem angegebenen Ordner und überlagert sie mit dem Firmenpapier.

#### Parameter:
- `scan_folder`: Ordner, der die eingescannten PDF-Dokumente enthält.
- `letterhead_path`: Pfad zum Firmenpapier (PDF).
- `output_folder`: Ordner, in dem die kombinierten PDF-Dokumente gespeichert werden.

## Nutzung

1. **Firmenpapier und Scans bereitstellen**:
   - Speichere dein Firmenpapier als `firmenpapier.pdf` im selben Verzeichnis wie das Skript oder passe den Pfad an.
   - Lege alle eingescannten PDF-Dateien in den Ordner `scans`.

2. **Das Programm ausführen**:
   Führe das Skript in der Konsole oder einer Python-Umgebung aus. Beispiel:
   ```bash
   python scriptname.py
   ```

3. **Ergebnisse prüfen**:
   - Die kombinierten PDF-Dokumente werden im Ordner `output` gespeichert.
   - Jedes kombinierte Dokument hat denselben Dateinamen wie das Original, mit dem Präfix `combined_`.

## Beispielablauf

- `firmenpapier.pdf`: Dein Firmenpapier mit Logo.
- `scans/Dokument1.pdf`: Ein gescanntes Dokument.
- `output/combined_Dokument1.pdf`: Die Ausgabe mit Firmenpapier als Hintergrund.

## Hinweise

- Das Programm verwendet immer die erste Seite des Firmenpapiers als Hintergrund.
- Die Dimensionen des Firmenpapiers werden auf jede Seite des gescannten Dokuments angewendet.

## Fehlerbehebung

- **Fehler: `ModuleNotFoundError: No module named 'PyPDF2'`**:
  - Installiere die Bibliothek mit `pip install PyPDF2`.
- **Firmenpapier wird nicht richtig angewendet**:
  - Überprüfe, ob das Firmenpapier tatsächlich die gewünschte erste Seite enthält.
- **Output-Ordner nicht gefunden**:
  - Das Skript erstellt den Ordner `output` automatisch. Stelle sicher, dass du Schreibrechte hast.



