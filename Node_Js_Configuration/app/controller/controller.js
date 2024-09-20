module.exports = {
    messageController(req, res) {
        let response = {
            success: true,
            message: "Hello World!!!"
        };
        res.status(200).send(response);
    }
};
