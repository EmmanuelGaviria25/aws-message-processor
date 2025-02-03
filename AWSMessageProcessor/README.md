# AWS Message Processor

Este proyecto es un sistema modular que procesa mensajes desde **AWS SQS**, almacena datos en **MongoDB** y **SQL Server**, y permite descargas concurrentes desde múltiples URLs. Implementa arquitectura **serverless** con **AWS Lambda**, concurrencia con **asyncio**, y un diseño escalable basado en módulos.

## 🚀 **Características Principales**
✔ Procesamiento de mensajes en **AWS SQS**  
✔ Almacenamiento en **MongoDB** y **SQL Server**  
✔ Almacenamiento de registros en **AWS S3**  
✔ Descargas concurrentes con **asyncio** y **aiohttp**  
✔ Diseño **modular y escalable**  
✔ Soporte para **pruebas unitarias**  

## Requisitos
- Python 3.8+
- Instalar dependencias:
  ```bash
  pip install -r requirements.txt 
<br>

## 📂 **Estructura del Proyecto**
**AWSMessageProcessor**/ 

│ <br>
├── **src/** Código fuente principal <br>
│ ├── **aws/** Módulos de AWS <br>
│ │ ├── **sqs_handler.py** Manejo de AWS SQS <br>
│ │ ├── **s3_handler.py** Manejo de AWS S3 <br>
│ │ └── **lambda_entrypoint.py** Punto de entrada para AWS Lambda <br>
│ │ <br>
│ ├── **database/** Conectores de bases de datos <br>
│ │ ├── **mongodb_connector.py** Conector MongoDB <br>
│ │ └── **sql_server_connector.py** Conector SQL Server <br>
│ │ <br>
│ ├── **utils/** Herramientas auxiliares <br>
│ │ ├── **logger.py** Configuración de logs <br>
│ │ └── **file_reader.py** Lector y validador de JSON <br>
│ │ <br>
│ ├── **services/** Lógica de negocio <br>
│ │ ├── **message_processor.py** Procesador de mensajes de SQS <br>
│ │ └── **downloader_service.py** Descarga de archivos concurrentes <br>
│ │ <br>
│ ├── **config/** Configuración global <br>
│ │ ├── **settings.py** Parámetros de configuración <br>
│ │ ├── **constants.py** Definición de constantes <br>
│ │ └── **config_loader.py** Carga de configuraciones <br>
│ │ <br>
│ └── **main.py** Punto de entrada del sistema <br>
│ <br>
├── **input_data/** Carpeta para archivos JSON de entrada <br>
├── **tests/** Pruebas unitarias <br>
├── **diagrams/** Diagramas de arquitectura <br>
├── **requirements.txt** Dependencias del proyecto <br>
├── **create_messages_table.sql** Script SQL para crear tabla en SQL Server <br>
└── **README.md**

## 🛠 Uso del Proyecto

### 🔹 Procesar Mensajes desde AWS SQS
```bash
python src/main.py process_sqs
```
Este comando:  
✅ Lee mensajes desde AWS SQS  
✅ Guarda los datos en MongoDB  
✅ Almacena ciertos registros en AWS S3  
✅ Elimina el mensaje de la cola SQS  


### 🔹 Descargar Archivos Concurrentemente
```bash
python src/main.py download_urls
```
Este comando:  
✅ Descarga archivos desde múltiples URLs en paralelo  
✅ Maneja reintentos en caso de fallos  


## 🧪 Pruebas Unitarias
Para ejecutar pruebas unitarias, usa:

```bash
pytest tests/
```
Esto ejecutará los tests en `tests/`.


## 📊 Diagrama de Arquitectura
El sistema sigue una arquitectura **serverless** con AWS Lambda, SQS, S3 y bases de datos.

📍 **Flujo General:** <br>
1️⃣ **AWS SQS** recibe mensajes  
2️⃣ **Lambda** procesa los mensajes  
3️⃣ **MongoDB/SQL Server** almacena los datos  
4️⃣ **AWS S3** guarda registros específicos  

Puedes encontrar el diagrama en `diagrams/architecture.png`.

## 👨‍💻 Autor
Desarrollado por **Emmanuel Gaviria**  
📧 Contacto: emmanuel.gaviria.25@gmail.com  
🔗 LinkedIn: [linkedin.com/in/tuusuario](https://linkedin.com/in/emmanuel-gaviria-00bb16124)

