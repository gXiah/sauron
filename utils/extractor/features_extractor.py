import requests
import numpy as np
from base64 import encodebytes
from io import BytesIO
from PIL import Image

from keras import backend as K
from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from keras.models import Model
from keras.layers import Input

from utils.IO_ops._txt_engine._txt_reader import get_lines


paths_list = []

m = MobileNetV2(weights="imagenet", include_top=True,input_tensor=Input(shape=(224 , 224, 3)))
m.layers.pop()
model = Model(m.input, m.layers[-1].output)

def process_image(image_url):
    response = requests.get(image_url)
    image_bytes = BytesIO(response.content)
    img = Image.open(image_bytes)
    img = img.resize((224, 224))
    image_data = np.asarray(img)
    image_data = np.expand_dims(image_data, axis=0)
    preprocess = preprocess_input(image_data)
    #preprocess = preprocess/255.
    return preprocess

def get_embedding(model, image_array):
    emb = model.predict(image_array)[0]
    return emb

def init(urls_file_path, save_path):

    paths_list = get_lines(urls_file_path)

    print("======================")
    print("Initializing extractor")
    
    embeddings = []
    for file in paths_list:
        image_processed = process_image(file)
        emb = get_embedding(model, image_processed)
        embeddings.append(emb)
    
    
    embeddings = np.asarray(embeddings)
    np.savez_compressed(save_path, embeddings = embeddings, file_names = paths_list)
    