import os
import signal
import time


ejecutando = True


def detener_aplicacion(signum, frame):
    global ejecutando

    print("\nAplicación: señal recibida.")
    print("Aplicación: cerrando correctamente...")

    ejecutando = False


signal.signal(signal.SIGTERM, detener_aplicacion)
signal.signal(signal.SIGINT, detener_aplicacion)


print("=== APLICACIÓN PRINCIPAL ===")
print("PID de la aplicación:", os.getpid())
print("Aplicación iniciada correctamente.")
print()

contador = 1

while ejecutando:
    print("Aplicación funcionando... ciclo", contador)
    contador += 1

    time.sleep(5)


print("Aplicación detenida.")
