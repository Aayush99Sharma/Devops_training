const mongoose = require('mongoose');
require('dotenv').config();

function connectDB() {
    mongoose.connect(process.env.MONGODB_URL, { 
        // Options are no longer needed in Mongoose v4.0.0 and above
    })
    .then(() => {
        console.log("MongoDB connection established successfully!!!");
    })
    .catch((err) => {
        console.log("MongoDB connection failed!!!", err);
    });
}

module.exports = { connect: connectDB };
