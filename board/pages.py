from flask import Blueprint, render_template, jsonify, request
from board.database import get_db
import sqlite3

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")