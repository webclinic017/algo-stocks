from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import logging
logging.basicConfig(level=logging.DEBUG)
# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="https://gateway-iboard.ssi.com.vn/graphql")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Provide a GraphQL query
query = gql(
    """
    query stockRealtimes($exchange: String) {
  stockRealtimes(exchange: $exchange) {
    stockNo
    __typename
  }
}
"""
)

params = {"exchange": "hose"}

# Execute the query on the transport
result = client.execute(query, variable_values=params)
print(result)