import sqlite3

#cur.execute("CREATE TABLE users(name, pass)")


def newuser(nm, ps):
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("INSERT INTO USERS (name, pass) VALUES (?, ?)",(nm, ps))
    print('inserted')
    con.commit()
    con.close()


def getuser(nm, ps):
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("select pass from users where name is ?", (nm,))
    out = cur.fetchone()
   # print(out)
    if out is not None:
     #   print('test')
        out = out[0]
    #    print('good')
        
        
        con.close()
        if ps == out:
            return 'allgood'
        else:
            return 'inpass'
    else:
        return 'wrongname'
    

getuser('eloni','pass')
#eloni
#pass