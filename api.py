import flask
from flask import request, jsonify
from flask import send_file
from imageai.Detection import ObjectDetection
from Surf_counter.read_video import ReadVidz
from Surf_counter.detector import Detect

from os import listdir
from os.path import isfile, join
import os, shutil 
import imageai
from Surf_counter.spot_urls import SpotUrls
from Surf_counter.scrape_video_links import ScrapeVideoLinks


app = flask.Flask(__name__)
app.config["DEBUG"] = True


#To put this back inside:
#This error seem to be solved after i add K.clear_session() before return of method
#  detectCustomObjectsFromImage in /imageai/Detection/__init__.py

det=Detect()
# det.clear_data_dir()
# #Find the video
# url=SpotUrls.lookup['venice_beach']
# v=ScrapeVideoLinks(url)
# link=v.get_link()
# det.pull_images(link)
# n_surfers=det.detection()
# print("WTF!")
# print(n_surfers)

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

# def do_prediction():
#     det=Detect()
#     det.clear_data_dir()
#     #Find the video
#     url=SpotUrls.lookup['venice_beach']
#     v=ScrapeVideoLinks(url)
#     link=v.get_link()
#     det.pull_images(link)
#     n_surfers=det.detection()
#     return n_surfers

#@app.route('/api/v1/breakwater/count', methods=['GET'])
@app.route('/api/v1/breakwater/count')
def api_surfercount():
    det.clear_data_dir()
    #Find the video
    url=SpotUrls.lookup['venice_beach']
    v=ScrapeVideoLinks(url)
    link=v.get_link()
    det.pull_images(link)
    n_surfers=det.detection()
    n_surfers=det.detection()
    print ("THERE ARE N SURFERS ", n_surfers)
    return str(n_surfers)
    #output=f'''There are currently {surfer_count} surfers at the Breakwater'''
    #return jsonify(n_surfers)


    # surfer_count=do_prediction()
    # #surfer_count = 10
    # output=f'''There are currently {surfer_count} surfers at the Breakwater'''
    # return jsonify(output)

# @app.route('/get_image')
# def get_image():
#     if request.args.get('type') == '1':
#        filename = 'data/frame3596.jpg'
#     else:
#        filename = 'frame3596.jpg'
#     return send_file(filename, mimetype='image/jpg')

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run(threaded=False,use_reloader=False)