import json
#from starlette.responses import Response
#from starlette.routing import request_response
import streamlit as st
import requests
import datetime

'''
# TaxiFareModel front
'''

date = st.date_input("Fecha en la que desea viajar")
time = st.time_input("Hora en la que desea viajar")
lon1 = st.number_input('Longitud de origen')
lat1 = st.number_input('Latitud de origen')
lon2 = st.number_input('Longitud destino')
lat2 = st.number_input('latitud destino')
passcount = st.number_input('Cantidad de pasajeros')

params = {
        "pickup_datetime": [f'{date} {time}'],
        "pickup_longitude": [float(lon1)],
        "pickup_latitude": [float(lat1)],
        "dropoff_longitude": [float(lon2)],
        "dropoff_latitude": [float(lat2)],
        "passenger_count": [int(passcount)]}

api = requests.get('https://taxifare.lewagon.ai/predict', params=params)
prediction = api.json()

# st.json(prediction)


st.write(prediction)

# params = {
#         "pickup_datetime": [pickup_datetime + " UTC"],
#         "pickup_longitude": [float(lon1)],
#         "pickup_latitude": [float(lat1)],
#         "dropoff_longitude": [float(lon2)],
#         "dropoff_latitude": [float(lat2)],
#         "passenger_count": [int(passcount)]}

# api = request.get(https://taxifare.lewagon.ai/predict, params=params)


# response = api.json()
'''
# TaxiFareModel front
'''










# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')
# '''


# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''
# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

# url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown(
#         'Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...'
#     )
# '''

# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''
