from flask import render_template
from app import app
from .request import get_sources, get_articles


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    business_sources = get_sources('business')
    entertainment_sources = get_sources('entertainment')
    technology_sources = get_sources('technology')
    sports_sources = get_sources('sports')
    health_sources = get_sources('health')
   
    title = "News"

    return render_template('index.html', title=title, business_sources=business_sources, sports_sources=sports_sources, health_sources=health_sources, technology_sources=technology_sources, entertainment_sources=entertainment_sources)



@app.route('/sources/<id>')
def articles(id):

    '''
    View root page function that returns the articles page and its data
    '''
    
    articles =get_articles(id)
    title = f'{id}'

    return render_template('articles.html', articles=articles, title=title)
