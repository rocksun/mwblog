# Build a Quick Time Series Forecasting App
![Featued image for: Build a Quick Time Series Forecasting App](https://cdn.thenewstack.io/media/2025/05/c0c9e2c8-forecast-1024x620.png)
Ever wondered what the weather will be like in London next month? Or perhaps you’re trying to predict your company’s sales for the upcoming quarter? Welcome to the fascinating world of [time series forecasting](https://thenewstack.io/time-series-forecasting-with-tensorflow-and-influxdb/), a data science technique that lets us peek into the future using historical patterns.

## The Art of Predicting Tomorrow
[Time series forecasting](https://www.influxdata.com/time-series-forecasting-methods/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_ts-forecasting_tns) is at the intersection of statistics, data science and domain expertise. It’s the secret sauce behind numerous business operations, from inventory management to financial planning. This tutorial will illustrate how to build a practical weather forecasting system for notoriously unpredictable London weather.
The data store will be a [time series database](https://www.influxdata.com/time-series-database/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_ts-forecasting_tns), which is highly suitable for time series forecasting due to its focus on time-stamped data.

They are designed to efficiently store and retrieve large volumes of data ordered by time, which is fundamental for analyzing historical trends and patterns.

## Our Toolkit
Three powerful technologies won’t cost you a penny:

: A powerful time series database designed to handle the complexities of storing, processing and analyzing high-volume, high-velocity data for historic time series forecasting. You can use the free trial or the free-at-home license.**InfluxDB 3 Enterprise**: Facebook Research’s robust open source forecasting library handles seasonality and anomaly detection with ease.**Prophet**: A free, comprehensive weather data API with global coverage used to collect London’s weather data from the last six months.**Open-Meteo API**
## Getting Started
**1. Installing InfluxDB 3 Enterprise**: Installation is easy; you can get started for free with just your email address. Run the following command in your terminal and follow the prompt for seamless installation.
1 |
curl-Ohttps://www.influxdata.com/d/install_influxdb3.sh&&shinstall_influxdb3.shenterprise |
**2. Start InfluxDB 3 Enterprise** with default settings that include a simple cluster and a Parquet file as the local object store.
12345 |
influxdb3 serve \ --node-id host01 \ --cluster-id cluster01 \ --object-store file \ --data-dir ~/.influxdb3 |
**3. Create an admin token** for database operations using the following command:
1 |
influxdb3createtoken--admin--hosthttp://localhost:8181 |
**4. Create a ‘.env’ file** and store the admin token string securely along with following details:
123456 |
INFLUXDB_HOST="localhost:8181"INFLUXDB_TOKEN="your_database_token"INFLUXDB_DATABASE="weather"LONDON_LAT="51.5074"LONDON_LON="-0.1278" |
**5. Python and Prophet Setup**
Finally, install the necessary libraries, such as Prophet, [requests](https://pypi.org/project/requests/) to handle web API requests from Open-Meteo’s API for London weather data, [dotenv](https://pypi.org/project/python-dotenv/) to store credentials in an environment file, and [InfluxDB v3 Client Library](https://github.com/InfluxCommunity/influxdb3-python) to communicate easily with InfluxDB 3 Enterprise.

1 |
pipinstallinfluxdb3-pythonprophetrequestspython-dotenv |
## Step 1: Collecting Historical Weather Data
The journey begins with collecting London’s temperature data. Use the Open-Meteo API to grab six months of historical data and store it efficiently in InfluxDB. Create a Python script and name it `main.py`
.

12345678910 |
# In main.py from weather_client import fetch_weather_datafrom influxdb_client import DBClientweather_data = fetch_weather_data()df = process_api_response(weather_data) # This function parses the API responsedb = DBClient()db.write_weather_data(df) # Efficiently writes data to InfluxDBprint("Weather data written to InfluxDB") |
Our DBClient class handles the heavy lifting of batch writing to the local InfluxDB 3 Enterprise instance for optimal performance.
## Step 2: Retrieving Weather Data
With the data safely stored, it can be retrieved using a straightforward SQL query. Create a Python script and name it `influxdb_client.py`
.

123456789 |
# influxdb_client.py def read_data(self): query = """ SELECT time, temperature FROM "weather-london" WHERE time >= now() - interval '180 days' ORDER BY time ASC """ return self.client.query(query=query) |
## Step 3: Crystal Ball Time – Forecasting With Prophet
Now, for the exciting part: using Prophet to generate predictions for London’s temperature over the next month. Create a Python script and name it `forecasting.py`
.

123456789101112 |
# forecasting.pyfrom influxdb_client import DBClientfrom prophet import Prophetdb = DBClient()df = db.read_data().to_pandas() # Get data from InfluxDBmodel = Prophet(yearly_seasonality=True, daily_seasonality=True)model.fit(df)future = model.make_future_dataframe(periods=30*24, freq='h') # Forecast 1 month aheadforecast = model.predict(future) |
## The Forecasting Choice: Machine Learning vs. Statistical Methods
Forecasting is not new, [especially for time series data](https://thenewstack.io/data-modeling-part-2-method-for-time-series-databases/). Popular approaches include statistical methods and [machine learning models](https://thenewstack.io/deploying-scalable-machine-learning-models-for-long-term-sustainability/). The key differences between the two are:

### Machine Learning Methods (like Prophet):
- Excel at detecting complex, nonlinear patterns
- Automatically handle seasonality and trend changes
- Require minimal manual tweaking
- Work better with larger data sets
### Traditional Statistical Methods (like ARIMA):
- Provide clearer interpretability
- Perform well, even with limited data
- Consume fewer computational resources
- Often require more statistical expertise
### The New Kid on the Block: Time Series LLMs
[Large language models](https://thenewstack.io/7-guiding-principles-for-working-with-llms/) specifically trained for time series analysis are emerging as a fascinating frontier:
**Advantages**:
- Can potentially forecast without explicit training (zero-shot learning)
- May generalize well across different types of time series data
**Limitations**:
- Still in early development stages
- Computationally intensive
- Often lack interpretability
- May struggle with long-term accuracy
**Real-Time vs. Batch Processing**
Our example uses batch processing, analyzing fixed data sets to make predictions. This works perfectly for weather forecasting, which doesn’t require up-to-the-second updates. However, for applications like financial trading or IoT sensor monitoring that might require real-time forecasting, the [Processing Engine](https://docs.influxdata.com/influxdb3/enterprise/plugins/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_ts-forecasting_tns) in InfluxDB 3 Core/Enterprise is ideal.

**Wrapping Up**
[Time series forecasting](https://thenewstack.io/what-is-time-series-forecasting/) unlocks incredible possibilities across industries. With tools like Prophet and InfluxDB becoming increasingly accessible, you can start implementing sophisticated forecasting solutions with minimal overhead.
The landscape continues to evolve rapidly, with [time series LLMs representing the cutting edge](https://thenewstack.io/bridging-time-series-from-edge-to-cloud/). Stay curious, keep experimenting and your forecasting skills will become increasingly valuable in our data-driven world.

Don’t hesitate to join our [community discussion](https://community.influxdata.com/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_ts-forecasting_tns) with your questions and insights.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)