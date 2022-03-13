import os
import dash

import layout
import callbacks

app = dash.Dash()

## Create Main View
app.layout = layout.layout

def run():
    app.run_server(port=8888, host='0.0.0.0', debug=True)

if __name__ == '__main__':
    run()
