[EN]

# YouTube Downloader

This Python script allows you to download YouTube videos either as audio (MP3) or video (MP4). It uses `yt-dlp`, a powerful tool for extracting and downloading content from YouTube and other websites. You can choose the download type by selecting either only the audio in MP3 format or the full video in MP4 format.

## Features
- **Audio Download (MP3):** Extracts and saves only the audio stream of the YouTube video.
- **Video Download (MP4):** Downloads the full YouTube video in MP4 format.
- **Cookie Support:** The script allows you to use a cookie file to access age-restricted content (optional).

## Installation

1. Make sure Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. Install the required libraries using `pip`:

    ```bash
    pip install yt-dlp
    ```

3. (Optional) If you want to use cookies for accessing age-restricted videos, export the cookies from your browser and save them in a file named `cookies.txt`.

## Usage

1. Download the `youtube_downloader.py` file and save it to your computer.
2. Open the command prompt or terminal and navigate to the directory where the file is saved.
3. Run the script:

    ```bash
    python youtube_downloader.py
    ```

4. Enter the YouTube URL of the desired video.
5. Choose the download type:
    - **1:** Audio Only (MP3)
    - **2:** Video (MP4)

The script will then download the video or audio file to the `downloads` directory.

## Example

```bash
Enter the YouTube URL: https://www.youtube.com/watch?v=MzGXZWktRbI
Choose the download type:
1. Audio Only (MP3)
2. Video (MP4)
Your choice (1 or 2): 1
Starting download from: https://www.youtube.com/watch?v=MzGXZWktRbI
Download completed. File saved to: downloads


[DE]

# YouTube Downloader

Dieses Python-Skript ermöglicht es dir, YouTube-Videos entweder als Audio (MP3) oder Video (MP4) herunterzuladen. Es verwendet `yt-dlp`, ein leistungsstarkes Tool zur Extraktion und zum Download von Inhalten von YouTube und anderen Websites. Du kannst den Download-Typ auswählen, indem du entweder nur das Audio im MP3-Format oder das komplette Video im MP4-Format herunterlädst.

## Funktionen
- **Audio-Download (MP3):** Extrahiert und speichert nur den Audio-Stream des YouTube-Videos.
- **Video-Download (MP4):** Lädt das komplette YouTube-Video im MP4-Format herunter.
- **Cookies-Unterstützung:** Das Skript ermöglicht es dir, eine Cookies-Datei zu verwenden, um auf altersbeschränkte Inhalte zuzugreifen (optional).

## Installation

1. Stelle sicher, dass Python auf deinem System installiert ist. Du kannst es von der [offiziellen Python-Website](https://www.python.org/downloads/) herunterladen.

2. Installiere die erforderlichen Bibliotheken mit `pip`:

    ```bash
    pip install yt-dlp
    ```

3. (Optional) Wenn du Cookies für den Zugriff auf altersbeschränkte Videos verwenden möchtest, exportiere die Cookies aus deinem Browser und speichere sie in einer Datei namens `cookies.txt`.

## Verwendung

1. Lade die `youtube_downloader.py`-Datei herunter und speichere sie auf deinem Computer.
2. Öffne die Eingabeaufforderung oder das Terminal und navigiere zum Verzeichnis, in dem die Datei gespeichert ist.
3. Führe das Skript aus:

    ```bash
    python youtube_downloader.py
    ```

4. Gib die YouTube-URL des gewünschten Videos ein.
5. Wähle den Download-Typ:
    - **1:** Nur Audio (MP3)
    - **2:** Video (MP4)

Das Skript lädt dann das Video oder die Audio-Datei in das `downloads`-Verzeichnis herunter.

## Beispiel

```bash
Gib die YouTube-URL ein: https://www.youtube.com/watch?v=MzGXZWktRbI
Wähle den Download-Typ:
1. Nur Audio (MP3)
2. Video (MP4)
Deine Auswahl (1 oder 2): 1
Starte Download von: https://www.youtube.com/watch?v=MzGXZWktRbI
Download abgeschlossen. Datei gespeichert in: downloads
