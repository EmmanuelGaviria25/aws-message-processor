import asyncio
import aiohttp
import logging

logger = logging.getLogger(__name__)

async def download_file(session, url, retries=3):
    """
    Descarga un archivo desde una URL con reintentos.
    """
    for attempt in range(retries):
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    logger.info(f"Descargado correctamente: {url}")
                    return await response.text()  # Guarda el contenido si es necesario
                else:
                    logger.warning(f"Error descargando {url}, estado: {response.status}")
        except Exception as e:
            logger.error(f"Error descargando {url}, intento {attempt + 1}: {e}")
        await asyncio.sleep(1)  # Espera antes de reintentar

    logger.error(f"No se pudo descargar {url} después de {retries} intentos.")
    return None

async def download_urls_concurrently(urls):
    """
    Descarga múltiples URLs en paralelo.
    """
    async with aiohttp.ClientSession() as session:
        tasks = [download_file(session, url) for url in urls]
        return await asyncio.gather(*tasks)

def download_urls():
    """
    Punto de entrada para manejar descargas concurrentes.
    """
    urls = [f"http://example.com/file{i}" for i in range(1, 11)]  # Lista de ejemplo
    logger.info(f"Iniciando descargas para {len(urls)} URLs...")
    results = asyncio.run(download_urls_concurrently(urls))
    logger.info(f"Descargas completadas: {len([r for r in results if r is not None])} exitosas.")
