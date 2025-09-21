from langchain_community.document_loaders import WebBaseLoader

def load_portfolio(url):
    loader = WebBaseLoader([url])
    return loader.load()
