FROM thinkwhere/gdal-python

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN mkdir -p data
COPY data/* data/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python","-u", "./processImg.py" ]