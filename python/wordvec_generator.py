import json
import os

import gensim
import numpy as np
from keras.layers import Dense, Activation, Dropout
from keras.models import Sequential
from keras.optimizers import RMSprop
from keras.utils import np_utils

np.random.seed(1337)

ROOT_PATH = "C:\\Users\\t-midu\\PycharmProjects\\BERT-BiLSTM-CRF-NER"
model_path = os.path.join(ROOT_PATH, "word2vec_tx")
place_path = os.path.join(ROOT_PATH, "NERdata\\place")

word2vec_model = gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=False)

train_data_list = list()
train_lable_list = list()


with open(place_path, encoding="utf-8") as place_fd:
    place_json = json.loads(place_fd.read())
    for index, type in enumerate(place_json["place"]):
        for word in type["properties"]:
            try:
                train_data_list += [word2vec_model[word]]
                train_lable_list += [index]
            except KeyError:
                pass

# 数据预处理
X_train = np.array(train_data_list)
y_train = np_utils.to_categorical(train_lable_list, num_classes=9)


# 模型构建
model = Sequential([
    Dense(32, input_dim=200),
    Activation('relu'),
    Dropout(0.1),

    Dense(16, input_dim=32),
    Activation('relu'),

    Dense(9, input_dim=32),
    Activation('softmax'),
])

# 激活RMS优化器
rmsprop = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)

model.compile(optimizer=rmsprop,
              loss='categorical_crossentropy',
              metrics=['accuracy'])

print('Training ------------')
model.fit(X_train, y_train, epochs=20, batch_size=8)


def get_result(result):
    max_index = np.argmax(result)
    category_list = ["forest", "mountain", "river", "ocean", "garden", "suburb", "city", "college", "flatland"]
    return category_list[max_index]


result = get_result(model.predict(np.array([word2vec_model["老师"]])))

print(result)

