# ID-GAN PyTorch Implementation

Reference paper: https://arxiv.org/abs/2001.04296

Auther's implementation: https://github.com/1Konny/idgan.git
___
## Training
 - Data Set: CelebA data set is used for model training
 - Stage 1: VAE is trained for 1e6 iteration
 - Stage 2: Resnet Generator & Discriminator are trained for 3e5 iteration
 - trained on 1xA100 (40 GB SXM4) for 28hrs
___
## Project Files and Folders
- `/d_chkpt` - Folder where 'Discriminator' model check points to be saved
	- `getModelPkl.py`: used to download final check point for the trained model. Command: `python getModelPkl.py`
- `/g_chkpt` - Folder where 'Generator' model check points to be saved
	- `getModelPkl.py`: used to download final check point for the trained model. Command: `python getModelPkl.py`
- `/vae_chkpt` - Folder where 'VAE' model check points to be saved
	- `getModelPkl.py`: used to download final check point for the trained model. Command: `python getModelPkl.py`
- `/outputs` - Folder where the generated images are saved
- `/ID-GAN.ipynb` - Jupyter notebook for the paper implementation.
- `/requirements.txt` - Needed python libraries
