from models.tokenization import *
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from models.model_architecture import *
from models.train_eval import *
from models.model_utils import *
from models.tokenization import *
from tqdm import tqdm, tqdm_notebook
parent_path='../Data/New_Data_15-06-2020/'


#bert-base-multilingual-cased
#xlm-roberta-base
#birnn_laser
params={'model_path':'bert-base-multilingual-cased',
        'preprocess_doc':False,
        'max_length':256,
        'batch_size':32,
        'hidden_size':128,
        'weights':[1.0,1.0],
        'seq_model':'lstm',
        'data_path':parent_path+'Fearspeech_data_final.pkl',
        'max_sentences_per_doc':5,
        'transformer_type':'lstm_transformer',
        'device':'cuda',
        'learning_rate':5e-4,
        'epsilon':1e-8,
        'random_seed':2020,
        'epochs':50,
        'max_memory':0.5
       }



if __name__=='__main__': 
    train_phase(params)