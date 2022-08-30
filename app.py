
from flask import Flask
from flask import request
from flask_restx import Resource, Api, fields
from tasks import count, add_celery, Celery_app
from celery.result import AsyncResult

app = Flask(__name__)

api = Api(app, version='0.0.3',
          title='Flask-RESTX combine celery tasks', default_label="below", default="Function")


account_output_data = api.model('輸出', {

    'status': fields.Integer(required=True, default=1),
    'message': fields.String(required=True, default='error'),
    'task_id': fields.String(required=True, default='task_id'),
})

input_payload = api.model('輸入', {

    'recipient': fields.String(required=True, default='allen@gmail.com'),
    'title': fields.String(required=True, default='Celery combine test'),
    'content': fields.String(required=True, default='HIHI'),
    'x': fields.Integer(requrid=True, default=0),
})


@api.route('/register')
class Register(Resource):
    @api.expect(input_payload)
    @api.marshal_with(account_output_data)
    def post(self):
        data = api.payload
        print(data)
        try:
            data = str(
                {'recipient': data['recipient'], 'title': data['title'], 'content': data["content"]})
        except Exception:
            message = {'status': 1, 'message': 'error'}
        else:
            message = {'status': 0, 'message': 'success'}
        finally:
            return message


@api.route('/get')
@api.doc(params={'id': 'input'})
class get(Resource):
    @api.marshal_with(account_output_data)
    def get(self):
        print(request.args.get('id'))
        task = count.delay(3)
        return {'task_id': task.id}


@api.route('/add')
class add(Resource):
    @api.doc(params={'x': 'x_value'})
    @api.marshal_with(account_output_data)
    def get(self):
        # x = request.values.get('x')
        task = add_celery.delay(0, 10)
        return {'status': 0, 'message': 'success', 'task_id': task.id}


@api.route('/result')
class result(Resource):
    @api.doc(params={'task_id': 'input'})
    @api.marshal_with(account_output_data)
    def get(self):
        getTask = request.values.get('task_id')
        Smitlea = AsyncResult(getTask, app=Celery_app)
        return (Smitlea.result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
