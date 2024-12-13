from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Set up logging for debugging
logging.basicConfig(level=logging.DEBUG)

@app.route('/groups', methods=['POST'])
def create_group():
    """
    Creates a new CHAMA group.

    Args:
        groupName: The name of the group.
        admin: The administrator of the group.

    Returns:
        A JSON object containing the group details, including the group ID.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        logging.debug(f"Received data: {data}")  # Log the received data

        # Extract data fields
        group_name = data['groupName']
        admin_name = data['admin']['name']
        admin_email = data['admin']['email']

        # Validate the input data
        if not group_name or not admin_name or not admin_email:
            return jsonify({'error': 'Invalid input: groupName and admin fields are required'}), 400

        # Simulate creating the group in the database
        group_id = create_group_in_database(group_name, admin_name, admin_email)

        # Return the group details
        response = {
            'groupId': group_id,
            'groupName': group_name,
            'admin': {
                'name': admin_name,
                'email': admin_email
            }
        }
        logging.debug(f"Response data: {response}")  # Log the response
        return jsonify(response), 201

    except KeyError as e:
        logging.error(f"KeyError: {e}")  # Log missing key errors
        return jsonify({'error': 'Invalid input: Missing required fields'}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {e}")  # Log unexpected errors
        return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500


def create_group_in_database(group_name, admin_name, admin_email):
    """
    Simulates creating a new group in the database.

    Args:
        group_name: The name of the group.
        admin_name: The name of the administrator.
        admin_email: The email address of the administrator.

    Returns:
        A mock group ID.
    """
    # Simulated logic for database creation
    logging.info("Simulating database insertion for the group")
    return "12345"  # Return a mock group ID


if __name__ == '__main__':
    app.run(debug=True)
