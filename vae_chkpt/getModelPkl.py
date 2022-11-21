import gdown

# https://drive.google.com/file/d/18iLNnncz5G8UYUFWB4yAkn3dBBn4cNnu/view?usp=share_link

url = 'https://drive.google.com/uc?id=18iLNnncz5G8UYUFWB4yAkn3dBBn4cNnu'
chkpts = 'VAE_Final.pt'
gdown.download(url, chkpts, quiet=False)