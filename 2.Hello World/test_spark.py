import os
import sys

# 1. Forzar las rutas (Ajusta a tus carpetas en C: o donde las tengas)
#os.environ["JAVA_HOME"] = r"C:\BigData\jdk-17" 
#os.environ["SPARK_HOME"] = r"C:\BigData\spark-3.5.0-bin-hadoop3"
#os.environ["HADOOP_HOME"] = r"C:\BigData\hadoop"

# 2. MUY IMPORTANTE: Indicar a Spark qué ejecutable de Python usar
# sys.executable apunta al python del venv que tienes activo
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

import findspark
findspark.init()

from pyspark.sql import SparkSession

if __name__ == "__main__":
    try:
        # 3. Configuración de red para evitar el WinError 10038
        spark = SparkSession.builder \
            .appName("PruebaPyspark") \
            .master("local[*]") \
            .config("spark.driver.host", "127.0.0.1") \
            .config("spark.driver.bindAddress", "127.0.0.1") \
            .config("spark.python.worker.faulthandler.enabled", "true") \
            .getOrCreate()

        data = [("Andrés", 28), ("María", 35), ("Juan", 19)]
        df = spark.createDataFrame(data, ["Nombre", "Edad"])
        df.show()

        spark.stop()
        print("Proceso finalizado con éxito")

    except Exception as e:
        print(f"Error detectado: {e}")
