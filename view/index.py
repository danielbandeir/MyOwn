from databaseProject import app
from flask import render_template, request, redirect
from databaseProject.codesForDatabase.registrar import registrar
from databaseProject.codesForDatabase.login import login
from databaseProject.codesForDatabase.dashboard import dashboard
from databaseProject.codesForDatabase.logout import logout
from databaseProject.codesForDatabase.search import search
from databaseProject.codesForDatabase.profile import profile
from databaseProject.codesForDatabase.solicitacao import solicitacao
from databaseProject.codesForDatabase.grupo import grupo
from databaseProject.codesForDatabase.account import account

import os

UPLOAD_FOLDER = './static/img_perfil/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ac = account()
gp = grupo()
sl = solicitacao()
pr = profile()
sr = search()
lg = login()
ds = dashboard()
lgt = logout()
rg = registrar()

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if lg.verificaLogado():
        print('entrodsaoku')
        ds.verificaMural(lg.verificaLogado())
        return redirect('/dashboard')

    else:
        if request.method == "POST":
            email = request.form['email']
            senha = request.form['senha']
            print(email, senha)
            if lg.verificarLogin(email, senha):
                return redirect('/dashboard')
            else:
                return redirect('/login')

    return render_template('login.html')


@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    '''Pegar id usuário'''
    id_usuario = lg.verLogado()
    
    '''Pegar dados do usuário e verificar se tem mural'''
    ds.verificaMural(id_usuario)
    dados = ds.pegarDados(id_usuario)


    posts = ds.pegarPosts(id_usuario)



    grupos = gp.verGrupos()
    comments = ds.pegarComments()
    respostas = ds.pegarResp()
    pessoas = ds.pegarPessoas()


    if request.method == "POST" and 'postText' in request.form:
        '''Pegar post'''
        postText = request.form['postText']
        postImage = request.form['postImage']
        ds.registrarPost(id_usuario, postImage, postText, id_usuario)

    if request.method == "POST" and 'textComent' in request.form:
        '''Pegar comentario'''
        postComent = request.form['textComent']
        ppost = request.form['textCatch']
        pegarPost = ds.pegarIdPost(ppost)
        ds.registrarComent(postComent, pegarPost)
        
    if request.method == "POST" and 'textResp' in request.form:
        '''Pegar comentario'''
        postResp = request.form['textResp']
        comentId = request.form['textCatch2']
        pegarComment = ds.registrarResp(postResp, comentId)
    
    if request.method == 'POST' and 'idPessoa' in request.form:
        action = request.form['action']
        idGr = request.form['idPessoa']
        if action == 'Aceitar':
            sl.addPessoa(idGr)
            redirect('/dashboard')

    if request.method == "POST" and 'removerComent' in request.form:
        '''Pegar post'''
        postText = request.form['idComent']
        ds.removerComent(postText)
            
    posts = ds.mostrarPosts(id_usuario)
    

    return render_template('dashboard.html', pessoas=pessoas, dados=dados, posts=posts, grupos=grupos, comments=comments, respostas=respostas)


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():

    if request.method =='POST':
        email = request.form['email']
        nome = request.form['nome']
        senha = request.form['senha']

        file = request.files['file']

        nomeArquivo = ''

        cidade = request.form['cidade']
        aniversario = request.form['aniversario']
        genero = request.form['gender']

        if file.filename == '':
            nomeArquivo = ''
        else:
            nomeArquivo = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], nomeArquivo))
        
        rg.registrarBanco(email, nome, senha, nomeArquivo, cidade, aniversario, genero)
        return redirect('/')

    return render_template('registrar.html')

@app.route('/logout')
def logout():
    try:
        lgt.deslogar()
        return redirect('/')
    except:
        return redirect('/')


@app.route('/search', methods=['GET', 'POST'])
def search():

    busca = request.args.get('buscar')

    if busca:
        pessoas = sr.verPessoas(busca)
        grupos = sr.verGrupos(busca)

    else:
        pessoas = sr.verTudoPessoas()
        grupos = sr.verTudoGrupos()
    
    if request.method == 'POST':
        idGr = request.form['idGrupo']
        sr.addGrupo(idGr)
            

    return render_template('search.html', pessoas=pessoas, grupos=grupos)

@app.route('/person/<int:id>', methods=['GET', 'POST'])
def profile(id):

    dados = pr.verDados(id)
    if request.method == 'POST':
        pr.addPerson(id)
    
    busca = request.args.get('buscar')
    buscaGrupo = request.args.get('buscar')

    if busca:
        pessoas = sr.verPessoas(busca)
        grupos = sr.verGrupos(busca)

    else:
        pessoas = sr.verTudoPessoas()
        grupos = sr.verTudoGrupos()
    
    if buscaGrupo:
        grupos = sr.verGrupos(busca)
        

    return render_template('profile.html', dados=dados)

@app.route('/solicitacao', methods=['GET', 'POST'])
def solicitacoes():

    pessoas = sl.verPessoas()

    if request.method == 'POST' and 'idPessoa' in request.form:
        action = request.form['action']
        idGr = request.form['idPessoa']
        if action == 'Aceitar':
            sl.addPessoa(idGr)
            redirect('/dashboard')

    
    return render_template('friendsRequest.html', pessoas=pessoas)


