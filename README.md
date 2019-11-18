# CryptoBytes
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/arcmena/cryptobytes.svg)

An cryptocurrency capitalization API made with the REST API Flask in Python, with base in the live CoinMarketCap API.

---------------

## Getting Started

CrypToBytes is a live cryptocurrency capitalization API made for search and consulting the values, IDs and overall everything you need to get updated in the current state of the market.

### Installing

To install the repository and start working on your implementation open your terminal, go to your project folder and type:
```
git clone https://github.com/arcmena/cryptobytes .
```
It will clone the repository inside your project folder.

Then make sure to set up a virtual development environment with virtualenv. Go to your project folder and type: 
```
virtualenv .venv
```
Install ```requests``` and ```flask``` and start the server with ```source .venv/Script/activate```

Access the link 127.0.0.1:5000 and you can start the tests.

## Dependencies
- flask
- requests

## Usage

Used for adding a website/portal the function to search the coin by their ID, aswell as show the top ten coins in the market at the moment of search!

- Comands: 
- ```/coin``` to see all the coins informations.
- ```/(coin id, example: dogecoin)```to see only the requested coin informations.
- ```/coin/topten```to see the top ten most valued coins in the market!

## Authors

* **Marcelo Mena** - [arcmena](https://github.com/arcmena)
