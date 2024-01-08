import json
import os
from whoosh.fields import Schema, TEXT, ID
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser

def create_index(data):
    schema = Schema(title=TEXT(stored=True), link=ID(stored=True), description=TEXT(stored=True), timestamp=TEXT(stored=True))

    # Create the index directory if it doesn't exist
    index_dir = "indexdir"
    if not os.path.exists(index_dir):
        os.makedirs(index_dir)

    # Create or open the index in the directory
    ix = create_in(index_dir, schema)
    writer = ix.writer()

    # Add documents to the index
    for entry in data:
        writer.add_document(title=entry['title'], link=entry['link'], description=entry.get('description'))

    # Commit changes
    writer.commit()

def search_index(query_string, data):
    # Open the existing index
    ix = open_dir("indexdir")

    # Create a searcher object
    searcher = ix.searcher()

    # Parse the user's query
    query_parser = QueryParser("title", ix.schema)
    query = query_parser.parse(query_string)

    # Perform the search
    results = searcher.search(query)

    # Return the results
    return results
