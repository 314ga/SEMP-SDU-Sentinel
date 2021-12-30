# set image to use
#to check images-> docker images
FROM python:3.6 
# Run is used to run operations inside the container, 
# In this case, we're creating the folder where our application will run in the container.
RUN mkdir /usr/src/app/
# It's going to copy everything from 
# ./ local directory and move to /usr/src/app/ host directory.
COPY . /usr/src/app/
# It sets the path where the CMD and the RUN commands will run.
WORKDIR /usr/src/app/
# Exposes the port 5000 of the container to be external accessed.
EXPOSE 5000
# Executes when the image is been generated. It works for when you want to install something in the image.
RUN pip install -r requirements.txt
CMD ["python", "api.py"]