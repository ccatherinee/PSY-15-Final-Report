# PSY-15-Final-Report
PSY 15 Final Paper Data Gathering 

<br/>
In order to run the script, you need to have an active session of the QReport open (e.g. you log in and authenticate in a browser). After you do that, you can manually download the html page containing all the links to the reports for a given semester. Then the code in proc.py (using session data extracted from your active session) sends a curl request to download all the links in the page. Once all the links are downloaded, the script in proc.py searches each report for the course mean and the hour mean. This resulting data is pickled into the file called data. Lastly viz.py takes the file data and produces visualizations. 
<br/>
