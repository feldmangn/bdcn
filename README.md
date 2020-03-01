## [Bi-Directional Cascade Network for Perceptual Edge Detection(BDCN)](https://arxiv.org/pdf/1902.10903.pdf)

This repo is an implementation of BCDN that's actually runnable out of the box. If you want to train your own model or go deeper in the code, consider looking into the original repo for more information. For this implementation an Nvidia GPU is needed.

### Installing:
If you don't have Pytorch installed: first go to the Pytorch site and install it. If you have an Nvidia GPU be sure to get the exact version of CUDA which matches the Pytorch version (At the moment of writing CUDA is on 10.2 but Pytorch on CUDA10.1)
Follow the getting started here https://pytorch.org/get-started/locally/

With Pytorch installed:
Download the ZIP or clone this repo. Go to its folder location in command line or your virtual environment and run 
then pip install requirements.txt
This should install all prerequisites except Pytorch and Torchvision because somehow the super intelligent guys over at Facebook can't figure out how Pip works

With the repo ready download the original pretrained models from here https://drive.google.com/file/d/1CmDMypSlLM6EAvOt5yjwUQ7O5w-xCm1n/view
Unzip them and drag the 4 models into the 'models' folder

### Running (evaluation)
Put your images in the 'images' folder and run main.py.
A few parameters for settings such as which of the 4 models to use can be found at the bottom of main.py in the parse_args() method.
If you get an error about memory usage consider downsizing the resolution of the images in your folder, or putting less of them in at the same time.