import gdown

# https://drive.google.com/file/d/1qV2AHPIC-ud1yPE28q4DP1TIDaPBQCnR/view?usp=share_link

url = 'https://drive.google.com/uc?id=1qV2AHPIC-ud1yPE28q4DP1TIDaPBQCnR'
chkpts = 'G_Final.pt'
gdown.download(url, chkpts, quiet=False)