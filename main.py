import os
import subprocess


def download_youtube(video_url, output_path="downloads", cookies_file="cookies.txt", download_type="audio"):
    try:
        # Erstelle den Zielordner, falls er nicht existiert
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        print(f"Starte Download von: {video_url}")

        # Wähle den Befehl basierend auf dem Download-Typ
        if download_type == "audio":
            command = [
                "yt-dlp",
                "--extract-audio",              # Extrahiere nur Audio
                "--audio-format", "mp3",        # Konvertiere zu MP3
                "--cookies", cookies_file,      # Verwende die Cookies-Datei
                "--output", f"{output_path}/%(title)s.%(ext)s",  # Dateiname (%(title)s wird durch den Videotitel ersetzt)
                video_url                       # Die YouTube-URL
            ]
        elif download_type == "video":
            command = [
                "yt-dlp",
                "--format", "mp4",              # Wähle das MP4-Format
                "--cookies", cookies_file,      # Verwende die Cookies-Datei
                "--output", f"{output_path}/%(title)s.%(ext)s",  # Dateiname
                video_url                       # Die YouTube-URL
            ]
        else:
            print("Ungültige Auswahl für den Download-Typ.")
            return

        # Führe den Befehl aus
        subprocess.run(command, check=True)

        print(f"Download abgeschlossen. Datei gespeichert in: {output_path}")

    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Download: {e}")
    except Exception as e:
        print(f"Allgemeiner Fehler: {e}")


if __name__ == "__main__":
    # Benutzer nach einer YouTube-URL fragen
    url = input("Gib die YouTube-URL ein: ")
    print("Wähle den Download-Typ:")
    print("1. Nur Audio (MP3)")
    print("2. Video (MP4)")
    choice = input("Deine Auswahl (1 oder 2): ").strip()

    if choice == "1":
        download_youtube(url, download_type="audio")
    elif choice == "2":
        download_youtube(url, download_type="video")
    else:
        print("Ungültige Auswahl. Das Programm wird beendet.")
