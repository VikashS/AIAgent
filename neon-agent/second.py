from langchain_community.tools import DuckDuckGoSearchResults




def search_web(query: str) -> str:
  return DuckDuckGoSearchResults(backend="news").run(query)

def search_yf(query: str) -> str:
  engine = DuckDuckGoSearchResults(backend="news")
  return engine.run(f"site:finance.yahoo.com {query}")

# tool_search_web2 = {'type':'function', 'function':{
#   'name': 'search_web',
#   'description': 'Search the web',
#   'parameters': {'type': 'object',
#                 'required': ['query'],
#                 'properties': {
#                     'query': {'type':'str', 'description':'the topic or subject to search on the web'},
# }}}}
# ## test



def start_agent2():
    print(search_yf(query="nvidia"))


if __name__=="__main__":
    start_agent2()
