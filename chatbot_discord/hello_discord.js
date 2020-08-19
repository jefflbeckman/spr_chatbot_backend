const Discord = require('discord.js');
const MongoClient = require('mongodb').MongoClient;
const dburl = "mongodb://localhost:27017/"
const client = new Discord.Client();
var dbo;

client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
    if (msg.channel.name === "bot-test"
        && msg.author.username !== client.user.username) {
        console.log(`Adding a message from ${msg.author.username} into the database`);
        db_entry = {
            time: msg.createdTimestamp,
            channel: msg.channel.name,
            username: msg.author.username,
            content: msg.content,
        };
        MongoClient.connect(dburl, function(err, db) {
            if (err) throw err;
            var dbo = db.db("DiscordMessagesDB").collection("messages");
            dbo.insertOne(db_entry, function(err, res) {
                if (err) throw err;
            })
            dbo.countDocuments({}, function(err, numMessages) {
                if (err) throw err;
                msg.reply(`I have heard ${numMessages} things`);
                db.close()
            })
        })

    }
});



client.login('');
