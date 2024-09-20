const controller = require('../controller/controller');

module.exports = (routes) => {
    routes.get('/hello_world', controller.messageController);
    routes.get('/', (req, res) => {
        res.status(200).send({ success: true, message: "Hello World!!!" });
    });
};

