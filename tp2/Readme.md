# TP 2: Cliente JavaScript con GET y POST

Cliente HTML + JavaScript que consume una API Rest emulada con **json-server**. El GET ya venía hecho de la clase 19; el TP es completar el **POST**.

## Estructura

```
/
├── db.json      # datos de la API (json-server)
└── index.html   # cliente con los botones GET y POST
```

## Cómo correrlo

1. Instalar json-server (una sola vez):

   ```
   npm install -g json-server
   ```

2. Levantar la API desde esta carpeta:

   ```
   json-server --watch db.json
   ```

   Queda en `http://localhost:3000/personas`.

3. Abrir `index.html` con la extensión **Live Server** de VSCode.

## Cómo usarlo

* **GET:** con la URL `http://localhost:3000/personas` trae todas las personas. Con `http://localhost:3000/personas/1` trae solo la persona con id 1.
* **POST:** con la URL `http://localhost:3000/personas`, escribir en el cuadro Body el JSON de la persona nueva y apretar POST:

  ```json
  { "nombre": "Guido" }
  ```

  json-server le asigna el `id` solo, devuelve la persona creada y la guarda en `db.json`.

## Cómo funciona el POST

`postByUrl()` toma la URL y el body, valida que el body sea un JSON válido y hace un `fetch` con `method: 'POST'` y el header `Content-Type: application/json`. Usa `await`, igual que el GET, y muestra la respuesta en el cuadro Resultado.
