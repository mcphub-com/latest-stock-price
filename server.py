import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/suneetk92/api/latest-stock-price'

mcp = FastMCP('latest-stock-price')

@mcp.tool()
def equities_search(Search: Annotated[str, Field(description='Define Search text. Search based on name|isin|symbol. Requires at least 2 character.')]) -> dict: 
    '''Search based on name|isin|symbol. Requires at least 2 character.'''
    url = 'https://latest-stock-price.p.rapidapi.com/equities-search'
    headers = {'x-rapidapi-host': 'latest-stock-price.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'Search': Search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def equities_enhanced(Symbols: Annotated[str, Field(description='Define Symbols Supports multiple comma separated Symbols')]) -> dict: 
    '''Latest stock data'''
    url = 'https://latest-stock-price.p.rapidapi.com/equities-enhanced'
    headers = {'x-rapidapi-host': 'latest-stock-price.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'Symbols': Symbols,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def equities(ISIN: Annotated[Union[str, None], Field(description='Define ISIN Supports multiple comma separated ISIN')] = None,
             OnlyIndex: Annotated[Union[bool, None], Field(description='Show only indices value')] = None,
             Indicies: Annotated[Union[str, None], Field(description='Define Index Code Supports multiple comma separated Index Code Possible values: BANKNIFTY CNX100 CNX200 CNX500 CNXALPHA CNXAUTO CNXCOMMO CNXCONSM CNXDEFTY CNXDIVOPT CNXENER CNXFIN CNXFMCG CNXHIGH CNXINFRA CNXIT CNXLOW CNXLOWV30 CNXMCAP CNXMEDIA CNXMETAL CNXMNC CNXNFTYJUN CNXPHAR CNXPSE CNXPSU CNXREALTY CNXSCAP CNXSERV CPSE INDIAVIX LIX15 LIX15MCAP LRGMID250 NI15 NIFADIBIR NIFESG NIFFINEX NIFFINSE NIFIND NIFMAHI NIFMIC NIFMIDS NIFMIDSE NIFMOM NIFMUL NIFREIN NIFSMQUA NIFTALPF NIFTATGRO NIFTATGRO25PC NIFTCOHOUS NIFTDEFE NIFTHOUS NIFTMANU NIFTMFIN NIFTMHEA NIFTMIT NIFTMOBI NIFTMOME NIFTNON NIFTPR1X NIFTPR2X NIFTRA NIFTTOTA NIFTTR1X NIFTTR2X NIFTY NIFTY100EQW NIFTY100ESG NIFTY200QUA NIFTY500VAL NIFTYALP NIFTYALPHQUAL NIFTYALPHVOLT30 NIFTYCON NIFTYDIV NIFTYEQUWEI NIFTYM150 NIFTYM50 NIFTYMIDQUA NIFTYMSC400 NIFTYOIL NIFTYPVTBANK NIFTYQUALVOLT30 NIFTYSCAP250 NIFTYSCAP50 NIFTYSME NIFTYVALUEVOLT30 NSEHCARE NSEQ30 NV20')] = None) -> dict: 
    '''Latest stock data'''
    url = 'https://latest-stock-price.p.rapidapi.com/equities'
    headers = {'x-rapidapi-host': 'latest-stock-price.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ISIN': ISIN,
        'OnlyIndex': OnlyIndex,
        'Indicies': Indicies,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def timeseries(Symbol: Annotated[str, Field(description='')],
               Timescale: Annotated[Union[int, float], Field(description='Define Timescale for timeseries data Unit: minutes Possible values: >0 (for MEGA), >1 (for ULTRA and PRO) Default: 1 Default: 1')],
               Period: Annotated[str, Field(description='Define Period for timeseries data Default: 1DAY Possible values: DAY (1DAY, 5DAY....) WEEK (1WEEK , 4WEEK ....) MONTH (1MONTH , 3MONTH ....) YEAR (1YEAR , 3YEAR ....)')]) -> dict: 
    '''Get timeseries data for given symbol'''
    url = 'https://latest-stock-price.p.rapidapi.com/timeseries'
    headers = {'x-rapidapi-host': 'latest-stock-price.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'Symbol': Symbol,
        'Timescale': Timescale,
        'Period': Period,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def price_all(Identifier: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Fetch latest stock price'''
    url = 'https://latest-stock-price.p.rapidapi.com/any'
    headers = {'x-rapidapi-host': 'latest-stock-price.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'Identifier': Identifier,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
