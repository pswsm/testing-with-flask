from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    navitems: list[dict[str:str]] = [
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

    passatemps: list[str] = ['aprendre programació', 'aprendre idiomes', 'jugar a videojocs', 'fotografía']
    estudis: list[str] = ['CFGM Sistemes Microinformàtics i Xarxes', '(Actual) CFGS Desenvolupament Web - Perfil Bioinformàtica']
    programacio: list[str] = ['Python', 'C++', 'Shell', 'JavaScript']
    languages: list[str] = ['catala nadiu', 'castella nadiu', 'angles B2', 'japones A2']
    abtme: list[str]= {'passatemps': passatemps, 'estudis': estudis, 'programacio': programacio, 'idiomes': languages}

    return render_template('index.html', navitems=navitems, abtme=abtme)


@app.route('/japones')
def japones():
    return "Aquí aniran les practiques de japonès"


@app.route('/mplayer')
def mplayer():
    return "Aquí anirà el reproductor d'àudio"
