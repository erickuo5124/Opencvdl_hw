import cv2
import torch
import torchvision
from torchvision import transforms
import matplotlib.pyplot as plt
import torch.utils.data as Data
from torch.autograd import Variable

label_text = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
img_index = 0
model = torchvision.models.vgg16()
test_dataset = torchvision.datasets.CIFAR10(
    root='./CIFAR10',
    train=False,
    download=True
)

def show_img():
    img_path = 'Dataset_OpenCvDl_Hw1/Q5_Image/show_img.png'
    img = cv2.imread(img_path)    
    cv2.imshow('Show Image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_hyperparameter():
    print('hyperparameters:')
    print('batch size: 50')
    print('learning rate: 0.0002')
    print('optimizer: Adam')

def show_shortcut():
    
    feature = torch.nn.Sequential(*list(model.children())[:])
    print(feature)

def show_accuracy():
    img_path = 'Dataset_OpenCvDl_Hw1/Q5_Image/loss_accuracy.png'
    img = cv2.imread(img_path)    
    cv2.imshow('Loss and Accuracy',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def test():
    global img_index
    model.load_state_dict(torch.load('./model', map_location='cpu'))
    trans = transforms.Compose([transforms.ToTensor()])
    img, label = test_dataset[img_index]
    test_x = Variable(trans(img)).unsqueeze(0)
    out = model(test_x)
    pred_y = torch.max(out, 1)[1].data.cpu().numpy().squeeze()
    print(pred_y, label)

    plt.figure()

    plt.subplot(1, 2, 1)
    title_idx = test_dataset[img_index][1]
    plt.title(label_text[title_idx])
    plt.imshow(img)

    plt.subplot(1, 2, 2)
    y = out[0, :10].detach().numpy().squeeze()
    y = (y - y.min()) / (y.max() - y.min())
    x = range(10)
    plt.bar(x, y)
    plt.xticks(x, label_text, rotation='vertical')

    plt.show()

def input_changed(num):
    global img_index
    img_index = int(num)
