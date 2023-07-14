import requests
from send_email import send_email


api_key = "0e48e828a9d24c3089695640dcb228d8"
url = "https://newsapi.org/v2/everything?" \
      "q=tesla&" \
      "from=2023-06-13" \
      "sortBy=publishedAt&" \
      f"apiKey={api_key}&" \
      "language=es"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = "Subject: Today's news"
for article in content["articles"][:20]:    # Select the first 20 news
    if article["title"] and article["description"] is not None:
        body = body + "\n" + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["url"] + "\n\n"

body = body.encode("utf-8")
send_email(body)