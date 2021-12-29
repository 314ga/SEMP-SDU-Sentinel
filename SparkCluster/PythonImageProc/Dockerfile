FROM bde2020/spark-python-template:2.4.3-hadoop2.7

COPY requirements-pyras.txt /
RUN pip install --upgrade pip

COPY submit.sh /

ENV ENABLE_INIT_DAEMON false
ENV SPARK_SUBMIT_ARGS "--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2"

CMD ["/bin/bash", "/template.sh"]