# most-frequent-words
Find the most frequent words in a set of documents

Run commands
Unzip the folder and go to the folder in the terminal and run the following commands

# Build the docker image
docker build -t "seldonmodel:Dockerfile" .

# run the Image 
docker run --publish 5000:5000 --name sm seldonmodel:Dockerfile

On the browser go to  
http://localhost:5000/

In the Most common field Type the number of how many frequent words you want to find.
In the choose file add a zip file which combines all the text documents.
One sample zip file I have provided in the uploads folder when you unzip the code
