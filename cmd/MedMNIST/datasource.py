import torch.utils.data as data
import torchvision.transforms as transforms

import medmnist
from medmnist import INFO
import random

download = True

BATCH_SIZE = 128


class DataSource(object):
    def __init__(self):
        raise NotImplementedError()
    def partitioned_by_rows(self, num_workers, test_reserve=.3):
        info = INFO[self.data_flag]
        DataClass = getattr(medmnist, info['python_class'])

        # preprocessing
        data_transform = transforms.Compose([
                         transforms.ToTensor(),
                         transforms.Normalize(mean=[.5], std=[.5])
	])

        # load the data
        train_dataset = DataClass(split='train', transform=data_transform, download=download)
        
        num_train = len(train_dataset)
        selected_train_indices = random.sample(range(num_train), int(num_train//num_workers))
        selected_train_dataset = data.Subset(train_dataset, selected_train_indices)

        # num_test = len(self.test_dataset)
        # selected_test_indices = random.sample(range(num_test), int(num_test//num_workers))
        # selected_test_dataset = data.Subset(self.test_dataset, selected_test_indices)

        self.train_loader = data.DataLoader(dataset=selected_train_dataset, batch_size=BATCH_SIZE, shuffle=True)
        self.valid_loader = data.DataLoader(dataset=selected_train_dataset, batch_size=2*BATCH_SIZE, shuffle=False)
        print("IID-Data:")
        print("Train:", len(selected_train_dataset))
        print("===================")

    def sample_single_non_iid(self, weight=None):
        raise NotImplementedError()

# You may want to have IID or non-IID setting based on number of your peers 
# by default, this code brings all dataset
class MedMNIST(DataSource):

    def __init__(self):
        self.data_flag = 'pathmnist' 
        info = INFO[self.data_flag]
        self.n_channels = info['n_channels']
        self.n_classes = len(info['label'])
        self.task = info['task']

        DataClass = getattr(medmnist, info['python_class'])

        # preprocessing
        data_transform = transforms.Compose([
                         transforms.ToTensor(),
                         transforms.Normalize(mean=[.5], std=[.5])
	])

        # load the data
        train_dataset = DataClass(split='train', transform=data_transform, download=download)
        test_dataset = DataClass(split='test', transform=data_transform, download=download)

        self.pil_dataset = DataClass(split='train', download=download)

        # encapsulate data into dataloader form
        self.train_loader = data.DataLoader(dataset=train_dataset, batch_size=BATCH_SIZE, shuffle=True)
        self.valid_loader = data.DataLoader(dataset=train_dataset, batch_size=2*BATCH_SIZE, shuffle=False)
        self.test_loader = data.DataLoader(dataset=test_dataset, batch_size=2*BATCH_SIZE, shuffle=False)

        print(train_dataset)
        print("===================")
        print(test_dataset)

if __name__ == "__main__":
    m = MedMNIST()
    print("===================")
    for inputs, targets in m.train_loader:
        print(inputs)
        print(targets)
        print(m.task)
        break
    print("===================")
    m.partitioned_by_rows(1000)
    print("===================")
    for inputs, targets in m.train_loader:
        print(inputs)
        print(targets)
        print(m.task)
        break
    print("===================")


# import torch.utils.data as data
# import torchvision.transforms as transforms
# import medmnist
# from medmnist import INFO

# download = True
# BATCH_SIZE = 128

# class DataSource(object):
#     def __init__(self):
#         raise NotImplementedError()
#     def partitioned_by_rows(self, num_workers, test_reserve=.3):
#         raise NotImplementedError()
#     def sample_single_non_iid(self, weight=None):
#         raise NotImplementedError()

# class MedMNIST(DataSource):

#     def __init__(self, train_fraction=0.01, test_fraction=0.01):
#         self.data_flag = 'pathmnist'
#         info = INFO[self.data_flag]
#         self.n_channels = info['n_channels']
#         self.n_classes = len(info['label'])
#         self.task = info['task']

#         DataClass = getattr(medmnist, info['python_class'])

#         # preprocessing
#         data_transform = transforms.Compose([
#                          transforms.ToTensor(),
#                          transforms.Normalize(mean=[.5], std=[.5])
# 	])

#         # load the data
#         full_train_dataset = DataClass(split='train', transform=data_transform, download=download)
#         full_test_dataset = DataClass(split='test', transform=data_transform, download=download)

#         # Calculate the number of samples to use based on the fractions
#         train_samples = int(len(full_train_dataset) * train_fraction)
#         test_samples = int(len(full_test_dataset) * test_fraction)

#         # Subset the datasets
#         train_dataset = data.Subset(full_train_dataset, range(train_samples))
#         test_dataset = data.Subset(full_test_dataset, range(test_samples))

#         self.pil_dataset = DataClass(split='train', download=download)

#         # Print dataset information
#         print("Train Dataset:")
#         print("Number of datapoints in full_train_dataset:", len(full_train_dataset))
#         print("Number of datapoints in train_dataset:", len(train_dataset))
#         print("Number of classes:", self.n_classes)
#         print("===================")

#         print("Test Dataset:")
#         print("Number of datapoints in full_test_dataset:", len(full_test_dataset))
#         print("Number of datapoints in test_dataset:", len(test_dataset))
#         print("Number of classes:", self.n_classes)
#         print("===================")

#         # encapsulate data into dataloader form
#         self.train_loader = data.DataLoader(dataset=train_dataset, batch_size=BATCH_SIZE, shuffle=True)
#         self.valid_loader = data.DataLoader(dataset=train_dataset, batch_size=2*BATCH_SIZE, shuffle=False)
#         self.test_loader = data.DataLoader(dataset=test_dataset, batch_size=2*BATCH_SIZE, shuffle=False)

# if __name__ == "__main__":
#     m = MedMNIST(train_fraction=0.01, test_fraction=0.01)  # Example: Use 80% of the data for training and 20% for testing
