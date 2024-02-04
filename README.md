# BitCoin Price Tracker

<h3> This is a bitcoin price  tracker built  using django and redis.

## Installation

```text
PS: Docker version will be pushed shortly
```
1. Clone the project using git
```bash
git clone https://github.com/thirt33n/price_tracker.git
```

2. Install the requirements

```bash
pip install -r requirements.txt
```

3. Install Redis On your system, if on Debian-Based system run the following comand:

```bash
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis
```
If not on debian system check the redis documentation for installation steps.


## Usage

To start the development server run the following 

```bash
cd price_tracker
python manage.py runserver
```
<br></br>
This starts the django server on port 8000

Navigate to [http://127.0.0.1:8000/api/alerts](http://127.0.0.1:8000/api/alerts) to view all the alerts created.

Fill the form below to create your alerts.

To Start redis server and Celery worker and beat processes run the following commands in different terminal windows:

```bash
redis-server
redis-cli ping #to Check if the redis server is up and running
```
For Celery
```bash
celery -A price_tracker worker -l info
celery -A price_tracker beat -l info

```
<br></br>

### To start the alert background process click on the **Extra Options** button at the top and click on **Check** option


## Working

### It uses Binance [Web Socket](https://github.com/thirt33n/price_tracker/blob/master/price_tracker_app/export_binance.py)  to fetch the average Price of Bitcoin in USD every 2 minutes and checks for created alerts whose target price is more than the current bitcoin value.

### Once this is found, it uses Redis message broker to send an email alert to the particular user's registered email about the current BTC price.

## Video Demo

### In Case you are unable to recreate the project in your system view this video:


https://github.com/thirt33n/price_tracker/assets/55974622/08b5b99b-1f89-4c20-bd12-2530646493f1




## Author

P Siddharth 
