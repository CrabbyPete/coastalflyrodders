# coastalflyrodders
Flask app to run coastalflyrodders web page http://coastalflyrodders.com

This page is generated by using Google Spreadsheets and photos on Google Drive. 
Any user that can share the spreadsheet, make changes, and the the web page is rendered
using those changes. Photos are stored on Google Drive and the code searches for them from
the name in the spreadsheet

The file Coastal Calendar.xlxs is stored on the Google Drive. It has 2 sheets. The first is
all the meetings, the second is all the activites scheduled. This code looks for this file
with this name, and looks at both sheets. 
