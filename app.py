from flask import Flask, render_template

app = Flask(__name__, static_folder='public', static_url_path='/')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    # If the user provides a home.html in the new style later, it will be served here. 
    # For now, we will just serve our-story.html as the placeholder for home to avoid confusion 
    # since we don't have a new style home.html, or we can just serve the old home.html.
    # Actually, let's serve real-weddings.html as home if home.html is old, but wait, 
    # the user didn't provide home.html, so let's just serve home.html
    return render_template('home.html')

@app.route('/our-story')
def our_story():
    return render_template('our-story.html')

@app.route('/wedding-films')
def wedding_films():
    return render_template('wedding-films.html')

@app.route('/real-weddings')
def real_weddings():
    return render_template('real-weddings.html')

@app.route('/client-guide')
def client_guide():
    return render_template('client-guide.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
