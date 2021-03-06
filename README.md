# scrapy-pharmacy
Getting information about medicines from an online pharmacy

## Requirements

Python 3.6+

## How to run it?

Clone the repository and enter to the newly created directory
```console
user@host:~$ git clone https://github.com/maciej-zieniewicz/scrapy-pharmacy.git
user@host:~$ cd scrapy-pharmacy/pharmacy/

```

Create a virtual environment
```console
user@host:~$ python -m venv venv
```

Run virtual environment (Windows)
```console
user@host:~$ venv/Scripts/activate
```

Install required libraries
```console
user@host:~$ pip install -r requirements.txt
```

Run crawler with scrapy (saves data into sqlite database)
```console
user@host:~$ scrapy crawl pharmacy-doz 
```

You can also run both spiders simultaneously with python
```console
user@host:~$ python run_scrapers.py 
```
