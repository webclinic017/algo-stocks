def getTodayData(exchange = "hose"):
    from python_graphql_client import GraphqlClient
    # Instantiate the client with an endpoint.
    client = GraphqlClient(endpoint="https://gateway-iboard.ssi.com.vn/graphql")

    # Create the query string and variables required for the request.
    query = """
        query stockRealtimes($exchange: String) {
          stockRealtimes(exchange: $exchange) {
            stockSymbol
            refPrice
            openPrice
            matchedPrice
            priceChange
            priceChangePercent
            highest
            avgPrice
            lowest
            nmTotalTradedQty
          }
        }
    """
    variables = {"exchange": exchange}

    # Asynchronous request
    import asyncio

    data = asyncio.run(client.execute_async(query=query, variables=variables))
    return data['data']['stockRealtimes']