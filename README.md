# CryptoBytes API
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/arcmena/cryptobytes.svg)

A cryptocurrency capitalization API made with Flask.

---------------

## Getting Started

CryptoBytes is a live cryptocurrency capitalization API. Stay updated in the current state of the market.

### Installing

To install the repository and start working on your implementation open your terminal, go to your project folder and type:
```
git clone https://github.com/arcmena/cryptobytes .
```
It will clone the repository inside your project folder.

Then make sure to set up a virtual development environment with virtualenv. Go to your project folder and type: 
```
pip install virtualenv
virtualenv .venv
```
Install ```requests``` and ```flask``` dependencies, then start the server with ```source .venv/Script/activate```

Access http://localhost:5000 and check for usage below.

## Usage

The endpoints are:

- ```/coin``` - to get all the cryptocurrencies data.
- ```/coin/[id]``` - to search for a specific cryptocurrency data where "[id]" is the id of the cryptocurrency (example of id: dogecoin).
- ```/coin/topten``` - to get the top ten cryptocurriencies by market value.

## Dependencies
- flask
- flask_cors
- requests

## Authors

* **Marcelo Mena** - [arcmena](https://github.com/arcmena)