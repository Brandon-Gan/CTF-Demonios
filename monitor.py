import os
import signal
import subprocess
import time


LOG_FILE = "monitor.log"
APP_FILE = "app.py"

ejecutando = True
proceso_app = None


def registrar(mensaje):
    fecha = time.strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as archivo:
        archivo.write(f"[{fecha}] {mensaje}\n")

    print(f"[{fecha}] {mensaje}")


def detener_monitor(signum, frame):
    global ejecutando

    registrar("Se recibió una señal. Deteniendo monitor.")
    ejecutando = False

    if proceso_app and proceso_app.poll() is None:
        registrar("Deteniendo aplicación principal.")
        proceso_app.terminate()


def iniciar_aplicacion():
    global proceso_app

    proceso_app = subprocess.Popen(
        ["python3", APP_FILE]
    )

    registrar(
        f"Aplicación iniciada. PID: {proceso_app.pid}"
    )


signal.signal(signal.SIGTERM, detener_monitor)
signal.signal(signal.SIGINT, detener_monitor)


registrar("=== MONITOR INICIADO ===")
registrar(f"PID del monitor: {os.getpid()}")

iniciar_aplicacion()


while ejecutando:

    time.sleep(3)

    if proceso_app.poll() is not None:

        codigo = proceso_app.returncode

        registrar(
            f"La aplicación terminó inesperadamente. Código: {codigo}"
        )

        if ejecutando:
            registrar("Reiniciando aplicación...")
            iniciar_aplicacion()


registrar("Monitor detenido.")
