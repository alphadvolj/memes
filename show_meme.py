from PIL import Image
import matplotlib.pyplot as plt



if name == '__main__':
    image_path = 'memes/mem.jpg'

    img = Image.open(image_path)

    plt.imshow(img)
    plt.axis('off')
    plt.show()