from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import logging
logging.basicConfig(level=logging.DEBUG)
# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="http://pwablog-m2.local/graphql")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Provide a GraphQL query
query = gql(
    """
    {
  cmsPage(identifier: "no-route") {
    identifier
    url_key
    title
    content
    content_heading
    page_layout
    meta_title
    meta_description
    meta_keywords
  }
}
"""
)

# Execute the query on the transport
result = client.execute(query)
print(result)