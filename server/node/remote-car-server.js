let server = require('express')();
const PORT_NUMBER = 3000;

server.get('/', function(req, res) {
    res.send('You won\'t find anything here.\n');
});
server.get('/left', function(req, res, next) {
    res.send('Hold on... I\'m moving left.\n');
});
server.get('/right', function(req, res, next) {
    res.send('Hold on... I\'m moving right.\n');
});
server.get('/up', function(req, res, next) {
    res.send('Hold on... I\'m moving up.\n');
});
server.get('/down', function(req, res, next) {
    res.send('Hold on... I\'m moving down.\n');
});
server.listen(PORT_NUMBER, function() {
    console.log(
        'Go to http://localhost:3000\n'               +
        'Go to http://localhost:3000/right\n'         +
        'Go to http://localhost:3000/left\n'          +
        'Go to http://localhost:3000/up\n'            +
        'Go to http://localhost:3000/down\n'          +
        'OR\n' +
        'Go to curl http://localhost:3000\n'        +
        'Go to curl http://localhost:3000/left\n'   +
        'Go to curl http://localhost:3000/right\n'  +
        'Go to curl http://localhost:3000/up\n'     +
        'Go to curl http://localhost:3000/down\n'
    );
});