# builder step used to download and configure spark environment
FROM openjdk:11.0.11-jre-slim-buster as builder

# Add Dependencies for PySpark
RUN apt-get update && apt-get install -y curl vim wget software-properties-common ssh net-tools ca-certificates python3.7 python3-pip python3-numpy python3-matplotlib python3-scipy python3-pandas python3-simpy

RUN update-alternatives --install "/usr/bin/python" "python" "$(which python3)" 1

# Fix the value of PYTHONHASHSEED
# Note: this is needed when you use Python 3.3 or greater
ENV SPARK_VERSION=2.4.4 \
    HADOOP_VERSION=3.2 \
    SPARK_HOME=/opt/spark \
    PYTHONHASHSEED=1

# Download and uncompress spark from the apache archive
RUN wget --no-verbose -O apache-spark.tgz "https://archive.apache.org/dist/spark/spark-2.4.3/spark-2.4.3-bin-hadoop2.6.tgz" \
    && mkdir -p /opt/spark \
    && tar -xf apache-spark.tgz -C /opt/spark --strip-components=1 \
    && rm apache-spark.tgz


# Apache spark environment
FROM builder as apache-spark

WORKDIR /opt/spark

COPY jdk-8u311-linux-x64.tar.gz /opt/

RUN tar -xvf /opt/jdk-8u311-linux-x64.tar.gz -C /usr/local && \
    rm /opt/jdk-8u311-linux-x64.tar.gz && cd /usr/local

ENV SPARK_MASTER_PORT=7077 \
    SPARK_MASTER_WEBUI_PORT=8080 \
    SPARK_LOG_DIR=/opt/spark/logs \
    SPARK_MASTER_LOG=/opt/spark/logs/spark-master.out \
    SPARK_WORKER_LOG=/opt/spark/logs/spark-worker.out \
    SPARK_WORKER_WEBUI_PORT=8080 \
    SPARK_WORKER_PORT=7000 \
    SPARK_MASTER="spark://spark-master:7077" \
    SPARK_WORKLOAD="master"

EXPOSE 8080 7077 6066

RUN mkdir -p $SPARK_LOG_DIR && \
    touch $SPARK_MASTER_LOG && \
    touch $SPARK_WORKER_LOG && \
    ln -sf /dev/stdout $SPARK_MASTER_LOG && \
    ln -sf /dev/stdout $SPARK_WORKER_LOG

RUN apt-get install python3.7-dev && \
    apt-get install -y gdal-bin && \
    apt-get install -y libgdal-dev && \
    export CPLUS_INCLUDE_PATH=/usr/include/gdal && \
    export C_INCLUDE_PATH=/usr/include/gdal && \
    pip3 install GDAL==2.4.4 && \
    pip3 install proj && \
    pip3 install setuptools==57.5.0 && \
    pip3 install --upgrade pip && \
    apt-get install -y python3-pyproj && \
    apt-get install -y python-wheel && \
    apt-get install  libgdal-doc && \
    python3 -m pip install pyrasterframes==0.9.0

RUN wget https://archive.apache.org/dist/hadoop/core/hadoop-2.7.4/hadoop-2.7.4.tar.gz && \
    tar -xvf hadoop-2.7.4.tar.gz -C /opt/ && \
    rm hadoop-2.7.4.tar.gz && cd /opt && \
    echo "export HADOOP_HOME=/opt/hadoop-2.7.4" >> ~/.bashrc && \
    echo "export PATH=\$PATH:\$HADOOP_HOME/bin:\$HADOOP_HOME/sbin" >> ~/.bashrc && \
    . ~/.bashrc

RUN wget http://mirrors.ocf.berkeley.edu/apache/hive/hive-3.1.2/apache-hive-3.1.2-bin.tar.gz && \
    tar -xvf apache-hive-3.1.2-bin.tar.gz -C /opt/ && \
    rm apache-hive-3.1.2-bin.tar.gz && \
    echo "export HIVE_HOME=/opt/apache-hive-3.1.2-bin" >> ~/.bashrc && \
    echo "export PATH=\$PATH:\$HIVE_HOME/bin" >> ~/.bashrc && \
    . ~/.bashrc && \
    echo "export HADOOP_HOME=/opt/hadoop-2.7.4" >> /opt/apache-hive-3.1.2-bin/bin/hive-config.sh && \
    hdfs dfs -mkdir /user && \
    hdfs dfs -mkdir /user/hive && \
    hdfs dfs -mkdir /user/hive/warehouse && \
    hdfs dfs -chmod g+w /user/hive/warehouse && \
    hdfs dfs -chmod g+w /tmp && \
    cd /opt/apache-hive-3.1.2-bin/conf && \
    mv hive-default.xml.template hive.default.xml && \
    cd /opt/spark/conf && \
    mv log4j.properties.template log4j.properties

ENV JAVA_HOME=/usr/local/jdk1.8.0_311

RUN /opt/apache-hive-3.1.2-bin/bin/hive && \
    . ~/.bashrc

COPY start-spark.sh /

CMD ["/bin/bash", "/start-spark.sh"]