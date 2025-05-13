# Reconocimiento Facial

Una aplicación web minimalista para reconocimiento facial desarrollada con Django.

## 📋 Descripción

Este proyecto permite:

* Mostrar información del proyecto (README renderizado en la página).
* Registro e inicio de sesión de usuarios.
* Interfaz muy simple, limpia y responsive.

## 🚀 Características

* **Autenticación**: Registro e inicio de sesión con `django.contrib.auth`.
* **Markdown**: Carga y renderizado de `README.md` en HTML.
* **Responsive**: Adaptación a dispositivos móviles con CSS simple.

## 🛠 Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/proyecto-reconocimiento-facial.git
   cd proyecto-reconocimiento-facial
   ```
2. Crea y activa un entorno virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Instala dependencias:

   ```bash
   pip install -r requirements.txt
   ```
4. Aplica migraciones:

   ```bash
   python manage.py migrate
   ```
5. Ejecuta el servidor:

   ```bash
   python manage.py runserver
   ```

## ⚙️ Uso

* Abre tu navegador en `http://localhost:8000/`.
* Si no tienes cuenta, haz clic en **Registrarse**.
* Una vez autenticado, verás el contenido del README renderizado.

## 📂 Estructura de carpetas

```plain
proyecto-reconocimiento-facial/
├── core/
│   ├── views.py
│   └── urls.py
├── templates/
│   └── home.html
├── static/
│   └── css/
│       └── style.css
├── README.md
└── manage.py
```

## 🛠 Tecnologías

* Python 3.x
* Django
* markdown2
* HTML5 & CSS3

## 📄 Licencia

Proyecto bajo licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
