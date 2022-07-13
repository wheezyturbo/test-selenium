from selenium import webdriver
import time
import psycopg

DB_HOST="localhost"
DB_NAME='postgres'
DB_USER='seltest'
DB_PASS = 'notrespass'

conn=psycopg.connect(dbname=DB_NAME, user=DB_USER,password=DB_PASS,host=DB_HOST)


regarray = ['mm20ccsr03','mm20ccsr03']
aadhararray = [663432470004,663432470004]

for i in (0,len(aadhararray)-1):

    driver = webdriver.Firefox()
    driver.get('http://www.exam.kannuruniversity.ac.in/UG/bsc3semresult2021/result19.php')
    
    regno = driver.find_element("xpath", '//*[@id="regno"]')
    regno.send_keys(regarray[i])

    aadhar = driver.find_element("xpath", '//*[@id="aadhaar"]')

    aadhar.send_keys(int(aadhararray[i]))
    driver.find_element("xpath",'//*[@id="cut"]').click()
    time.sleep(0.5)
    name = driver.find_element("xpath",'/html/body/div[1]/div[2]/div[4]/div/div/div[2]/span[21]').text
    mark1 = driver.find_element("xpath",'/html/body/div[1]/div[2]/div[4]/div/div/div[2]/span[73]').text
    mark2 = driver.find_element("xpath",'/html/body/div[1]/div[2]/div[4]/div/div/div[2]/span[94]').text
    mark3 = driver.find_element("xpath",'/html/body/div[1]/div[2]/div[4]/div/div/div[2]/span[116]').text
    mark4 = driver.find_element("xpath",'/html/body/div[1]/div[2]/div[4]/div/div/div[2]/span[138]').text
    mark5 = driver.find_element("xpath",'/html/body/div[1]/div[2]/div[4]/div/div/div[2]/span[159]').text
    markp = driver.find_element("xpath",'/html/body/div[1]/div[2]/div[4]/div/div/div[2]/span[183]').text
    # print("mark 1 = ",mark1,"\nmark2 = ",mark2,"\nmark3 = ",mark3,"\nmark4 = ",mark4,"\nmark5 = ",mark5,"\ntotal marks = ",markp)
    driver.close()
    cur = conn.cursor()

    # cur.execute("drop table info;")

    # cur.execute("create table info (name text,mark1 int,mark2 int,mark3 int,mark4 int,mark5 int,percentage float);")

    cur.execute("insert into info values(%s,%s,%s,%s,%s,%s,%s)",(name,mark1,mark2,mark3,mark4,mark5,markp))
    #cur.execute("CREATE TABLE student1 (id int primary key,name varchar);")
    # cur.execute("insert into student1 values(%s,%s)",(1,"hello",))



    conn.commit()
cur.execute("select * from info;")

print(cur.fetchall())
conn.close()

print('marks scraped terminating....................\n')