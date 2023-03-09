from flask import Flask,render_template
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///marks.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Marks(db.Model):
    regno = db.Column(db.Text, primary_key=True)
    name = db.Column(db.Text(30))
    m1 = db.Column(db.Integer)
    m2 = db.Column(db.Integer)
    m3 = db.Column(db.Integer)
    m4 = db.Column(db.Integer)
    m5 = db.Column(db.Integer)
    mp = db.Column(db.Float)
    
    def __repr__(self) -> str:
    	return f"{self.regno} - {self.name} - {self.m1} - {self.m2} - {self.m3} - {self.m4} - {self.m5} -{self.mp}"

@app.route("/") 
def home():
    return render_template('index.html')
 
@app.route("/whot")
def whot():
    regarray = ['mm20ccsr03']
    aadhararray = [663432470004]
    #i dont know this shit was working fine before but dont know what the fuck just happened lol
    for i in regarray:
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox()
        driver.get('http://www.exam.kannuruniversity.ac.in/UG/bsc3semresult2021/result19.php')
        print("website loaded")
        regno_ = driver.find_element("xpath", '//*[@id="regno"]')
        print("regno found")
        print(i)
        print(regarray[0])
        regno_.send_keys(i)
        print("regno path found")
        aadhar = driver.find_element("xpath", '//*[@id="aadhaar"]')
        j = 0
        aadhar.send_keys(int(aadhararray[j]))
        j=j+1
        print("aadhar path found")
        driver.find_element("xpath",'//*[@id="cut"]').click()
        time.sleep(0.5)
        with open("./results/results.html", "w") as f:
            f.write(driver.page_source)
            for dirpath, dirnames, filenames in os.walk('<source path>'):
                for fileName in filenames:
                    print(holo)
                    driver.get(f'file://{os.path.join(dirpath, fileName)}')
                    time.sleep(7)
                    driver.execute_script('window.print();')
                    driver.close()

        # name_ = driver.find_element("xpath",'/html/body/div[1]/div[2]/div[4]/div/div/div[2]/span[21]').text
        # mark1 = driver.find_element("xpath",'/html/body/div[1]/div[2]/div[4]/div/div/div[2]/span[73]').text
        # mark2 = driver.find_element("xpath",'/html/body/div[1]/div[2]/div[4]/div/div/div[2]/span[94]').text
        # mark3 = driver.find_element("xpath",'/html/body/div[1]/div[2]/div[4]/div/div/div[2]/span[116]').text
        # mark4 = driver.find_element("xpath",'/html/body/div[1]/div[2]/div[4]/div/div/div[2]/span[138]').text
        # mark5 = driver.find_element("xpath",'/html/body/div[1]/div[2]/div[4]/div/div/div[2]/span[159]').text
        # markp = driver.find_element("xpath",'/html/body/div[1]/div[2]/div[4]/div/div/div[2]/span[183]').text
        print(f," written successfully")
        # print("mark 1 = ",mark1,"\nmark2 = ",mark2,"\nmark3 = ",mark3,"\nmark4 = ",mark4,"\nmark5 = ",mark5,"\ntotal marks = ",markp)
        time.sleep(5)
        driver.close()
        print("retrievved successfully")
        marks = Marks(regno = regarray[i],name = name_,m1 = mark1,m2 = mark2,m3 = mark3,m4 = mark4,m5 = mark5,mp = markp)
        db.session.add(marks)
        db.session.commit()
    return render_template("index.html")

@app.route('/table')
def showtable():
	allMarks = Marks.query.all()
	return render_template("table.html",allMarks = allMarks)

@app.route('/delete')
def dlt():
    Marks.query.delete()
    db.session.commit()
    return render_template("index.html")

