from dateutil.relativedelta import relativedelta
from flask import Flask
import datetime


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# predefined times
age_time = datetime.datetime(2000, 3, 23)
work_time = datetime.datetime(2021, 10, 1)
linux_time = datetime.datetime(2014, 1, 1) # somewhere in 2014
python_time = datetime.datetime(2017, 3, 1) # somewhere in march 2017


def beautify_time(date1, date2, *, approx=None):
    builder = []

    if date1 < date2:
        return 'waiting...'

    relative = relativedelta(date1, date2)
    attrs = approx or ['years', 'months', 'days']
    for attr in attrs:
        r = getattr(relative, attr)
        if r:
            builder.append(f'{r} {attr}')

    return ', '.join(builder) + ' ago'


@app.route('/whoami')
def root():
    now = datetime.datetime.utcnow()
    age = relativedelta(now, age_time)

    return {
        'whoami': {
            'name': 'Eduard Grosu',
            'age': age.years,
            'country': 'Romania'
        },
        'education': [
            {
                'name': 'Victor Babeş National College',
                'field': 'Natural Sciences',
                'when': '2015-2019',
                'degree': 'Baccalaureate Degree'
            },
            {
                'name': 'Spiru Haret University',
                'field': 'Computer Science',
                'when': '2020-2023',
                'degree': 'Bachelor\'s Degree'
            }
        ],
        'hobbies': [
            {
                'hobby': 'Python Developer',
                'since': beautify_time(now, python_time, approx=['years'])
            },
            {
                'hobby': 'Linux Enthusiast',
                'since': beautify_time(now, linux_time, approx=['years'])
            }
        ],
        'work': {
            'as': 'DevOps Engineer',
            'for': 'Wipro Technology Solutions SRL',
            'since': f'{work_time.strftime("%B %Y")} ({beautify_time(now, work_time)})'
        }
    }


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
