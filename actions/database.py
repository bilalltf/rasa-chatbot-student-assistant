from sqlite3 import *
c = connect("database.sqlite")
req1="create table if not exists course(id int, subject1 str, subject2 str, sector1 str, sector2 str, prof str,link str,primary key(id))"
req2="create table if not exists institution(id_inst int, name str, type str, link str, primary key(id_inst))"
cur = c.cursor()
cur.execute(req1)
cur.execute(req2)


# coding=utf8
def insert_courses():
    c = connect("database.sqlite")
    cur = c.cursor()
    req= "insert into course values (1, 'base de données', 'bdd','SMI', 'Sciences mathématiques et informatique', 'M. E. RIFFI', 'https://mega.nz/file/euxEFTTS#WgN-rykClx1tSEjqfD3jSJgv2MLbvLW2fJCjfIS6Ov8'), (2, 'Administration Oracle', 'Oracle', 'SMI', 'Sciences mathématiques et informatique', 'Abdellah MADANI', 'https://mega.nz/file/SmZDVAZZ#gyK25eeFCeMbm-l3ttt3Ygx87l_9NBTsccrC_WeuLhI'), (3, 'Algorithme simplexe', 'Algo simplexe', 'SMI', 'Sciences mathématiques et informatique', '', 'https://mega.nz/file/H2YDXYDD#0-oo6gtZRsjqdVuljoWJWGiVmyBGb494d1989vHsTbg'), (4, 'Algorithmique II', 'Algo II','SMI', 'Sciences mathématiques et informatique', 'Loubna CHERRAT', 'https://mega.nz/folder/7iJ1wQpS#ncLYhgRIQ3Y7XuUX0GJlCw'), (5, 'Compilation', 'compl','SMI', 'Sciences mathématiques et informatique', '', 'https://mega.nz/file/7mIRlYJD#pWjyy5OGFpScjbo765MEtkHPJUKe7dg6PUVGsXENeWM'), (6, 'Recherche Opérationel', 'RO','SMI', 'Sciences mathématiques et informatique', 'Hamid ZOUAKI', 'https://mega.nz/file/avAFECzR#5y1OGdU_qyq2zBZ0BoJZx7VetY2eYY1ohh6IizQqBR0'), (7, 'java', 'java','SMI', 'Sciences mathématiques et informatique', '', 'https://mega.nz/file/3yB1gIKA#w6JKfHBxl3xThQEq2tMRo8TSli9nrI9p4M7LEGBGGQ0'), (8, 'linux', 'SE','SMI', 'Sciences mathématiques et informatique', '', 'https://mega.nz/file/nyIRkCTB#dfpbCsfLD35A9GbxYT08ydC0v7667N23FlJkgEtumQo'), (9, 'Réseau', 'Reseau','SMI', 'Sciences mathématiques et informatique', '', 'https://mega.nz/file/SyZx2ISa#w_3TPYCMLKLHijgOBKi6bbDY7FcNi1iWyDCrucZ2AeM'), (10, 'électromagnetisme', 'Electromagnetisme','SMI', 'Sciences mathématiques et informatique', '', 'https://mega.nz/file/TipWFIaR#kdpBe1xnhLs0boU7JcTtlnrVkM_Giq39TthdFkeMgJI'), (11, 'Programmation c', 'Prog c','SMI', 'Sciences mathématiques et informatique', 'Salwa BELAQZIZ', 'https://mega.nz/file/3mYVQQ7A#HH16m-0VZJSxXZmp5Dx5KbcuwYtwZLE8Lh_bm6HsaW8'), (12, 'Programmation web', 'Prog web','SMI', 'Sciences mathématiques et informatique', 'Omar BOUTKHOUM', 'https://mega.nz/file/Dy5SSYxC#7fL6G_cXb_ihHDI1XgHo4ZxSk-kKguy9A8tmLJU82Gw')  "
    cur.execute(req)
    c.commit()
def insert_inst():
    c = connect("database.sqlite")
    cur = c.cursor()
    req= "insert into institution values (1, 'Faculté des Sciences Juridiques, Economiques et Sociales El Jadida', 'faculté','http://www.fsjesj.ucd.ac.ma/'), (2, 'Faculté des lettres et des  sciences humaines El Jadida', 'faculté','http://www.flshj.ucd.ac.ma/'), (3, 'Faculté des Sciences El Jadida', 'faculté','http://www.fs.ucd.ac.ma/'), (4, 'École Nationale de Commerce et de Gestion El Jadida', 'école','http://www.encgj.ucd.ac.ma/'), (5, 'École Nationales des Sciences Appliquées El Jadida', 'école','http://www.ensaj.ucd.ac.ma/'), (6, 'École Supérieur de Technologie Sidi Benour', 'école','http://www.estsb.ucd.ac.ma/')"
    cur.execute(req)
    c.commit()

#insert_courses()
#insert_inst()    
c.close()

