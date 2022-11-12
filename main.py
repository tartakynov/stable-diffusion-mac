import torch
from diffusers import StableDiffusionPipeline


def main():
    pipe = StableDiffusionPipeline.from_pretrained("./stable-diffusion-v1-5")
    # pipe = pipe.to("cuda")

    prompt = "a photo of an astronaut riding a horse on mars"
    image = pipe(prompt).images[0]
    image.save("astronaut_rides_horse.png")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
