# Automated Chat Bot by Airdrop Variance Authority

A Python script that automatically generates random questions and sends them to the Nous and Hyperbolic API to get responses from the model

## Features

- Generates random questions across various topics
- Sends requests to the Hyperbolic API
- Configurable response parameters
- Random timing between requests (60-120 seconds)
- Graceful shutdown with CTRL+C

## Prerequisites

- Python 3.x
- `requests` and `python-dotenv` library
- Hyperbolic API key with sufficient balance

## Installation

1. Clone this repository or download the script
2. Install the required package:

```
pip install requests python-dotenv
```

3. Add your API key to the script by copy `.env.example` to `.env` and fill it with API key from hyperbolic and nous research.

## Getting an API Key

1. Visit [Hyperbolic Settings Page](https://app.hyperbolic.xyz/settings) and [Nous Research Settings Page](https://portal.nousresearch.com/api-keys) to obtain your API key
2. Ensure you have sufficient balance in your account to make API requests
3. Copy your API key and paste it in the script

## Usage

Simply run the script:

```sh
python hyperbolic.py
python nous.py
```

The script will:

1. Generate a random question
2. Send it to the Hyperbolic and nous API
3. Display the model's response
4. Wait for a random period (60-120 seconds)
5. Repeat the process

To stop the script, press CTRL+C.

## Customization

You can modify the following parts of the script:

- `topics`: Add or remove topics for question generation
- `actions`: Customize the question formats
- `specifics`: Add context variations to questions
- API parameters: Adjust temperature, tokens, and other model settings