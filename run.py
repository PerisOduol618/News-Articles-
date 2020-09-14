from app import app

if __name__ == '__main__':
    app.run()


# Sources = sources.Sources


# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_SOURCES_BASE_URL"]

articles_base_url = app.config['ARTICLES_BASE_URL']
