from flask import jsonify, request, Blueprint
from CaseStudy_4.data.datastore import restaurants,orders,feedbacks
admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/api/v1/admin/restaurants/<int:rid>/approve", methods=["PUT"])
def approve_restaurant(rid):
    for restaurent in restaurants:
        if restaurent["id"] == rid:
            restaurent["approved"] = True
            return jsonify({"message": "Restaurant approved"})
    return jsonify({"error": "Restaurant not approved"}),404

@admin_bp.route("/api/v1/admin/restaurants/<int:rid>/disable", methods=["PUT"])
def admin_disable_restaurant(rid):
    for restaurant in restaurants:
        if restaurant["id"] == rid:
            restaurant["enabled"] = False
            return jsonify({"message": "Restaurant disabled"}),200
    return jsonify({"error": "Restaurant not enabled"}),404

@admin_bp.route("/api/v1/admin/orders", methods=["GET"])
def get_orders():
    return jsonify({"orders": orders}),200

@admin_bp.route("/api/v1/admin/feedback", methods=["GET"])
def get_feedback():
    return jsonify({"feedbacks": feedbacks}),200