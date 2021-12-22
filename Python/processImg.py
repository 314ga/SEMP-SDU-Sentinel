# import required libraries
import rasterio
from rasterio import plot
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
# current date and time
now = datetime.now()
timestamp = datetime.timestamp(now)
print(datetime.fromtimestamp(timestamp))
print("workingstart")
# import bands as separate 1 band raster
imagePath = './data/S2A_MSIL2A_20180803T103021_N0208_R108_T32UNG_20180803T151712SAFE/GRANULE/L2A_T32UNG_A016264_20180803T103239/IMG_DATA/R10m/'
band2 = rasterio.open(
    imagePath+'T32UNG_20180803T103021_B02_10m.jp2', driver='JP2OpenJPEG')  # blue
band3 = rasterio.open(
    imagePath+'T32UNG_20180803T103021_B03_10m.jp2', driver='JP2OpenJPEG')  # green
band4 = rasterio.open(
    imagePath+'T32UNG_20180803T103021_B04_10m.jp2', driver='JP2OpenJPEG')  # red
band8 = rasterio.open(
    imagePath+'T32UNG_20180803T103021_B08_10m.jp2', driver='JP2OpenJPEG')  # nir
# number of raster bands
print(band4.count)
# number of raster columns
print(band4.width)
# number of raster rows
print(band4.height)
print(band4.bounds)
# plot band
bandNir = band8.read(1)
bandRed = band4.read(1)
print(bandRed.shape)
ndvi = np.zeros(bandRed.shape, dtype=rasterio.float32)
ndvi = (bandNir.astype(float)-bandRed.astype(float))/(bandNir+bandRed)
for x in ndvi:
    print(x)

profile = band4.profile
profile.update(
    dtype=rasterio.float32,
    count=1,
    compress='lzw',
    driver='GTiff')

with rasterio.open('./exampleNDVI2.tiff', 'w', **profile) as dst:
    dst.write_band(1, ndvi.astype(rasterio.float32))

now = datetime.now()
timestamp = datetime.timestamp(now)
print(datetime.fromtimestamp(timestamp))
