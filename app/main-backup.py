# Run by typing python3 main.py

## **IMPORTANT:** only collaborators on the project where you run
## this can access this web server!

"""
    Bonus points if you want to have internship at AI Camp
    1. How can we save what user built? And if we can save them, like allow them to publish, can we load the saved results back on the home page? 
    2. Can you add a button for each generated item at the frontend to just allow that item to be added to the story that the user is building? 
    3. What other features you'd like to develop to help AI write better with a user? 
    4. How to speed up the model run? Quantize the model? Using a GPU to run the model? 
"""

# import basics
import os

# import stuff for our web server
from flask import Flask, flash, request, redirect, url_for, render_template
from flask import send_from_directory
from flask import jsonify
from utils import get_base_url, allowed_file, and_syntax

# import stuff for our models
import torch
from aitextgen import aitextgen

'''
Coding center code - comment out the following 4 lines of code when ready for production
'''


# setup the webserver
# port may need to be changed if there are multiple flask servers running on same server
port = 12345
base_url = get_base_url(port)
app = Flask(__name__, static_url_path=base_url+'static')
the_folder = ""
global genre

'''
Deployment code - uncomment the following line of code when ready for production
'''
#app = Flask(__name__)

#@app.route('/')
@app.route(base_url)
def home():
    return render_template('home.html', generated=None)

#@app.route('/', methods=['POST'])
@app.route(base_url, methods=['POST'])
def home_post():
    return redirect(url_for('results'))

#@app.route('/results')
@app.route(base_url + '/results')
def results():
    return render_template('Write-your-story-with-AI.html', generated=None)

#@app.route('/genre', methods=["POST"])
@app.route(base_url + '/genre', methods=["POST"])
def genre():

    # get number 0-5 for genre
    genre = request.form['genre']
    # change model folder based on in
    if genre == 0:
        the_folder = "DystopianModel"
    elif genre == 1:
        the_folder = "FantasyModel"
    elif genre == 2:
        the_folder = "SciFiModel"
    elif genre ==3:
        the_folder = "HistoricalModel"
    elif genre == 4:
        the_folder = "RomanceModel"
    else:
        the_folder = "HorrorModel"

#@app.route('/generate_text', methods=["POST"])
@app.route(base_url + '/generate_text', methods=["POST"])
def generate_text():
    """
    view function that will return json response for generated text. 
    """
    # get number 0-5 for genre
    genre = request.form['genre']
    genre = int(genre)
    # change model folder based on in
    if genre == 0:
        the_folder = "DystopianModel"
    elif genre == 1:
        the_folder = "FantasyModel"
    elif genre == 2:
        the_folder = "SciFiModel"
    elif genre ==3:
        the_folder = "HistoricalModel"
    elif genre == 4:
        the_folder = "RomanceModel"
    else:
        the_folder = "HorrorModel"

    # load up the model into memory
    # you will need to have all your trained model in the app/ directory.
    ai = aitextgen(model_folder= the_folder, to_gpu=False)
    print(str(genre))
    print(the_folder)
    prompt = request.form['prompt']

    if prompt is not None:
        generated = ai.generate(
            n=3,
            batch_size=1,
            prompt=str(prompt),
            min_length = len(prompt.split(" ")) + 50,
            max_length = len(prompt.split(" ")) + 65,
            temperature=0.9,
            return_as_list=True
        )
    for i in range(0,3):
        generated[i] = generated[i].replace(str(prompt),'')
        #generated[i] = re.sub(r'\W')

    data = {'generated_ls': generated}




    return jsonify(data)

if __name__ == "__main__":
    '''
    coding center code
    '''
    # IMPORTANT: change the cocalcx.ai-camp.org to the site where you are editing this file.
    website_url = 'cocalc5.ai-camp.org'
    print(f"Try to open\n\n    https://{website_url}" + base_url + '\n\n')

    app.run(host = '0.0.0.0', port=port, debug=True)
    import sys; sys.exit(0)

    '''
    scaffold code
    '''
    # Only for debugging while developing
    # app.run(port=80, debug=True)
