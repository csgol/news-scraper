import config
import requests

def get_company_news(company_name, api_key):
  api_key = config.NEWS_API_KEY
  """
  Fetches news articles about a company using the News API.

  Args:
      company_name: The name of the company to search for.
      api_key: Your News API key.

  Returns:
      A list of dictionaries containing news articles.
  """
  url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey={api_key}"
  response = requests.get(url)
  
  if response.status_code == 200:
    data = response.json()
    articles = data["articles"]
    return articles
  else:
    print(f"Error: {response.status_code}")
    return []

# Example usage
company = input("Enter company name: ")
api_key = "YOUR_NEWS_API_KEY"  # Replace with your actual key
news_articles = get_company_news(company, api_key)

if news_articles:
  print(f"\n** News about {company.capitalize()} **")
  for article in news_articles:
    print(f"- {article['title']}")
    print(f"  Link: {article['url']}\n")
else:
  print("No news found for this company.")