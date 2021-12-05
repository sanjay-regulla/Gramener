# Gramener
Project Title :- Scatterplot of imdb (www.imdb.com) top 250 movies.

Description :- The project is to develop a Scatterplot of imdb top 250 movies with rating v/s number of votes.

    I used Linux environment to develop this project.
    Tech Stack :- Python3, Django2.2,CSS3,HTML,Javascript.
    
    I crawled IMDb top 250 movies details using beautifulsoup module and after scrollwing the data from the website, i prepared a list of movies with name and the rating of users. using this data i plotted a scatterplot using Highcharts Scatterplot.
    
Install :- Initial Start by updating the package list using the following command in lixux terminal:
                "sudo apt update"
           Now you can start the installation of Python 3.8 with the command:
                "sudo apt install python3.8"
           Use the following command to install pip for Python 3:
                "sudo apt install python3-pip"
           Then we need to create a virtual environment for running this project 
                "python3 -m venv gramener_venv"
                "source gramener_venv/bin/activate"
              
           Then we need to install requirments.txt file to install the modules requirement for project
                "pip3 install -r /path/requirements.txt"
           Now we need create project using the below command
                "django-admin manage.py startproject Gramener"
           then create app using the below command
                "python3 manage.py startapp ScatterPlot"
                "python3 manage.py migrate"
                "python3 manage.py runserver"
                
           after running the project, open crome browser to open the url.
                "http://127.0.0.1:8000/imdb/"
              
    
