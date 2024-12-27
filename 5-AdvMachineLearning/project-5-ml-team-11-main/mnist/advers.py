from mnist import Net
import torch
from PIL import Image               # PIL is an image processing library
from torchvision import transforms
import torch.nn.functional as F

# Load the model and its weights. Set model to evaluate mode
model = Net()                                   # Net() is the model class
model.load_state_dict(torch.load('model.pt'))   # load OUR model
model.eval()                                    # set to eval mode

img = Image.open('5.png')   # we will use '5.png' as our adversarial example
img_tensor = transforms.ToTensor()(img).unsqueeze(0)    # converts our image into a tensor, which is a 2d array of values between 0-1 instead of 0-255

goal = torch.tensor([9], dtype=torch.long)              # set goal to 9

for i in range(250):
    # This lets us compute gradients on the input.
    # Otherwise, only the model's would be computed.
    img_tensor.requires_grad = True
    output = model(img_tensor)
    loss = F.nll_loss(output, goal)

    loss.backward()
    dx = img_tensor.grad    # dx stores changes we could make to make the classification MORE accurate

    # create adversarial example which is the original image MINUS our changes
    adversarial_example = img_tensor - dx*0.001
    adversarial_example = torch.clamp(adversarial_example, 0, 1)    # clamp value to between 0 and 1

    # set our new example to be the new original image. call detach so we can use .backward() again
    img_tensor = adversarial_example.detach()

# write new adversarial image to a file
img_out = transforms.ToPILImage()(img_tensor.squeeze())
img_out.save('adversarial.png' )