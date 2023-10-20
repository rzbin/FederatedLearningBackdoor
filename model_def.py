import torch.nn as nn

# Define a simple neural network
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 128) # Input layer (784 input features, 128 hidden units)
        self.relu = nn.ReLU()              # ReLU activation function
        self.fc2 = nn.Linear(128, 10)      # Output layer (10 classes for digits 0-9)

    def forward(self, x):
        # Flatten the input image
        x = x.view(-1, 28 * 28)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
