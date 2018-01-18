# bulkr

Un montón de scripts para ayudarte a bajar varias fotos de Flickr a la vez.

## Requisitos

Los scripts están pensados para Python 3. Se hace uso de la librería `requests`.

También necesitas una API key de Flickr. [Se consiguen aquí](https://www.flickr.com/services/api/keys/). Cuando la tengas, renombra el archivo `.env.example` a `.env` y agrégala en la clave `FLICKR_APIKEY`, sin comillas ni espacios.

## Uso

Personalmente uso los scripts en python para obtener un listado de urls hacia las imágenes directas, luego edito ese listado conviertiéndolo en un script sh que baja cada foto con `wget`. Si se te ocurre cómo hacerlo de forma directa con Python 3, te agradecería el pull request.
