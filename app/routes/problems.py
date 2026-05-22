from flask import Blueprint, jsonify
from app.services.dynatrace_service import get_problems, get_problem_by_id
from app.models.problem_model import transform_problem

problems_bp = Blueprint("problems", __name__)

@problems_bp.route("/problems", methods=["GET"])
def problems():

    data = get_problems()

    problems = data.get("problems", [])

    transformed_problems = [
        transform_problem(problem)
        for problem in problems
    ]

    return jsonify({
        "count": len(transformed_problems),
        "problems": transformed_problems
    })
@problems_bp.route("/problems/<problem_id>", methods=["GET"])
def problem_details(problem_id):

    data = get_problem_by_id(problem_id)

    return jsonify(data)