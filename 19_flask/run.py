from app import create_app
from app.config.config import DevelopmentConfig


app = create_app()

if __name__ == "__main__":
    host = app.config.get("FLASK_RUN_HOST", "127.0.0.1")
    port = app.config.get("FLASK_RUN_PORT", 5000)
    debug = app.config.get("DEBUG", False)
    # app.run(debug=True)
    app.run(host=host, port=port, debug=debug)
