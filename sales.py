import pandas as pd
import streamlit as st
import matplotlib as mt
import numpy as py
import datetime
import json
import requests

api_Request = "https://api.pipedrive.com/v1//deals?api_token=15c3e2fb8501a925f71db8de534f3bed42345041&user_id=0&filter_id=301&stage_id=0&status=all_not_deleted&start=0&limit=100&sort=&owned_by_you="
results= requests.get(api_Request).json()
results_dataframe = pd.DataFrame(data=results, columns=['id'])
results_flattened = pd.json_normalize(results, record_path=['id'])

df = pd.read_json(results)

print(results_dataframe)

