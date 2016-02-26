
import os
import gspread

from datetime                       import datetime
from oauth2client.service_account   import ServiceAccountCredentials
from flask                          import Flask, render_template

app = Flask(__name__, static_url_path='/static')

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

credentials = ServiceAccountCredentials.from_json_keyfile_name( CURRENT_DIR + '/coastal.json', 
                                                                 scopes = ['https://spreadsheets.google.com/feeds',
                                                                           'https://www.googleapis.com/auth/drive' ]
                                                              )
SpreadSheet = gspread.authorize(credentials)


@app.route('/')
def index():
    calendar = SpreadSheet.open('Coastal Calendar')
    speakers = calendar.worksheet("Speakers")
    
    speaker_details = []
    for r, row in enumerate( speakers.get_all_values()):
        if r == 0:
            continue
 
        day = datetime.strptime(row[0],"%m/%d/%Y")
        speaker_details.append( { 'date'    :day.strftime( "%B %d, %Y" ),
                                  'name'    :row[1],
                                  'photo'   :row[2],
                                  'url'     :row[3],
                                  'describe':row[4]
                              } )
    
    events   = calendar.worksheet('Events')
    event_details = []
    for r,row in enumerate( events.get_all_values()):
        if r == 0:
            continue
 
        day = datetime.strptime(row[0],"%m/%d/%Y")
        event_details.append( { 'date'    :day.strftime( "%a %B %d, %Y" ),
                                'describe':row[1],
                                'place'   :row[2]
                              } )
    
    context = {'speakers':speaker_details, 'events':event_details}
        
    return render_template( 'main.html', **context )

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500

"""
if __name__ == '__main__':     
    app.run(debug = False,  port=8000)
"""