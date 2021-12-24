from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
import logging
logging.basicConfig(level=logging.DEBUG)
transport = RequestsHTTPTransport(
    url="https://gateway-iboard.ssi.com.vn/graphql", verify=True, retries=3,
)

client = Client(transport=transport, fetch_schema_from_transport=True)

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
result = client.execute(query, variable_values=params)
print(result)