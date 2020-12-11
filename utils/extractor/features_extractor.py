import requests
import numpy as np
from base64 import encodebytes
from io import BytesIO
from PIL import Image
from PIL import UnidentifiedImageError

from keras import backend as K
from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from keras.models import Model
from keras.layers import Input

from utils.IO_ops._txt_engine._txt_reader import get_lines
from __main__ import Logger, os

paths_list = []

m = MobileNetV2(weights="imagenet", include_top=True,input_tensor=Input(shape=(224 , 224, 3)))
m.layers.pop()
model = Model(m.input, m.layers[-1].output)


IMG_PROCESS_ERROR = -1
IMG_PROCESS_OK = 0
image_process_flag = IMG_PROCESS_OK

def process_image(image_url):
    response = requests.get(image_url)
    image_bytes = BytesIO(response.content)
    preprocess = 0
    
    try:
        img = Image.open(image_bytes)
        img = img.resize((224, 224))
        image_data = np.asarray(img)
        image_data = np.expand_dims(image_data, axis=0)
        preprocess = preprocess_input(image_data)

        image_process_flag = IMG_PROCESS_OK

    except UnidentifiedImageError as e:
        image_process_flag = IMG_PROCESS_ERROR


    finally:
        pass

    
    #preprocess = preprocess/255.
    return preprocess

def get_embedding(model, image_array):

    emb = 0

    try:
        emb = model.predict(image_array)[0]
    except IndexError as e:
        print('Error while getting embeding : {}'.format(e))
    

    return emb

def init(urls_file_path, save_path):

    paths_list = get_lines(urls_file_path)

    Logger.print("Initializing extractor")
    
    embeddings = []
    i = 0
    for file in paths_list:

        print('Saving file #{} - {}'.format(i, file))

        try:
            image_processed = process_image(file)
        except IndexError as e:
            continue

        if image_process_flag == IMG_PROCESS_OK:

            emb = get_embedding(model, image_processed)
            #embeddings.append(emb)


            try:
                os.mkdir(save_path)
            except FileExistsError as e:
                pass
            finally:
                pass

            np_emp = np.asarray(emb)
            np.savez_compressed(save_path + '/' + str(i), embeddings = emb, file_names = file)

        i += 1