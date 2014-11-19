HistoricalSensitivity plugin for QGIS
=====================================
Author: [Benedikt Budig](http://www1.informatik.uni-wuerzburg.de/en/staff/budig_benedikt/) / Universität Würzburg

This plugin for [QGIS](http://www.qgis.org/) takes a layer with assignments and 
their corresponding sensitivity values and presents them in ascending order to 
the user.

Installation
------------
Assuming you have the latest python-enabled QGIS version installed, place the 
`HistoricalSensitivity` folder in the following directory:

```
.qgis2/python/plugins/
```

In QGIS, go to `Plugins` -> `Manage and Install Plugins` -> `Installed` and 
activate the `HistoricalSensitivity` plugin.

Usage and Tests
---------------
This plugin presents sensitive assignments in historical maps to the user. 
You need to load a layer containing this data in QGIS. With this layer being 
selected, run the plugin. It presents every assignment in ascending order of 
sensitivity by selecting it and panning the map accordingly.

As of now, the code to create such layers is not yet ready to be released. 
However, all layers containing geometries and a (sensitivity) value as its first 
attribute can be presented using this plugin.

In the `Tests` folder, two examples for historical map data with assignment 
sensitivities are provided.

<!--
Acknowledgements
----------------
Thanks to the [University Library Würzburg](http://www.bibliothek.uni-wuerzburg.de/) for 
providing the beautiful historical maps for testing!
-->
