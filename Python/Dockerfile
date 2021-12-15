FROM thinkwhere/gdal-python

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY ./Data/. /Data/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./processImg.py" ]