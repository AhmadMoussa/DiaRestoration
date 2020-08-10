import numpy as np
import cv2
import os

class DataLoader():
    def __init__(self, data_path, batch_size = 4):
        self.data_path = data_path
        self.batch_size = batch_size
        self.data, self.labels = self.pre_load_data()
        print(self.data.shape)

    def pre_load_data(self):
        imgs = []
        labels = []
        for file in os.listdir(self.data_path):
            imgs.append(cv2.imread(os.path.join(self.data_path, file)))

            label = file[:-4].split(" ")
            label = label[:-1]
            for i, num in enumerate(label):
                label[i] = int(num)

            labels.append(label)
        return np.array(imgs), np.array(labels)

    def __len__(self):
        '''
        :return:    number of total batches, depends on batch size and index
        '''
        return int(np.floor(len(self.data) / float(self.batch_size)))

    def shuffle_in_unison_scary(self, a, b):
        rng_state = np.random.get_state()
        np.random.shuffle(a)
        np.random.set_state(rng_state)
        np.random.shuffle(b)

    def load_batch(self):
        self.shuffle_in_unison_scary(self.data, self.labels)
        for i in range(self.__len__()):
            batch = self.data[i * self.batch_size:(i + 1) * self.batch_size]
            target = self.labels[i * self.batch_size:(i + 1) * self.batch_size]

            for j in range(self.batch_size):
                # shift image a little as data augmentation
                rows, cols, c = batch[j].shape
                sav = np.random.randint(-65, 65)
                sah = np.random.randint(-65, 65)
                M = np.float32([[1, 0, sav], [0, 1, sah]])
                img = cv2.warpAffine(batch[j] , M, (cols, rows))
                batch[j,] = img / 255

                # also need to shift
                flat_list = np.array([target[j]])

                flat_list[0][0] = flat_list[0][0] + sav
                flat_list[0][2] = flat_list[0][2] + sav
                flat_list[0][4] = flat_list[0][4] + sav
                flat_list[0][6] = flat_list[0][6] + sav

                flat_list[0][1] = flat_list[0][1] + sah
                flat_list[0][3] = flat_list[0][3] + sah
                flat_list[0][5] = flat_list[0][5] + sah
                flat_list[0][7] = flat_list[0][7] + sah

                flat_list = flat_list[0]
                target[j,] = np.array(flat_list)

            yield batch, target



if __name__ == "__main__":
    loader = DataLoader("annotated_aug", batch_size = 4)

    for i, (imgs, labels) in enumerate(loader.load_batch()):
        print(imgs.shape, labels.shape)

        print(labels[0])
        cv2.imshow("image", imgs[0])
        cv2.waitKey()



