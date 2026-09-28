# 🛡️ Tolerancia a Fallas en Python

## 📌 Descripción

Este proyecto implementa una aplicación tolerante a fallas utilizando **Python y procesos en segundo plano**.

El sistema está compuesto por dos procesos:

* **Aplicación principal:** realiza una tarea continuamente.
* **Monitor:** supervisa el estado de la aplicación y la reinicia automáticamente si termina inesperadamente.

El proyecto fue desarrollado y probado en un entorno **Linux (Ubuntu)**.

---

## 🎯 Problema a resolver

Una aplicación que funciona continuamente puede detenerse inesperadamente debido a diferentes fallas.

Para solucionar este problema, se implementa un proceso monitor que revisa constantemente si la aplicación principal continúa funcionando.

Si detecta que la aplicación terminó, el monitor la inicia nuevamente de forma automática.

---

## 🧰 Herramientas utilizadas

* Python 3
* `subprocess`
* `signal`
* `os`
* `time`
* Procesos en Linux
* Archivo de registro (`monitor.log`)

### Funciones principales

* `subprocess.Popen()` → inicia la aplicación como un proceso independiente.
* `poll()` → permite comprobar si el proceso continúa ejecutándose.
* `signal` → permite manejar señales del sistema.
* `os.getpid()` → obtiene el identificador PID de cada proceso.
* `time.sleep()` → establece intervalos entre las comprobaciones.
* `monitor.log` → almacena los eventos del monitor.

---

## ⚙️ Funcionamiento

El sistema funciona de la siguiente manera:

1. Se inicia el **monitor**.
2. El monitor inicia la **aplicación principal**.
3. La aplicación comienza a ejecutar ciclos continuamente.
4. El monitor revisa cada cierto tiempo si la aplicación sigue activa.
5. Si la aplicación termina inesperadamente:

   * El monitor detecta que el proceso terminó.
   * Registra el evento en `monitor.log`.
   * Inicia nuevamente la aplicación.
6. La aplicación vuelve a ejecutarse automáticamente.

### 🔄 Estrategia de tolerancia a fallas

La estrategia utilizada es la **detección y reinicio automático del proceso**.

De esta manera, si el proceso principal deja de funcionar, el monitor permite que la aplicación vuelva a ejecutarse sin necesidad de iniciarla manualmente.

---

## 🧪 Prueba realizada

Para comprobar el funcionamiento, se inició el monitor y posteriormente se terminó manualmente el proceso de la aplicación utilizando su PID:

```bash
kill PID
```

El monitor detectó la finalización y mostró mensajes similares a:

```text
La aplicación terminó inesperadamente. Código: 0
Reiniciando aplicación...
Aplicación iniciada. PID: 3676
```

Después de esto, la aplicación volvió a mostrar sus ciclos de funcionamiento.

Esto demuestra que el mecanismo de recuperación funciona correctamente.

---

## ▶️ Ejecución

Primero se debe entrar a la carpeta del proyecto:

```bash
cd tolerante_fallas
```

Después se ejecuta el monitor:

```bash
python3 monitor.py
```

El monitor se encargará de iniciar automáticamente la aplicación principal.

---

## 📁 Archivos

```text
tolerante_fallas/
│
├── app.py
├── monitor.py
```

### `app.py`

Contiene la aplicación principal y maneja las señales del sistema para poder cerrarse correctamente.

### `monitor.py`

Contiene el proceso monitor encargado de supervisar y reiniciar la aplicación.

### `monitor.log`

Archivo generado automáticamente donde se registran los eventos del monitor. No es necesario subirlo al repositorio.
