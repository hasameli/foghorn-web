from foghornw import app
from flask import render_template

@app.route('/')
def index():
  whitelist = load_list("%s%s" % (app.config['FOGHORN_LISTDIR'], 'whitelist'))
  blacklist = load_list("%s%s" % (app.config['FOGHORN_LISTDIR'], 'blacklist'))
  greylist  = load_list("%s%s" % (app.config['FOGHORN_LISTDIR'], 'greylist'))
  return render_template('index.html', title="Foghorn Configurator",
      whitelist = whitelist, blacklist = blacklist, greylist = greylist)


def load_list(filename):
  """Load the specified list."""
  lines = []
  try:
    with open(filename, mode='r') as read_file:
      lines = [x.strip() for x in read_file.readlines()]
      return lines
  except IOError as io_error:
    print "%s" % io_error
    return []
