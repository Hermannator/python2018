dag = (input("Ukedag: ")).lower()
ukedager = ["mandag","tirsdag","onsdag","torsdag","fredag","lørdag","søndag"]
def is_workday(dag):
    if ukedager.index(dag) < 5:
        return True
    else:
        return False