import sqlite3
import os
from datetime import datetime

class database_mgmt():

    def db_check(self):
        if not os.path.isfile("Tama_Stats.db"):
            db = sqlite3.connect("Tama_Stats.db")
            cur = db.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS stat_detail "
                        "('id' INTEGER PRIMARY KEY,"
                        "'datetime' int,"
                        "'stat_name' text,"
                        "'stat_before' integer,"
                        "'stat_after' integer,"
                        "'degrading' boolean,"
                        "'self_pres' boolean)")

            database_mgmt.update_table("BeginningPlay", "100", "100", "False", "False")

            db.commit()
            cur.close()
            db.close()

    def update_table(self, stat_name, prior_value, after, degrading_value, pres_status):
        db = sqlite3.connect("Tama_Stats.db")
        cur = db.cursor()
        now2 = (datetime.now().year * 10000000000 +
                datetime.now().month * 100000000 +
                datetime.now().day * 1000000 +
                datetime.now().hour * 10000 +
                datetime.now().minute * 100 +
                datetime.now().second)

        cur.execute("INSERT INTO stat_detail(datetime,stat_name,stat_before,stat_after,degrading,self_pres) "
                    "VALUES ('" + str(now2) + "','" + str(stat_name) + "','" + str(prior_value) + "','" + str(after) +
                    "','" + str(degrading_value) + "'," + str(pres_status) + ")")

        db.commit()
    #  cur.close()

    def resumevalues(self, valuetest):
        db = sqlite3.connect("Tama_Stats.db")
        cur = db.cursor()
        curvalue = 0

        get_latest_stat = "SELECT stat_after FROM stat_detail WHERE stat_name =? ORDER BY ID DESC LIMIT 1 "
        cur.execute(get_latest_stat, (valuetest,))

        for row in cur:
            curvalue = row[0]

        cur.close()
        db.close()

        return curvalue