const {Builder, By, Key, until} = require('selenium-webdriver');
var express = require('express');
var app = express()
var mysql = require('mysql');

const connection = mysql.createConnection({
  //properties
  host:"localhost",
  user:"root",
  password:"",
  database: 'sampleDB',
});


connection.connect(function(error){
  if(!!error){
    console.log('Error');
  }else{
    console.log('Connected');
  }
});

  let name;
  let marks;

(async function example() {
  let driver = await new Builder().forBrowser('firefox').build();

  try {
    await driver.get('http://www.exam.kannuruniversity.ac.in/UG/bsc3semresult2021/result19.php');
    await driver.findElement(By.name('regno')).sendKeys('mm20ccsr03');
    await driver.findElement(By.name('aadhaar')).sendKeys('663432470004');
    await driver.findElement(By.name('but')).click();
    await driver.wait(until.elementLocated(By.xpath('/html/body/div[1]/div[2]/div[6]/div/div/div[2]/span[21]')), 1000);
    await driver.findElement(By.xpath('/html/body/div[1]/div[2]/div[6]/div/div/div[2]/span[21]')).getText().then(function(txt){
      name =  txt;
    });
    await driver.findElement(By.xpath('/html/body/div[1]/div[2]/div[6]/div/div/div[2]/span[183]')).getText().then(function(txt){
      marks = txt;
    });
    
  } finally {
//     setTimeout(() => {
//   console.log("Details Scraped Bruh!");
//   console.log(name);
//   console.log(marks);
//   driver.close();
// }, "200")
      await console.log(name);
      await console.log(marks);
      driver.close();
  }
})();

app.get('',function(req,res){
  res.sendFile(__dirname+'/public/index.html');
})

app.get('/display',function(req,res){
    connection.query("SELECT * FROM sample",function(error,rows,fields){
      if(!!error){
        console.log("error in the query");
      }
      else{
        console.log("successful query");
        console.log(rows[0].Name);
        console.log(rows[0].marks);
        res.render('index',{"data":rows});
      }
    });
    // res.sendFile(__dirname+'/public/display.html',{data:rows});
});

app.get('/delete',function(req,res){
  connection.query('truncate table sample');
  console.log("Deleted");
})

app.get('/insert',function(req,res){
  connection.query("insert into sample values('"+name+"','"+marks+"')");
  console.log("inserted");
})

app.listen(1337);