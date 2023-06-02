from src import create_app
# from flask_cors import CORS
from src.entities.entity import engine, Base
from src import cors

# if __name__ == '__main__':
# 	app = create_app()
app = create_app()
Base.metadata.create_all(engine)
# CORS(app)
# cors.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)