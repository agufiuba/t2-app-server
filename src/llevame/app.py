from app_builder import build_app

# Construcción de una aplicación con la configuración por default
# salvo variables de entorno (como MONGO_URI)
app = build_app()

if __name__ == "__main__":
    app.run()
