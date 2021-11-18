from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    navitems = [
            {
                'ref': '/japones',
                'name': 'Japones'
            },
            {
                'ref': '/mplayer',
                'name': 'reproductor'
            },
            {
                'ref': '/nextcloud',
                'name': 'Nextcloud'
            }
        ]
    abtme = [
            {
                'name': 'Idiomes',
                'subthing': [
                    {'name': 'Català'},
                    {'name': 'Castellà'},
                    {'name': 'Anglès'},
                    {'name': 'Japonès'}
                    ]
            },
            {
                'name': 'Passatemps',
                'subthing': [
                    {'name': 'Aprendre programació'},
                    {'name': 'Aprendre idiomes'}
                    ]
            }
            ]
    return render_template('index.html', navitems=navitems, abtme=abtme)


@app.route('/japones')
def japones():
    return "Aquí aniran les practiques de japonès"


@app.route('/mplayer')
def mplayer():
    return "Aquí anirà el reproductor d'àudio"
