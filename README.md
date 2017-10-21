# Movie_Trailer_Website
The files necessary to create the Movie Trailer Website from Udacity's Full Stack Web Dev Nanodegree.

#### As the title and description suggest, this is a project that is focused on meeting the requirements of the Udacity Full Stack Web Dev Nanodegree's "Create a Movie Trailer Website" project.
    
This "program" uses multiple .py files to generate a website currently consisting of six (6) movie trailers.
This number can be scaled by adding to the "entertainment_center.py" file.

### How it works

#### There are three (3) main files used in this project:

    * fresh_tomatoes.py - Provided by Udacity to generate the website, with minor edits to add ratings and scores.
    
    * media.py - Created for the sake of creating the "Movie" class.
    
    * entertainment_center.py - Created to leverage the Movie class and enter the details needed to populate the site.

* To add movies to the site, edit entertainment_center.py with the title, storyline, poster URL, trailer URL, critical score, and rating.

### Running the application

* To run the application, simply place the three (3) files into a single folder, and execute the ____entertainment_center.py____ file.  This will run the application, gather the information on your movies, and generate/open the newly created "fresh tomatoes" html file in your browser.

### Running the application from the terminal

* As before, the application's files will need to be downloaded to the local machine to run the application.  Python will also need to be downloaded and installed.  The installer(s) can be found at https://www.python.org/downloads/.
* With the application downloaded and python installed, open an instance of terminal (command prompt/cmd in Windows).
* cd (change directory) to wherever the downloaded application files reside.
    * For example, if you have them in a folder called "movie_site" in your "downloads" folder you can use the following commands:
        * OSX (Mac) 'cd cd Downloads/movie_site/'
        * Windows 'cd driveletter:\users\youraccount\downloads\movie_site\' ex: C:\users\me\downloads\movie_site\
* Once in the correct folder enter the command 'python entertainment_center.py" to use Python to run the entertainment_center file.  This will run the application and generate/display the website with the movie information.
