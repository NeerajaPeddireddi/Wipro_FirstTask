from flask import Flask

from CaseStudy_4.routes.admin_routes import admin_bp
from CaseStudy_4.routes.dish_routes import dish_bp
from CaseStudy_4.routes.order_routes import order_bp
from CaseStudy_4.routes.restaurant_routes import restaurant_bp
from CaseStudy_4.routes.user_routes import user_bp

app = Flask(__name__)

app.register_blueprint(restaurant_bp)
app.register_blueprint(dish_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(user_bp)
app.register_blueprint(order_bp)
@app.route("/",methods=['GET'])
def home():
    return "Welcome to Foodie App REST API"

if __name__ == "__main__":
    app.run(debug=True)
