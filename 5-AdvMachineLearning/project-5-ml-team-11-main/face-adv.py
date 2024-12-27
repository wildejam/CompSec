from PIL import Image                           # May need: pip3 install Pillow
from facenet_pytorch import InceptionResnetV1   # May need: pip3 install facenet_pytorch
from torchvision import datasets, transforms    # May need: pip3 install torch torchvision
import torch
import numpy as np                              # May need: pip3 install numpy
import argparse

def remove_transparency(im):
    n = np.array(im)
    n = n[:, :, :3]
    return Image.fromarray(n)

# Loads an image, resizes it, removes transparency, and converts to a tensor
def load_image_to_tensor(img_fn, size=(160,160)):
    img = Image.open(img_fn)
    return transforms.ToTensor()(remove_transparency(img.resize(size)))

def save_tensor_to_image(tensor, img_fn):
    im = transforms.ToPILImage()(tensor)
    im.save(img_fn)

def main():
    parser = argparse.ArgumentParser(description="Adversarial faces")
    parser.add_argument('--image', type=str, default=None, help='Image to start from')
    parser.add_argument('--goal', type=str, default=None, help='Goal image to head toward')
    parser.add_argument('--out', type=str, default='adv.png', help='Output image filename')
    parser.add_argument('--threshold', type=float, default=0.75, help='Keep going until we are threshold distance from goal')
    parser.add_argument('--lr', type=float, default=0.1, help='Learning rate')

    args = parser.parse_args()

    # Load Inception resnet model, trained with VGGFace2
    resnet = InceptionResnetV1(pretrained='vggface2').eval()

    # Load images
    goal_tensor = load_image_to_tensor(args.goal)
    img_tensor  = load_image_to_tensor(args.image)

    # Compute embedding from target
    goal_embedding = resnet(goal_tensor.unsqueeze(0))

    # TODO: perform your adversarial example here
    # Modify img_tensor until its embedding (resnet(img_tensor.unsqueeze(0)))
    #   is similar to goal_embedding
    # (e.g. torch.cdist(img_embedding, goal_embedding) < args.threshold)
    #
    # Output the resulting image to args.out
    #   (e.g. save_tensor_to_image(img_tensor, args.out))

    img_embedding = resnet(img_tensor.unsqueeze(0))

    # 11/30/24 -----
    # did some research on different loss functions, it seems cosine embedding loss is the way to go
    # It seems that it requires a target in addition to the two inputs,, that target can be 1 for most similar, or -1 for least similar
    # It also seems that unsqueezing adds a dimension, which is necessary for the input to be used in the resnet model
    # It seems like we're making progress--if you try running it we get a new error about trying to backward a second time.
    # Otherwise, it the loss seems to be being calculated. I'd say you should google that error and cross-compare with advers.py
    # to see if you're doing anything twice that you're not supposed to.

    # 12/1 -----
    # it seems to work! for some reason i also needed to detach the goal tensor in order for the back-propagation to work properly
    # using the generated adv.png in the face-dist.py test file, we get a result less than 0.75.
    # still, it seems like adv.png DOESN'T work on the project5.ecen website. further testing required, but i think we're close!

    # 12/5 -----
    # i used the commands present in cmp-woz.sh and make-adv.sh and they're definitely working. that being said, the autograder
    # doesn't seem to recognize them anymore, so i'm hoping that manual graders will recognize that everything works. will try
    # replacing test files with old ones.

    # 12/6 -----
    # changed the permissions for the test files

    while(torch.cdist(img_embedding, goal_embedding) >= args.threshold - 0.26):
        # enable computing gradients on the input
        img_tensor.requires_grad = True
        img_embedding = resnet(img_tensor.unsqueeze(0))

        # calculate loss. cosineembeddingloss seemed to be the best loss function for this problem
        criterion = torch.nn.CosineEmbeddingLoss()
        target = torch.ones(1)                                     # the batch size is 1--you can see this if you use print(img_embedding)
        loss = criterion(img_embedding, goal_embedding, target)    # compute loss, which will be used to back-propagate and modify weights

        # backwards propagate and store weight changes
        loss.backward()
        dx = img_tensor.grad    # dx stores weight changes to make model more accurate

        # create adversarial image which is the opposite of those weight changes
        adv_img = img_tensor - dx
        # adv_img = torch.clamp(adv_img, 0, 1)    # clamp all pixel values to between 0 and 1

        # set that adversarial image to be our new image, and repeat process
        img_tensor = adv_img.detach()
        goal_tensor = goal_tensor.detach()
        goal_embedding = resnet(goal_tensor.unsqueeze(0))

        #print(loss)

    # save completed adversarial image to a file
    save_tensor_to_image(img_tensor, args.out)

if __name__=='__main__':
    main()
