import os
import shutil


# ruta de los archivos de música por crear sus directorios
MUSIC_DIR = ''


def create_dirs_for_tacks(ruta_directorio):
    files_in_dir = os.listdir(ruta_directorio)
    mp3_files = [f for f in files_in_dir if f.endswith('.mp3')]

    # get artists names
    artists_names = set()
    for mp3_file in mp3_files:
        name_without_extension = os.path.splitext(mp3_file)[0]
        artist_name = name_without_extension.split(" - ")[0]
        artists_names.add(artist_name)
    
    # create new dirs for artists
    for new_dir_name in artists_names:
        new_dir = os.path.join(ruta_directorio, new_dir_name)
        os.makedirs(new_dir, exist_ok=True)
    
    # move files to artist dir
    for mp3_file in mp3_files:
        for artist_name in artists_names:
            if mp3_file.startswith(artist_name):
                original_path = os.path.join(ruta_directorio, mp3_file)
                new_path = os.path.join(ruta_directorio, artist_name)
                shutil.move(original_path, new_path)
                break
    
    return list(artists_names)


dir_names = create_dirs_for_tacks(MUSIC_DIR)
for name in dir_names:
    print(name)
