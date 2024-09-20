var express = require('express'),
    app = express(),
    bodyparser = require('body-parser'),
    connectdb = require('./config/database/mongodb').connect,
    swagger_ui = require('swagger-ui-express'),
    swagger_doc = require('./app/lib/swagger-ui/api_docs');

app.use(bodyparser.json());

require('./app/routes/routes')(app);

app.use('/swagger/api', swagger_ui.serve, swagger_ui.setup(swagger_doc));

app.listen(process.env.PORT || 3000, () => {
    console.log("Server is running on port: " + (process.env.PORT || 3000));
    connectdb();
});
