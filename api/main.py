import flask
import json
from http import HTTPStatus
import api.ppd_complaints as ppd_complaints


app = flask.Flask(__name__)

class Health_Check():
    """Health Check class stub
    """
    @classmethod
    def set_health(self):
        return True

@app.route('/ping', methods=['GET'])
def ping():
    """ ping endpoint on API takes GET requests and returns API Health Status
    """
    health = Health_Check.set_health()
    if health:
        return flask.Response(response="health check successful", status=HTTPStatus.OK, mimetype="application/json", content_type="application/json")
    return flask.Response(response="Error - health check failed", status=HTTPStatus.INTERNAL_SERVER_ERROR)

@app.route('/all_complaints', methods=['POST'])
def all_complaints():
    """ ppd_complaints endpoint retrieves all ppd complaint data from the database
    """
    #request = flask.request.get_json(force=True)
    try:
        result = ppd_complaints.get_all_complaints()
        response = json.dumps(json.loads(result))
    except Exception as e:
        return flask.Response(response="Error - "+ str(e), status=HTTPStatus.INTERNAL_SERVER_ERROR)
    return flask.Response(response=response, status=HTTPStatus.OK, mimetype="application/json", content_type="application/json")


if __name__ == '__main__':
    app.run()