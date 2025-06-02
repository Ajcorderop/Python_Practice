import processing
from qgis.core import QgsProject, QgsVectorLayer, QgsCoordinateReferenceSystem

output_path = 'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/output/03_ProspeccionMuni.gpkg'
layer_name = '01_BuildingComb'  # Sin .gpkg

result = processing.run("native:mergevectorlayers", {
    'LAYERS': [
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11011/A.ES.SDGC.BU.11011.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11025/A.ES.SDGC.BU.11025.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11035/A.ES.SDGC.BU.11035.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11002/A.ES.SDGC.BU.11002.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11036/A.ES.SDGC.BU.11036.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11021/A.ES.SDGC.BU.11021.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11023/A.ES.SDGC.BU.11023.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11031/A.ES.SDGC.BU.11031.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/53020/A.ES.SDGC.BU.53020.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11043/A.ES.SDGC.BU.11043.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11022/A.ES.SDGC.BU.11022.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11029/A.ES.SDGC.BU.11029.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/53026/A.ES.SDGC.BU.53026.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11014/A.ES.SDGC.BU.11014.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/18033/A.ES.SDGC.BU.18033.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11027/A.ES.SDGC.BU.11027.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11038/A.ES.SDGC.BU.11038.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11013/A.ES.SDGC.BU.11013.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11030/A.ES.SDGC.BU.11030.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/53041/A.ES.SDGC.BU.53041.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11001/A.ES.SDGC.BU.11001.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11037/A.ES.SDGC.BU.11037.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11033/A.ES.SDGC.BU.11033.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11028/A.ES.SDGC.BU.11028.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11039/A.ES.SDGC.BU.11039.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11015/A.ES.SDGC.BU.11015.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11008/A.ES.SDGC.BU.11008.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11018/A.ES.SDGC.BU.11018.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11005/A.ES.SDGC.BU.11005.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/53017/A.ES.SDGC.BU.53017.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11007/A.ES.SDGC.BU.11007.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/53003/A.ES.SDGC.BU.53003.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/53006/A.ES.SDGC.BU.53006.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11040/A.ES.SDGC.BU.11040.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/53010/A.ES.SDGC.BU.53010.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11032/A.ES.SDGC.BU.11032.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11900/A.ES.SDGC.BU.11900.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11034/A.ES.SDGC.BU.11034.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11016/A.ES.SDGC.BU.11016.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11042/A.ES.SDGC.BU.11042.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11045/A.ES.SDGC.BU.11045.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11004/A.ES.SDGC.BU.11004.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11024/A.ES.SDGC.BU.11024.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11019/A.ES.SDGC.BU.11019.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/53044/A.ES.SDGC.BU.53044.building.gml|layername=Building|geometrytype=Polygon',
        'C:/Users/acordero/Desktop/Proyecto/01_Inicio_Mayo2025/input/ED_Catastro/11009/A.ES.SDGC.BU.11009.building.gml|layername=Building|geometrytype=Polygon'
    ],
    'CRS': QgsCoordinateReferenceSystem('EPSG:25830'),
    'OUTPUT': f"{output_path}|layername={layer_name}"
})

merged_layer = QgsVectorLayer(f"{output_path}|layername={layer_name}", layer_name, "ogr")
QgsProject.instance().addMapLayer(merged_layer)

