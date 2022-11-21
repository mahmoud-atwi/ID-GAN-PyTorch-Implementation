import gdown

# https://drive.google.com/file/d/1ipqT88zNAO4gSgjCSOszSyWpLNvgT6m1/view?usp=share_link

url = 'https://drive.google.com/uc?id=1ipqT88zNAO4gSgjCSOszSyWpLNvgT6m1'
chkpts = 'D_Final.pt'
gdown.download(url, chkpts, quiet=False)