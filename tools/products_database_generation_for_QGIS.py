# BLOCK 1 - https://gis.stackexchange.com/questions/233279/
# clipping-a-raster-using-an-irregular-polygon-with-python
import processing
from qgis.core import *
# END BLOCK 1

# https://realpython.com/python-sleep/
import time

NATURAL_EARTH_RASTER = 'path_to_TIF_file/TIF_file.TIF'
fi = QFileInfo(NATURAL_EARTH_RASTER)
fname_r = fi.baseName()

NATURAL_EARTH_VECTOR = \
    'path_to_shape_with_country_borders/country_borders_file_name.shp'
fi2 = QFileInfo(NATURAL_EARTH_VECTOR)
fname_v = 'country_borders'

r_layer = iface.addRasterLayer(NATURAL_EARTH_RASTER, fname_r)
vec_layer = iface.addVectorLayer(NATURAL_EARTH_VECTOR, fname_v, "ogr")

features = vec_layer.getFeatures()

countries = []

# https://gis.stackexchange.com/questions/167831/
# print-values-from-tables-in-qgis-console
for ft in features:
    attrs = ft.attributes()
    countries.append(attrs[3])


# https://gis.stackexchange.com/questions/233279/clipping-a-raster-using-an-irregular-polygon-with-python
raster_layer = QgsRasterLayer(NATURAL_EARTH_RASTER, 'raster')

for i in range(0, len(countries)):

    print (countries[i])

    # https://opensourceoptions.com/blog/
    # pyqgis-select-features-from-a-vector-layer/
    field_name = '"NAME" = '
    country_to_filter = "'" + countries[i] + "'"
    selected_country = vec_layer.selectByExpression(
        field_name + country_to_filter
    )
    selected_country = vec_layer.selectedFeatures()

    # https://gis.stackexchange.com/questions/80292/
    # creating-vector-layer-from-selected-features-with-pyqgis
    layer = iface.activeLayer()

    # https://gis.stackexchange.com/questions/
    # 80292/creating-vector-layer-from-selected-features-with-pyqgis
    current_layer = layer.materialize(
        QgsFeatureRequest().setFilterFids(layer.selectedFeatureIds())
    )

    # https://gis.stackexchange.com/questions/
    # 311919/saving-layer-as-shapefile-using-pyqgis
    QgsVectorFileWriter.writeAsVectorFormat(
        current_layer, 'path_to_saving_directory/' +
        countries[i], 'utf-8', driverName='ESRI Shapefile'
    )

    # ACTIVATE IF YOU WANT TO LOAD FILTERED/SELECTED VECTOR LAYERS
    # IN CURRENT QGIS PROJECT, BE AWARE OF MEMORY REQUIREMENTS
    # https://gis.stackexchange.com/questions/
    # 290938/adding-layer-to-group-in-layers-panel-using-pyqgis
    groupName = "Countries"
    root = QgsProject.instance().layerTreeRoot()
    group = root.addGroup(groupName)
    vlayer = current_layer

    QgsProject.instance().addMapLayer(vlayer)
    root = QgsProject.instance().layerTreeRoot()
    layer = root.findLayer(vlayer.id())
    clone = layer.clone()
    group.insertChildNode(0, clone)
    root.removeChildNode(layer)

    # https://gis.stackexchange.com/questions/233279/
    # clipping-a-raster-using-an-irregular-polygon-with-python

    mask_filepath = 'path_to_saving_directory/' + countries[i] + '.shp'

    mask_layer = QgsVectorLayer(mask_filepath, 'mask', 'ogr')

    parameters = {'INPUT': raster_layer,
                  'MASK': mask_layer,
                  'NODATA': -9999,
                  'ALPHA_BAND': False,
                  'CROP_TO_CUTLINE': True,
                  'KEEP_RESOLUTION': True,
                  'OPTIONS': None,
                  'DATA_TYPE': 0,
                  'OUTPUT': 'path_to_saving_directory/file_name_' +
                  countries[i] + '.png'}

    # Changed from processing.runAndLoadResults to processing.run after reading
    # https://github.com/qgis/QGIS/issues/28934
    processing.run('gdal:cliprasterbymasklayer', parameters)

    # USE processing.runAndLoadResults IF YOU WANT TO LOAD THE FILTERED RASTERS
    # processing.runAndLoadResults('gdal:cliprasterbymasklayer', parameters)
