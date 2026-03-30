from flask import Flask, render_template, current_app
from flask_wtf import CSRFProtect
from flask_wtf.csrf import CSRFError


def register_error_handlers(app):
    if not app.config.get("USE_CUSTOM_ERROR_PAGES", False):
        return  # do nothing if toggle is False

    @app.errorhandler(400)
    def bad_request(e):
        return render_template("pages/errors/400.html", reason=str(e)), 400

    @app.errorhandler(403)
    def forbidden(e):
        return render_template("pages/errors/403.html", reason=str(e)), 403

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("pages/errors/404.html", reason=str(e)), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template("pages/errors/500.html", reason=str(e)), 500

    # Optional: CSRF errors specifically
    @app.errorhandler(CSRFError)
    def handle_csrf_error(e):
        return render_template("pages/errors/400.html", reason=e.description), 400
