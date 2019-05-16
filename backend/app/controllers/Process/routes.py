from app import app

app.add_url_rule('/create-process'    , methods=['POST'], endpoint='/create-process')
app.add_url_rule('/teste'             , methods=['POST'], endpoint='/teste')

