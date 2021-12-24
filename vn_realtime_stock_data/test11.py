import asyncio

from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport


async def main():

    transport = AIOHTTPTransport(url="https://gateway-iboard.ssi.com.vn/graphql")

    # Using `async with` on the client will start a connection on the transport
    # and provide a `session` variable to execute queries on this connection
    async with Client(
        transport=transport, fetch_schema_from_transport=True,
    ) as session:

        # Execute single query
        query = gql(
            """
            query stockRealtimes($exchange: String) {
              stockRealtimes(exchange: $exchange) {
                stockNo
                ceiling
                floor
                refPrice
                stockSymbol
                stockType
                exchange
                matchedPrice
                matchedVolume
                priceChange
                priceChangePercent
                highest
                avgPrice
                lowest
                nmTotalTradedQty
                best1Bid
                best1BidVol
                best2Bid
                best2BidVol
                best3Bid
                best3BidVol
                best4Bid
                best4BidVol
                best5Bid
                best5BidVol
                best6Bid
                best6BidVol
                best7Bid
                best7BidVol
                best8Bid
                best8BidVol
                best9Bid
                best9BidVol
                best10Bid
                best10BidVol
                best1Offer
                best1OfferVol
                best2Offer
                best2OfferVol
                best3Offer
                best3OfferVol
                best4Offer
                best4OfferVol
                best5Offer
                best5OfferVol
                best6Offer
                best6OfferVol
                best7Offer
                best7OfferVol
                best8Offer
                best8OfferVol
                best9Offer
                best9OfferVol
                best10Offer
                best10OfferVol
                buyForeignQtty
                buyForeignValue
                sellForeignQtty
                sellForeignValue
                caStatus
                tradingStatus
                currentBidQty
                currentOfferQty
                remainForeignQtty
                session
                __typename
              }
            }
        """
        )
        params = {"exchange": "hose"}

        # Execute the query on the transport
        result = await session.execute(query, variable_values=params)
        print(result)

asyncio.run(main())
