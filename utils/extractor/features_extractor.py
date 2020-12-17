import requests
from requests.exceptions import MissingSchema

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

from __main__ import Logger, os, database, SAVE_LOCALLY

from scribe.postgresql.models.product_feature import ProductFeature
from scribe.postgresql.models.product import Product

paths_list = []

m = MobileNetV2(weights="imagenet", include_top=True,input_tensor=Input(shape=(224 , 224, 3)))
m.layers.pop()
model = Model(m.input, m.layers[-1].output)


IMG_PROCESS_ERROR = -1
IMG_PROCESS_OK = 0
image_process_flag = IMG_PROCESS_OK

def process_image(image_url):
    

    preprocess = 0


    try:
        response = requests.get(image_url)
        
        image_bytes = BytesIO(response.content)
        
        
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

    except MissingSchema as e:
        Logger.print('Features extractor : [ERROR] {} is not a valid URL'.format(image_url))
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

def init(paths_list, save_path):

    Logger.print(paths_list)

    Logger.print("Initializing extractor\nDatabase contains {} products".format(len(paths_list)))
    
    # Extracting the data from each image
    embeddings = []
    i = 0
    for file in paths_list:

        # Processing the image ('file')
        # If the processing returns and IndexError exception, we skip the current image
        # IMPORTANT : The IndexError excpetion need to be addressed.
        try:
            image_processed = process_image(file.picture_url)
        except IndexError as e:
            continue


        # If the processing did not raise any error flag
        # (processing of the current image : 'file.picture_url', that is)
        if image_process_flag == IMG_PROCESS_OK:

            emb = get_embedding(model, image_processed)
            embeddings.append(emb)


            # If this is the first execution of the loop
            # we create a new directory for the .npz files
            try:
                os.mkdir(save_path)
            except FileExistsError as e:
                pass
            finally:
                pass

            if SAVE_LOCALLY:
                # Logging 
                print('Saving file #{} - {}'.format(i, file.picture_url))

                # Saving the .npz files locally
                np_emp = np.asarray(emb)
                np.savez_compressed(save_path + '/' + str(i), embeddings = emb, file_names = file.picture_url)

            # Stagging to database ...
            prod_feature = ProductFeature(file.product_id, file.store_id, file.picture_url, emb)
            database.session.add(prod_feature)
            print('Saving to remote storage #{} - {}'.format(i, file.picture_url))

        else:
            printf('Error while trying to save #{} - {}'.format(i, file.picture_url))

        # ... Commit to database
        database.session.commit()
        
        i += 1

    return embeddings