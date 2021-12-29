SparkCLuster Folder:
In order to run pyrasterframes on spark master:

1. Add missing JAR dependency:
   cd /root/.ivy2/jars/
   curl https://repo1.maven.org/maven2/io/netty/netty-transport-native-epoll/4.1.33.Final/netty-transport-native-epoll-4.1.33.Final.jar --output io.netty-transport-native-epoll-4.1.33.Final.jar
   cp io.netty-transport-native-epoll-4.1.33.Final.jar io.netty_netty-transport-native-epoll-4.1.33.Final.jar

2. Load Python zip file from PYRASTERFRAMES:
   cd /opt/spark/bin
   curl https://repo1.maven.org/maven2/org/locationtech/rasterframes/pyrasterframes_2.11/0.9.0/pyrasterframes_2.11-0.9.0-python.zip --output pyrasterframes_2.11-0.9.0-python.zip

3. To start Spark pyrasterframes shell execute in directory with Python zip file (/opt/spark/bin):
   pyspark --master local[*] --py-files pyrasterframes_2.11-0.9.0-python.zip --packages org.locationtech.rasterframes:rasterframes_2.11:0.9.0,org.locationtech.rasterframes:pyrasterframes_2.11:0.9.0,org.locationtech.rasterframes:rasterframes-datasource_2.11:0.9.0 --conf spark.serializer=org.apache.spark.serializer.KryoSerializer --conf spark.kryo.registrator=org.locationtech.rasterframes.util.RFKryoRegistrator --conf spark.kryoserializer.buffer.max=500m

IMPORTANT: Each start of the spark master console, following script needs to run to start hive:
/opt/apache-hive-3.1.2-bin/bin/hive &&
. ~/.bashrc

TO TEST:
import pyrasterframes
spark = spark.withRasterFrames()
df = spark.read.raster('https://landsat-pds.s3.amazonaws.com/c1/L8/158/072/LC08_L1TP_158072_20180515_20180604_01_T1/LC08_L1TP_158072_20180515_20180604_01_T1_B5.TIF')
print(df.head())

python folder:
convert jp2 to tiff file in order to read ata in pyrasterframes. - this could be done through some AWS catalogs and so on...
