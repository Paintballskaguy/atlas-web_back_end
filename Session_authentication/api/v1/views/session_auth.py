#!/usr/bin/env python3
""" Session Authentication Views """
from flask import jsonify, request, make_response
from models.user import User
import os


def handle_login():
    """ Handles session authentication login """
    # Get form data
    email = request.form.get('email')
    password = request.form.get('password')

    # Validate email
    if not email or not email.strip():
        return jsonify({"error": "email missing"}), 400

    # Validate password
    if not password or not password.strip():
        return jsonify({"error": "password missing"}), 400

    # Search for user by email
    try:
        users = User.search({'email': email})
    except Exception as e:
        # Log the error for debugging
        print(f"Search error: {str(e)}")
        return jsonify({"error": "database error"}), 500

    # Check if we found any users
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    # Get first user
    user = users[0]

    # Verify password - must return 401 for wrong password
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Import auth inside function to avoid circular imports
    from api.v1.app import auth

    # Create session
    session_id = auth.create_session(user.id)
    if not session_id:
        return jsonify({"error": "failed to create session"}), 500

    # Create response with user info
    response = make_response(user.to_json())

    # Set session cookie
    session_name = os.getenv('SESSION_NAME', '_my_session_id')
    response.set_cookie(session_name, session_id, path='/')

    return response


def handle_logout():
    """Handles session authentication logout"""
    # Import auth inside function to avoid circular imports
    from api.v1.app import auth

    # Destroy the session
    destroyed = auth.destroy_session(request)
    if not destroyed:
        abort(404)

    # Return empty JSON response
    return jsonify({}), 200
