import os, time

try:
    from pytube import Playlist, YouTube
    from art import * 

except ModuleNotFoundError:
    os.system('pip install pytube')
    os.system('pip install art')


def inicio(func1=print, func2=print, func3=print):
    tprint('YT Download')
    print('Modify: Francisco J. Velez O.')
    print('-----------------------------')

    msg = "Write: \n"
    msg += "\t1. Download Video. \n"
    msg += "\t2. Playlist. \n"
    msg += "\t3. Personalized. \n"
    msg += " >>> "

    opc = input(msg)

    if '1' in opc: func1()
    elif '2' in opc: func2()
    elif '3' in opc: func3()

    else: print(f'Invalid option error ({opc}).')

def get_Url(archivo='plurls.txt'):
    # Create a function to get urls form list of playlist
    def get_playlist(playlists):
        urls = []

        for playlist in playlists:
            playlist_urls = Playlist(playlist)

            for url in playlist_urls:
                urls.append(url)

        return urls 

    # Code drive
    infor = input('\n >>> Write the url: ')

    playlist = infor.split('+')
    pl_ursls = get_playlist(playlist)

    with open(archivo, 'w') as f:
        for url in pl_ursls:
            f.write(f'{url}\n')

    print(f"\n [+] Urls successfully saved into {os.getcwd()}/{archivo}")

def downloadVideo(ruta, cont='', enCarpeta='./videos'):
    video = YouTube(ruta)  
    descarga = video.streams.get_highest_resolution()
    
    if cont: cont = f'{cont}. '
    
    descarga.download(
        enCarpeta, filename=f'{cont}{descarga.default_filename}'
    )

    return descarga.title
    
def download_videos(archivo='./plurls.txt', enCarpeta='./videos', sum_=0):
    with open(archivo, 'r') as f: lines = f.readlines()

    for num, ruta in enumerate(lines):
        try:
            name = downloadVideo(ruta, num+1+sum_, enCarpeta)
            
            print(f'\n >>> {num+1+sum_}. {ruta}; ({name}).')
            time.sleep(0.02)

        except: pass

def opcs(opc=0):
    if opc == 1: print('\n Downloaded video: ' + downloadVideo(input('\n Route: ')))
    
    if opc == 2: 
        get_Url('plurls.txt')
        download_videos('plurls.txt', './videos')

    if opc == 3:
        print("Option to customize the code...")

inicio( 
    lambda: opcs(1),
    lambda: opcs(2),
    lambda: opcs(3)
)

#* Author: Francisco Velez
