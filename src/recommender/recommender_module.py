
import os
import pandas as pd
from pathlib import Path
import json
import logging

from src.config.settings import settings

LOG_FILE = os.path.join(settings.LOG_DIR, "app.log")
INPUT_NAME = settings.INPUT_NAME
RESULT_NAME = settings.RESULT_NAME

# Configure logging
logging.basicConfig(
    level=logging.INFO,                           # logging level
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),           # save to file
        logging.StreamHandler()                  # also print to console
    ]
)

# l_feature = ['性别','年龄','国籍','职业','形象','粉丝性别','粉丝年龄','粉丝城市级别','粉丝区域','粉丝省份']
# l_feature_detailed_celebrity = ['性别_男', '年龄_90后', '国籍_中国', '职业_网红', '粉丝-性别_女', '粉丝-年龄_18-24', '粉丝-城市级别_一线城市', '粉丝-区域_华东']
# INPUT_FILE = r'C:\Users\lwjen\PycharmProjects\Proj001\SelfRepo001\misc_code\agent\assignment\KOL-Recommender\input\raw_data\KOL_Database.xlsx'

########################################################################################################################

def jaacard_similarity(l_feature_detailed_celebrity,kol_feature):
    full_set_len = len(set(l_feature_detailed_celebrity+kol_feature))
    common_set_len = len(list(set(l_feature_detailed_celebrity) & set(kol_feature)))
    return common_set_len/full_set_len


def recommender_func(l_feature,l_feature_detailed_celebrity,top_n):
    logging.info("Data Processing & Feature Parsing -- commencing ...")
    df = pd.read_excel(INPUT_NAME)
    df = df[['KOL']+l_feature]
    print(df.columns)
    df_encoded = pd.get_dummies(df, columns=l_feature)

    print(df_encoded.columns)
    dummy_cols = [c for c in df_encoded.columns if any(c.startswith(f + "_") for f in l_feature)]
    print(dummy_cols)

    df_encoded["kol_active_features"] = df_encoded[dummy_cols].apply(
        lambda row: [col for col, val in row.items() if val == 1],
        axis=1
    )
    logging.info("Data Processing & Feature Parsing -- completed ...")

    logging.info("Similarity score computation -- commencing ...")
    df_encoded['jaacard_similarity'] = df_encoded['kol_active_features'].apply(lambda x:jaacard_similarity(l_feature_detailed_celebrity,x))
    logging.info("Similarity score computation -- completed ...")
    print(df_encoded)
    df_encoded = df_encoded.sort_values(by=['jaacard_similarity'],ascending=False)
    df_encoded = df_encoded.head(top_n)
    logging.info(f"Top {top_n} selection -- completed ...")
    df_encoded = df_encoded[['KOL','kol_active_features','jaacard_similarity']]
    df_encoded.to_excel(RESULT_NAME,index=False)
    logging.info(f"Excel output -- completed ...")
    return df_encoded





# import pandas as pd
# INPUT_FILE = r'C:\Users\lwjen\PycharmProjects\Proj001\SelfRepo001\misc_code\agent\assignment\KOL-Recommender\input\raw_data\KOL_Database.xlsx'
#
# l_feature = ['性别','粉丝年龄']
# df = pd.read_excel(INPUT_FILE)
# df = df[['KOL'] + l_feature]
# print(df.columns)
#
# print(df['粉丝年龄'].unique())
# df_encoded = pd.get_dummies(df, columns=l_feature)
# print(df_encoded.columns)

