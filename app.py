from flask import Flask, render_template, request, make_response
from bahnapi.functions import download_passbook

app = Flask(__name__)

@app.route('/')
def index():
	args = request.args.copy()
	if 'auftragsnummer' in args and 'nachname' in args:
		auftragsnummer = args.get('aufteagsnummer')
		nachname = args.get('nachname')
		passbook = download_passbook(auftragsnummer, nachname)
		resp = make_response(passbook)
		resp.headers['Content-type'] = 'application/vnd.apple.pkpass'
		resp.headers['content-disposition'] = 'attachment;' + \
                                                      'filename=' + auftragsnummer + '.pkpass'
		return resp
	return render_template('form.html')
