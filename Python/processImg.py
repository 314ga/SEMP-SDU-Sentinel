# import required libraries
from matplotlib import pyplot as plt
import rasterio
from datetime import datetime
import numpy as np

# current date and time
print("Loading image............................")
now = datetime.now()
timestamp = datetime.timestamp(now)
print(datetime.fromtimestamp(timestamp))
# import bands as separate 1 band raster
imagePath = './data/'
band2 = rasterio.open(
    imagePath+'S2A_MSIL2A_20180803T103021_N0208_R108_T32UNG_20180803T151712SAFE/R10m/T32UNG_20180803T103021_B02_10m.jp2', driver='JP2OpenJPEG')  # blue
band3 = rasterio.open(
    imagePath+'S2A_MSIL2A_20180803T103021_N0208_R108_T32UNG_20180803T151712SAFE/R10m/T32UNG_20180803T103021_B03_10m.jp2', driver='JP2OpenJPEG')  # green
band4 = rasterio.open(
    imagePath+'S2A_MSIL2A_20180803T103021_N0208_R108_T32UNG_20180803T151712SAFE/R10m/T32UNG_20180803T103021_B04_10m.jp2', driver='JP2OpenJPEG')  # red
band8 = rasterio.open(
    imagePath+'S2A_MSIL2A_20180803T103021_N0208_R108_T32UNG_20180803T151712SAFE/R10m/T32UNG_20180803T103021_B08_10m.jp2', driver='JP2OpenJPEG')  # nir
band22 = rasterio.open(
    imagePath+'S2B_MSIL1C_20210616T103629_N0300_R008_T32UNG_20210616T131204SAFE/T32UNG_20210616T103629_B02.jp2', driver='JP2OpenJPEG')  # blue
band33 = rasterio.open(
    imagePath+'S2B_MSIL1C_20210616T103629_N0300_R008_T32UNG_20210616T131204SAFE/T32UNG_20210616T103629_B03.jp2', driver='JP2OpenJPEG')  # green
band44 = rasterio.open(
    imagePath+'S2B_MSIL1C_20210616T103629_N0300_R008_T32UNG_20210616T131204SAFE/T32UNG_20210616T103629_B04.jp2', driver='JP2OpenJPEG')  # red
band88 = rasterio.open(
    imagePath+'S2B_MSIL1C_20210616T103629_N0300_R008_T32UNG_20210616T131204SAFE/T32UNG_20210616T103629_B08.jp2', driver='JP2OpenJPEG')  # nir

print("count")
# number of raster bands
print(band4.count)
print("width")
# number of raster columns
print(band4.width)
print("height")
# number of raster rows
print(band4.height)
print("bounds")
print(band4.bounds)
print("transform")
print(band4.transform)
print("crs")
print(band4.crs)
# plot band
print("ReadingBand............................")
now = datetime.now()
timestamp = datetime.timestamp(now)
print(datetime.fromtimestamp(timestamp))
bandNir = band8.read(1)
bandRed = band4.read(1)
bandNirNow = band88.read(1)
bandRedNow = band44.read(1)
print("Finish reading bands.........................")
now = datetime.now()
timestamp = datetime.timestamp(now)
print(datetime.fromtimestamp(timestamp))
print("Creating numpy array........................")
now = datetime.now()
timestamp = datetime.timestamp(now)
print(datetime.fromtimestamp(timestamp))

ndvi2018Red = np.zeros(bandRed.shape, dtype=rasterio.float32)
#ndvi2018Nir = np.zeros(bandRed.shape, dtype=rasterio.float32)
ndvi2018Red = bandRed.astype(float)
#ndvi2018Nir = bandNir.astype(float)

#ndvi2021Red = np.zeros(bandRedNow.shape, dtype=rasterio.float32)
#ndviNow = (bandNirNow.astype(float)-bandRedNow.astype(float))/(bandNirNow+bandRedNow)
#ndvi2021Nir = np.zeros(bandRedNow.shape, dtype=rasterio.float32)
#ndvi2021Red = bandRedNow.astype(float)
#ndvi2021Nir = bandNirNow.astype(float)


print("Finish.........................")
now = datetime.now()
timestamp = datetime.timestamp(now)
print(datetime.fromtimestamp(timestamp))

profile = band4.profile
profile.update(
    dtype=rasterio.float32,
    count=1,
    compress='lzw',
    driver='GTiff')

print("Creating image...............................")
now = datetime.now()
timestamp = datetime.timestamp(now)
print(datetime.fromtimestamp(timestamp))

# with rasterio.open('./ndvi2018Red.tiff', 'w', **profile) as dst:
#   dst.write_band(1, ndvi2018Red.astype(rasterio.float32))

# export true color image
trueColor = rasterio.open('./ndvi2018Red.tiff', 'w', driver='Gtiff',
                          width=band4.width, height=band4.height,
                          count=3,
                          crs=band4.crs,
                          transform=band4.transform,
                          dtype=band4.dtypes[0]
                          )
trueColor.write(band4.read(1), 1)  # blue
trueColor.close()

trueColor = rasterio.open('./ndvi2018NIR.tiff', 'w', driver='Gtiff',
                          width=band4.width, height=band4.height,
                          count=3,
                          crs=band4.crs,
                          transform=band4.transform,
                          dtype=band4.dtypes[0]
                          )
trueColor.write(band8.read(1), 1)  # blue
trueColor.close()

trueColor = rasterio.open('./ndvi2021Red.tiff', 'w', driver='Gtiff',
                          width=band4.width, height=band4.height,
                          count=3,
                          crs=band4.crs,
                          transform=band4.transform,
                          dtype=band4.dtypes[0]
                          )
trueColor.write(band44.read(1), 1)  # blue
trueColor.close()

trueColor = rasterio.open('./ndvi2021NIR.tiff', 'w', driver='Gtiff',
                          width=band4.width, height=band4.height,
                          count=3,
                          crs=band4.crs,
                          transform=band4.transform,
                          dtype=band4.dtypes[0]
                          )
trueColor.write(band88.read(1), 1)  # blue
trueColor.close()

# out_ndvi.set_cmap('nipy_spectral')
