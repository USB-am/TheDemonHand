import eel


def run_ui():
	eel.init('ui/web')
	eel.start('templates/index.html',
		      jinja_templates='templates')
