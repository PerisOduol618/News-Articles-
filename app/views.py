from flask import render_template


@app.route('/news/<int:news_id>')
def index(news_id):
    '''
    View news page function that returns the news details page and its data
    '''

    return render_template('news.html',id = news_id)
    
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Hello welcome to News Article'
    return render_template('index.html', title = title)