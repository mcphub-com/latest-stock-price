markdown
# Latest Stock Price MCP Server

## Overview

The Latest Stock Price MCP (Marketplace Communication Protocol) Server provides real-time stock price data from the NSE (National Stock Exchange). This service is designed to deliver the latest stock data with a high update frequency, making it an essential tool for traders, investors, and financial analysts.

### Key Features

- **Real-Time Data**: Get the latest stock prices with updates every minute.
- **High Performance**: Enjoy low latency and high service availability.
- **Flexible Pricing Plans**: Choose from different subscription levels to suit your needs.

## Tools and Functions

The server offers a variety of tools to interact with stock data:

### v2 Tools

1. **Equities Search**
   - **Description**: Search for stocks based on name, ISIN, or symbol. Requires a minimum of 2 characters for a search query.
   - **Parameters**: 
     - `Search`: Define search text based on name, ISIN, or symbol.

2. **Equities Enhanced**
   - **Description**: Retrieve the latest stock data.
   - **Parameters**:
     - `Symbols`: Define the symbols for which the data is needed. Supports multiple comma-separated symbols.

3. **Equities**
   - **Description**: Fetch the latest stock data.
   - **Parameters**:
     - `ISIN`: Define ISIN for stock. Supports multiple comma-separated ISINs.
     - `OnlyIndex`: Show only indices value.
     - `Indicies`: Define index code. Supports multiple comma-separated index codes.

4. **Timeseries**
   - **Description**: Obtain timeseries data for a given symbol.
   - **Parameters**:
     - `Symbol`: Define the symbol for which timeseries data is needed.
     - `Timescale`: Define timescale for timeseries data.
     - `Period`: Define the period for timeseries data.

### v1 Tools

1. **Price All**
   - **Description**: Fetch the latest stock prices.
   - **Parameters**:
     - `Identifier`: Optional identifier parameter.

## Usage

The Latest Stock Price MCP Server is designed for easy integration into applications requiring up-to-date stock market data. It supports a wide range of functionalities, from simple stock searches to detailed timeseries analysis, making it a comprehensive solution for financial data needs.

Whether you are developing a financial application, conducting market research, or simply monitoring stock performance, the Latest Stock Price MCP Server provides reliable and accurate data to support your objectives.