@app.route('/criaGrupo', methods=['GET', 'POST'])
def criarGrupo():

    if request.method =='POST':
        nome = request.form['nome']
        desc = request.form['desc']

        file = request.files['file']

        nomeArquivo = ''

        if file.filename == '':
            nomeArquivo = ''
        else:
            nomeArquivo = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], nomeArquivo))
        
        rg.registrarGrupo(nome, desc, nomeArquivo)
        return redirect('/dashboard')

    return render_template('criarGrupo.html')

@app.route('/conta', methods=['GET', 'POST'])
def conta():
    idLogado = lg.verLogado()
    dados = pr.verDados(idLogado)

    if request.method =='POST':
        email = request.form['email']
        nome = request.form["nome"]
        senha = request.form['senha']
        cidade = request.form['cidade']
        aniversario = request.form['aniversario']
        genero = request.form.get('gender')

        ac.atualizarBanco(email, nome, senha, cidade, aniversario, genero)
        return redirect('/conta')

    
    busca = request.args.get('buscar')
    buscaGrupo = request.args.get('buscar')

    if busca:
        pessoas = sr.verPessoasContSearch(busca)

    else:
        pessoas = sr.verPessoasCont(idLogado)
    
    if buscaGrupo:
        grupos = sr.verGrupos(busca)
    else:
        grupos = sr.verTudoGrupos()
    


    return render_template('account.html', dados=dados, pessoas=pessoas)


@app.route('/mural/<int:id>', methods=['GET', 'POST'])
def muralSee(id):

    '''Pegar id usuário'''
    id_usuario = id
    
    '''Pegar dados do usuário e verificar se tem mural'''
    ds.verificaMural(id)
    dados = ds.pegarDados(id)


    grupos = gp.verGrupos()
    comments = ds.pegarComments()
    respostas = ds.pegarResp()
    pessoas = ds.pegarPessoas()


    if request.method == "POST" and 'postText' in request.form:
        '''Pegar post'''
        postText = request.form['postText']
        postImage = request.form['postImage']
        ds.registrarPost(id_usuario, postImage, postText, id_usuario)
        redirect('/dashboard')

    if request.method == "POST" and 'textComent' in request.form:
        '''Pegar comentario'''
        postComent = request.form['textComent']
        ppost = request.form['textCatch']
        pegarPost = ds.pegarIdPost(ppost)
        ds.registrarComent(postComent, pegarPost)
        redirect('/dashboard')
        
    if request.method == "POST" and 'textResp' in request.form:
        '''Pegar comentario'''
        postResp = request.form['textResp']
        comentId = request.form['textCatch2']
        pegarComment = ds.registrarResp(postResp, comentId)
        redirect('/dashboard')
    
    if request.method == 'POST' and 'idPessoa' in request.form:
        action = request.form['action']
        idGr = request.form['idPessoa']
        if action == 'Aceitar':
            sl.addPessoa(idGr)
            redirect('/dashboard')
            
    posts = ds.mostrarPosts(id)

    return render_template('mural2.html', dados=dados, pessoas=pessoas, posts=posts, grupos=grupos, comments=comments, respostas=respostas)


@app.route('/gruposAdm', methods=['GET', 'POST'])
def grupoAdm():
    idLogado = lg.verLogado()

    busca = request.args.get('buscar')

    if busca:
        grupos = sr.verGrupos(busca)

    else:
        grupos = sr.verTudoGruposAdm()
            

    return render_template('admgrupos.html', grupos=grupos)

@app.route('/grupoAdm/<int:id>', methods=['GET', 'POST'])
def grupoGerenciar(id):
    idLogado = lg.verLogado()

    busca = request.args.get('buscar')

    if busca:
        dates = sr.verMembroGrupoDates(id, busca)
        grupos = sr.verPessoas(busca)

    else:
        dates = sr.verTudoGrupoDates(id)
        grupos = sr.verTodasPessoas()

    if request.method == 'POST' and 'idPessoa' in request.form:
        action = request.form['action']
        idGr = request.form['idPessoa']
        if action == 'Aceitar':
            sl.addPessoaGrupo(idGr, id)
            redirect('/dashboard')

        if action =='Recusar':
            sl.RemovPessoaGrupo(idGr, id)
            redirect('/dashboard')

    if request.method == 'POST' and 'idPessoa2' in request.form:
        action = request.form['action']
        idGr = request.form['idPessoa2']

        if action =='Remover':
            print("entroaidsaokdsakdsaosk")
            sl.RemovPessoaGrupo2(idGr, id)
            redirect('/dashboard')
    
    return render_template('addremove.html', grupos=grupos, dates=dates)


@app.route('/grupos/<int:id>', methods=['GET', 'POST'])
def gruposSee(id):
    busca = request.args.get('buscar')

    if busca:
        pessoasGrupo = sr.verTudoGrupoDates(id)

    else:
        pessoasGrupo = sr.verTudoGrupoDates(id)
    

    grupo = sr.verGruposID(id)
        

    return render_template('gruposSee.html', pessoasGrupo=pessoasGrupo, grupo=grupo)