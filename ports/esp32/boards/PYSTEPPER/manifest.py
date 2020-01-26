freeze('../../../firmware/micropython_pymodule')
freeze('modules', (
    'webrepl.py',
    'websocket_helper.py',
    'upip.py',
    'upip_utarfile.py'
    ))

freeze('../../../pycopy-lib/uasyncio.core', ('uasyncio/core.py',))
freeze('../../../pycopy-lib/uasyncio', ('uasyncio/__init__.py',))
freeze('../../../pycopy-lib/uasyncio.websocket.server', ('uasyncio/websocket/server.py',))


freeze('../../../webconsole/dist', ('index_html.py',))

