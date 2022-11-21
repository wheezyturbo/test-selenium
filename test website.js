const {
    Builder,
    By,
    Key,
    until
} = require('selenium-webdriver');
var express = require('express');
var app = express()
var mysql = require('mysql');
require('json-response');
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
const connection = mysql.createConnection({
    //properties
    host: "localhost",
    user: "root",
    password: "",
    database: 'sampleDB',
});
connection.connect(function (error) {
    if (!!error) {
        console.log('Database connection : False');
    } else {
        console.log('Connected To the database');
    }
});
// regno = ['mm20ccsr03', 'mm20ccsr28', 'mm20ccsr22', 'mm20ccsr18', 'mm20ccsr16', 'mm20ccsr13'];
// aadhar = [663432470004, 480001511958, 686185381631, 578533381676, 823508626405, 783917821528];
// var name = [];
// var marks = [];
// (async function example() {
//     // let a = await readline.question("enter regno");
//     // let b = await readline.question("Enter aadhaar");
//     const screen = {
//         width: 640,
//         height: 480
//     };
//     const firefox = require('selenium-webdriver/firefox');
//     let driver = await new Builder().forBrowser('firefox').setFirefoxOptions(new firefox.Options().headless().windowSize(screen)).build();
//     for (i in regno) {
//         try {
//             await driver.get('http://www.exam.kannuruniversity.ac.in/UG/bsc4semresult2022/result19.php');
//             await driver.findElement(By.name('regno')).sendKeys(regno[i]);
//             await driver.findElement(By.name('aadhaar')).sendKeys(aadhar[i]);
//             await driver.findElement(By.name('but')).click();
//             await driver.wait(until.elementLocated(By.xpath('/html/body/div[1]/div[2]/div[6]/div/div/div[2]/span[21]')), 1000);
//             await driver.findElement(By.xpath('/html/body/div[1]/div[2]/div[6]/div/div/div[2]/span[20]')).getText().then(function (txt) {
//                 name[i] = txt;
//             });
//             await driver.findElement(By.xpath('/html/body/div[1]/div[2]/div[6]/div/div/div[2]/span[225]')).getText().then(function (txt) {
//                 marks[i] = txt;
//             });
//         } finally {
//             //     setTimeout(() => {
//             //   console.log("Details Scraped Bruh!");
//             //   console.log(name);
//             //   console.log(marks);
//             //   driver.close();
//             // }, "200")
//              console.log(name[i]);
//             if (marks[i] == "-") {
//                  console.log("failed\n");
//             } else {
//                  console.log(marks[i] + '\n');
//             }
//         }
//     }
//     driver.close();
// })();


app.get('', function (req, res) {
    res.sendFile(__dirname + '/public/index.html');
})
app.get('/display' || '/delete/display', function (req, res) {
    // connection.query("SELECT * FROM sample", function(error, results) {
    //     if (error) {
    //         console.log("error in the query");
    //     } else {
    //         console.log("successful query");
    //         console.log(results.row[0].name)
    //         res.render('index', {
    //             data: results.rows
    //         });
    //     }
    // });
    connection.query('SELECT * FROM sample', (error, results) => {
        if (error) {
            throw error
        }
        console.log(results);
        res.render('index', {
            data: results
        });
    })
    // res.sendFile(__dirname+'/public/display.html',{data:rows});
});

app.get('/test', function (req, res) {
    connection.query('select * from sample', (error, results) => {
        if (error) {
            throw error
        }
        res.sendFile(__dirname + '/public/display.html', { data: results });
    })
})



app.get('/delete', function (req, res) {
    connection.query('truncate table sample');
    console.log("Deleted");
    res.redirect('/')
})
app.get('/insert', function (req, res) {
    for (i in regno) {
        connection.query("insert into sample values('" + name[i] + "','" + marks[i] + "')");
        console.log("inserted " + name[i]);
    }
    res.redirect('/')
})

app.get('/sort' || '/display/sort', function (req, res) {
    // connection.query("SELECT * FROM sample", function(error, results) {
    //     if (error) {
    //         console.log("error in the query");
    //     } else {
    //         console.log("successful query");
    //         console.log(results.row[0].name)
    //         res.render('index', {
    //             data: results.rows
    //         });
    //     }
    // });
    connection.query('SELECT * FROM sample ORDER BY Marks DESC', (error, results) => {
        if (error) {
            throw error
        }
        console.log(results);
        res.render('index', {
            data: results
        });
    })
    // res.sendFile(__dirname+'/public/display.html',{data:rows});
});

app.listen(1337);