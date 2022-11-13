# Run Stable Diffusion locally on a Macbook Pro

This repo is me documenting my attempt to run Stable Diffusion AI model locally on my Macbook Pro laptop with Intel chip

## Prerequisites

- Python 3
- Dependencies from the requirements.txt
- [git lfs](https://git-lfs.github.com)

## Get stable-diffusion-v1-5 model
```
git lfs install
git clone https://huggingface.co/runwayml/stable-diffusion-v1-5
```

## Run the script
```
./main.py
```

It took 23m 38s to render the image, which is extremely slow 🥴

## What's next?

I was able to get this down to ~8m (33 iterations, ~14s/it) with https://github.com/bes-dev/stable_diffusion.openvino. This is not ideal, but it is still almost 3x faster than the original model. Ideally, I should probably invest in a Thunderbolt eGPU or cloud computing.
