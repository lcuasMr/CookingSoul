# CookingSoul

CookingSoul es una aplicación web para compartir, descubrir y gestionar recetas de cocina. Permite a los usuarios registrarse, iniciar sesión, publicar recetas, ver recetas de otros usuarios, gestionar ingredientes y mucho más.

## Características

- Registro e inicio de sesión de usuarios (con roles, por ejemplo, admin).
- Publicación y visualización de recetas con ingredientes y pasos.
- Gestión de ingredientes.
- Visualización de usuarios y sus posts.
- Interfaz moderna y responsiva gracias a Bootstrap.
- Sistema de likes para posts de recetas.
- Panel de administración para gestionar usuarios e ingredientes.

## Tecnologías utilizadas

- **Backend:** Python, Flask, SQLAlchemy, Flask-Login, Flask-Bcrypt
- **Frontend:** Bootstrap 5, Jinja2
- **Base de datos:** SQLite (por defecto, fácilmente adaptable a otros motores)

## Instalación y despliegue local

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tuusuario/CookingSoul.git
   cd CookingSoul
   ```

2. **Crea y activa un entorno virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura las variables de entorno (opcional):**
   - Puedes modificar la clave secreta y la cadena de conexión a la base de datos en `app.py`.

5. **Inicializa la base de datos:**
   - La base de datos se crea automáticamente al ejecutar la app si no existe.

6. **Ejecuta la aplicación:**
   ```bash
   python app.py
   ```
   Accede a [http://127.0.0.1:5000](http://127.0.0.1:5000) en tu navegador.

## Usuarios de ejemplo

- **admin** / contraseña: la contraseña está hasheada, puedes cambiarla en el código de inicialización si lo deseas.
- **lucas** / contraseña: igual que arriba.

## Estructura del proyecto

```
CookingSoul/
│
├── app.py
├── Facade.py
├── requirements.txt
├── models/
├── entities/
├── daos/
├── mappers/
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── recetas.html
│   ├── receta.html
│   ├── user.html
│   ├── usuarios.html
│   └── ...
├── static/
│   └── logo.png
├── utils/
│   ├── forms.py
│   ├── ingredients.py
│   └── recipiesexample.py
└── README.md
```

## Despliegue en producción

1. **Configura un servidor WSGI** como Gunicorn o uWSGI.
2. **Configura un servidor web** (Nginx, Apache) para servir archivos estáticos y hacer proxy al backend.
3. **Configura variables de entorno seguras** (SECRET_KEY, base de datos, etc).
4. **(Opcional) Usa una base de datos más robusta** como PostgreSQL o MySQL.
5. **Desactiva el modo debug** en producción.

## Notas adicionales

- Puedes modificar los ingredientes y recetas de ejemplo en ingredients.py y recipiesexample.py.
- El sistema de roles es básico, pero puedes ampliarlo fácilmente.
- El sistema de likes y comentarios puede ser extendido según tus necesidades.


---

**¡Disfruta cocinando y compartiendo con CookingSoul!**
