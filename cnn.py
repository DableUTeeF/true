from keras import models, layers, optimizers
import numpy as np
import cv2
import os
from sklearn.model_selection import train_test_split

def get_model():
    inpl = layers.Input((360, 640, 3))
    inpr = layers.Input((360, 640, 3))
    inpc = layers.Input((384, 640, 3))
    # xl = layers.Conv2D(32, 3, strides=(2, 2))(inpl)
    # xl = layers.BatchNormalization()(xl)
    # xl = layers.Activation('relu')(xl)
    # xl = layers.Conv2D(32, 3)(xl)
    # xl = layers.BatchNormalization()(xl)
    # xl = layers.Activation('relu')(xl)
    # xl = layers.MaxPooling2D()(xl)
    #
    # xr = layers.Conv2D(32, 3, strides=(2, 2))(inpr)
    # xr = layers.BatchNormalization()(xr)
    # xr = layers.Activation('relu')(xr)
    # xr = layers.Conv2D(32, 3)(xr)
    # xr = layers.BatchNormalization()(xr)
    # xr = layers.Activation('relu')(xr)
    # xr = layers.MaxPooling2D()(xr)

    xc = layers.Conv2D(32, 3, 2)(inpc)
    xc = layers.BatchNormalization()(xc)
    xc = layers.Activation('relu')(xc)
    xc = layers.Conv2D(32, 3)(xc)
    xc = layers.BatchNormalization()(xc)
    xc = layers.Activation('relu')(xc)
    x = layers.MaxPooling2D()(xc)

    # x = layers.concatenate((xl, xc, xr))
    # x = layers.concatenate([xl, xr])

    x = layers.Conv2D(96, 3, strides=(2, 2))(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    x = layers.Conv2D(128, 3)(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    x = layers.Conv2D(128, 3)(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    x = layers.MaxPooling2D()(x)
    x = layers.Conv2D(256, 3)(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    x = layers.Conv2D(256, 3)(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    x = layers.MaxPooling2D()(x)
    x = layers.Conv2D(512, 3)(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    x = layers.Conv2D(512, 3)(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    # x = layers.GlobalAveragePooling2D()(x)
    x = layers.Flatten()(x)
    x = layers.Dense(2, activation='sigmoid')(x)

    # model = models.Model([inpl, inpc, inpr], x)
    # model = models.Model([inpl, inpr], x)
    model = models.Model(inpc, x)
    model.compile(optimizer='adam',
                  loss='mae')
    return model


def out2d():
    inp = layers.Input((352, 640, 3))
    x = layers.Conv2D(32, 3, strides=(2, 2), padding='same')(inp)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    d1 = layers.Conv2D(32, 3, padding='same')(x)
    x = layers.BatchNormalization()(d1)
    x = layers.Activation('relu')(x)
    x = layers.MaxPooling2D()(x)
    x = layers.Conv2D(64, 3, padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    d2 = layers.Conv2D(64, 3, padding='same')(x)
    x = layers.BatchNormalization()(d2)
    x = layers.Activation('relu')(x)
    x = layers.MaxPooling2D()(x)
    x = layers.Conv2D(128, 3, padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    d3 = layers.Conv2D(128, 3, padding='same')(x)
    x = layers.BatchNormalization()(d3)
    x = layers.Activation('relu')(x)
    x = layers.MaxPooling2D()(x)
    x = layers.Conv2D(256, 3, padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    d4 = layers.Conv2D(256, 3, padding='same')(x)
    x = layers.BatchNormalization()(d4)
    x = layers.Activation('relu')(x)
    x = layers.MaxPooling2D()(x)
    x = layers.Conv2D(512, 3, padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    x = layers.Conv2D(512, 3, padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    # x = layers.Conv2DTranspose(256, 3, strides=(2, 2), padding='same')(x)
    # x = layers.BatchNormalization()(x)
    # x = layers.Activation('relu')(x)
    # x = layers.Conv2D(256, 3, padding='same')(x)
    # # x = layers.concatenate([x, d4])
    # x = layers.BatchNormalization()(x)
    # x = layers.Activation('relu')(x)
    # x = layers.Conv2DTranspose(128, 3, strides=(2, 2), padding='same')(x)
    # x = layers.BatchNormalization()(x)
    # x = layers.Activation('relu')(x)
    # x = layers.Conv2D(128, 3, padding='same')(x)
    # # x = layers.concatenate([x, d3])
    # x = layers.BatchNormalization()(x)
    # x = layers.Activation('relu')(x)
    # x = layers.Conv2DTranspose(64, 3, strides=(2, 2), padding='same')(x)
    # x = layers.BatchNormalization()(x)
    # x = layers.Activation('relu')(x)
    # x = layers.Conv2D(64, 3, padding='same')(x)
    # # x = layers.concatenate([x, d2])
    # x = layers.BatchNormalization()(x)
    # x = layers.Activation('relu')(x)
    # x = layers.Conv2DTranspose(32, 3, strides=(2, 2), padding='same')(x)
    # x = layers.BatchNormalization()(x)
    # x = layers.Activation('relu')(x)
    # x = layers.Conv2D(32, 3, padding='same')(x)
    # # x = layers.concatenate([x, d1])
    # x = layers.BatchNormalization()(x)
    # x = layers.Activation('relu')(x)
    # x = layers.Conv2D(32, 3, padding='same')(x)
    # x = layers.BatchNormalization()(x)
    # x = layers.Activation('relu')(x)
    x = layers.Conv2D(1, 3, padding='same', activation='sigmoid')(x)
    model = models.Model(inp, x)
    model.compile(optimizer=optimizers.Adam(),
                  loss='binary_crossentropy',
                  metrics=['acc'])
    return model


def get_data():
    x = []
    y = []
    for file in os.listdir('output/mouse/'):
        if 'jpg' in file:
            continue
        txt = open(os.path.join('output/mouse/', file)).read().split('\n')
        for line in txt:
            if len(line.split(',')) == 2:
                a, b = line.split(',')
                # y.append((int(a) / 1920, int(b) / 1080))
                a = int(a) // 3 // 32
                b = int(b) // 3 // 32
                target = np.zeros((352 // 32, 640 // 32, 1))
                target[b, a] = 1
                # target[max(0, b-31):b+30, max(0, a-31):a+30] += 0.25
                # target[max(0, b-15):b+14, max(0, a-15):a+14] += 0.25
                # target[max(0, b-7):b+6, max(0, a-7):a+6] += 0.25
                # target[max(0, b-3):b+2, max(0, a-3):a+2] += 0.25
                y.append(target)
        im1 = cv2.imread(os.path.join('output/mouse/', file[:-4]+'_1.jpg'))
        im1 = cv2.resize(im1, (640, 384))
        im2 = cv2.imread(os.path.join('output/mouse/', file[:-4]+'_2.jpg'))
        im2 = cv2.resize(im2, (640, 384))
        im3 = cv2.imread(os.path.join('output/mouse/', file[:-4]+'_center.jpg'))
        im3 = cv2.resize(im3, (640, 384))
        # ims = np.concatenate((im1, im2, im3), axis=-1).astype('float32')
        ims = im3.astype('float32')
        ims /= 127.5
        ims -= 1
        ims = ims[:352, :, :]
        x.append(ims)
    return np.array(x, dtype='float32'), np.array(y)


if __name__ == '__main__':
    x, y = get_data()
    X_train, X_test, y_train, y_test = train_test_split(x, y)

    model = out2d()
    model.summary()
    model.fit(x[:-16], y[:-16], epochs=400, batch_size=8,
              # validation_data=[X_test, y_test]
              )

    y_pred = model.predict(x)
    for i in range(y.shape[0]):
        # print(y_pred[i], y[i])
        pred = cv2.resize((y_pred[i] * 255).astype('uint8'), (640, 352))
        true = cv2.resize((y[i] * 255).astype('uint8'), (640, 352))
        cv2.imwrite(f'predict/{i}_pred.jpg', pred)
        cv2.imwrite(f'predict/{i}_test.jpg', true)
