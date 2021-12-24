from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
import logging
logging.basicConfig(level=logging.DEBUG)
transport = RequestsHTTPTransport(
    url="http://pwablog-m2.local/graphql", verify=True, retries=3,
)

client = Client(transport=transport, fetch_schema_from_transport=True)

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
result = client.execute(query)
print(result)