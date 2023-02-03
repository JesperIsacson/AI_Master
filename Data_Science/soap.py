from zeep import Client

client = Client(wsdl="https://swea.riksbank.se/sweaWS/docs/api/call/getInterestAndExchangeRates.htm?wsdl")
