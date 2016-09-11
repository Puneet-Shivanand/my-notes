1)LOAD DATA INFILE '/tmp/mydata.txt' INTO TABLE HGVD;

2)select hgvd_table.DescriptorUI, hgvd_table.RSID, hgvd_table.PMID, mesh_table.TreeNumber from HGVD hgvd_table, MeshC mesh_table where  hgvd_table.DescriptorUI = mesh_table.DescriptorUI group by hgvd_table.RSID,hgvd_table.PMID INTO OUTFILE '/tmp/OUTPUT.csv'


3)"""UPDATE HGVD LEFT JOIN MeshC 
                   ON HGVD.DescriptorUI=MeshC.DescriptorUI 
                   SET HGVD.ISSUES='DELETE_ME' where MeshC.TreeNumber='{}'
                 """.format(j)

4)select RSID, PMID from HGVD where RSID='***'



5)select count(*) from HGVD where ISSUES='DELETE_ME';

6)select count(*) from HGVD where ISSUES='DO_NOTHIN';

7)select * from HGVD limit 10 \G;

8)***UPDATED***
select hgvd_table.DescriptorUI, hgvd_table.RSID, hgvd_table.PMID, mesh_table.TreeNumber from HGVD1 hgvd_table, MeshC1 mesh_table where  hgvd_table.DescriptorUI = mesh_table.DescriptorUI order by hgvd_table.PMID;

8)select DescriptorUI from HGVD1 where PMID='{}' and RSID='{}' '.format(i,j)


9)$MySql Query that Concatinates multiple trees from MeshC DB

select DescriptorNameString, GROUP_CONCAT(TreeNumber) from MeshC where DescriptorNameString='Lung Neoplasms' GROUP BY DescriptorNameString limit 10 \g;

10) SQL dump 

mysqldump -u root -p test_fb MeshC > dumpfile.sql

11) USER LOGIN:
	mysql -h 192.168.0.110 -u puneet -p puneet123 


12) Mysql DUMP
	mysqldump -h 192.168.0.110 -u puneet -p test HGVD1 > BLANK_RSID.sql

13) write select output to file:
	 select * INTO OUTFILE '/tmp/BLANK_RSID.CSV' FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' from HGVD1 where RSID='';

14)Delete Query 

	DELETE FROM table_name [WHERE Clause]

15) mysql screen clear

	\! clear


16) delete certain count of rows : 
delete from HGVD1 where ID between 6002 and 6499;

17) limit certain rows only 
	select id, PMID, RSID, DescriptorUI, CURATED_BY, ISSUES from HGVD1_BACKUP_11_06_2015 limit 0,1000;

18) to compare old and new databases;
	select id from pu where id not in (select ID from hgvd);

19) update field with comma seperated values:

	UPDATE `yable` SET `value`= `value` + ',blue' WHERE `id` = 1;
		or
	UPDATE `yable` SET `value`= CONCAT(value,',blue') WHERE `id` = 1;



20) update the table field from one table in one database to another table in another database:

	update test.HGVD1 left join puneet.hgvd_test ON test.HGVD1.id=hgvd_test.id set HGVD1.FLAGS='DM' where puneet.hgvd_test.ISSUES='DM';



21) display from last :
		select id,FLAGS from HGVD1 where FLAGS='DM' ORDER BY ID DESC LIMIT 10;

22)select only distinct tag from marfan
	select distinct * from marfan where info like'%/*%'limit 10;
	
23) ALTERING TABLE STRUCTURE

	alter table marfan add column DescriptorUI varchar(7) NOT NULL AFTER info 



24) substring matching
	SUBSTRING_INDEX( sift , '(', 1 ) AS sift, SUBSTRING_INDEX(SUBSTRING_INDEX( sift , '(', 2 ),'(',-1) AS C2  from sam

25) use --local-infile when importing local csv files
	abdul@xmpp3:~/Desktop/Jiva$ mysql -uroot -p --local-infile


25) change or replace string substring	
	update marfan set info=REPLACE(info, '*','');

26)	Querying for Dieases !!
	Age of Onset:
	select marfan.DescriptorUI, TreeNumber from marfan left join Mesh on marfan.DescriptorUI=Mesh.DescriptorUI where marfan.DescriptorUI='D017668';
	
	Get Age of Onset from Mesh 
	select * from marfan where DescriptorUI='D017668';


27) dumping:
	mysqldump -u root -p test_fb marfan > marfan_up.sql 


28) CREATE TABLE marfan_update(
				ID INT NOT NULL AUTO_INCREMENT,
				AGE_OF_ONSET VARCHAR(100),
				AGE_OF_DIAGNOSIS VARCHAR(100),
				AGE_OF_DEATH VARCHAR(100),
				CLINICAL_BIOMARKERS VARCHAR(100),
				GEOGRAPHY VARCHAR(100),
				GENES VARCHAR(100),
				CHROMOSOME VARCHAR(100),
				PATHWAY VARCHAR(100),
				ORGAN_OF_ONSET VARCHAR(100),
				THERAPY VARCHAR(100),
				DRUG_NAME VARCHAR(100),
				DRUG_TARGET VARCHAR(100),
				TIME_TO_DEATH VARCHAR(100),
				GENETIC_VARIATIONS VARCHAR(100),
				PRIMARY KEY ( ID )
				);


29)	get all age groups
	select * from Mesh where TreeNumber like 'M01.060%';


30) for all connections	

	conn = MySQLdb.connect("localhost","root","root","test_fb")
	conn.autocommit(True)


31)	create table sam_1 SELECT id, medline_tag, GROUP_CONCAT(info SEPARATOR '|') as info FROM sam GROUP BY id, medline_tag;

create table sam_1 SELECT pmid, value, GROUP_CONCAT(Tree SEPARATOR '|') as Tree FROM sam_aged GROUP BY pmid;

32)	select id,   max(case when medline_tag = "AU" then info end) AU,   max(case when medline_tag = "PG" then info end) PG,   max(case when 		medline_tag = "SS" then info end) pg, max(case when medline_tag = "SO" then info end) SO  from sam_1 group by id;

33) updating table with .sql file in mysql terminal
		
			source /tmp/marfan_capture.sql


34) selecting only those that records
	select id, marfan.DescriptorUI from marfan left join Mesh on marfan.DescriptorUI=Mesh.DescriptorUI where marfan.DescriptorUI='D017668' 	group by id


35)	joins!!	
select * from T1 LEFT JOIN T2 on T1.id=T2.id limit 10;
update T1 LEFT JOIN T2 on T1.id=T2.id set T1.id=t2.PMID limit 10;

select count(*),id, marfan.DescriptorUI from marfan left join Mesh on marfan.DescriptorUI=Mesh.DescriptorUI where Mesh.TreeNumber like 'Z%' group by id ;


35) select * from age_of_diagnosis INNER JOIN age_of_onset INNER JOIN organ_onset where age_of_diagnosis.pmid=age_of_onset.pmid and age_of_diagnosis.pmid=organ_onset.pmid limit 5;


36)	 SELECT pmid, GROUP_CONCAT(smesh SEPARATOR ' '), pmesh, smesh FROM age_of_diagnosis GROUP BY pmid limit 5;

36)	SELECT pmid,pmesh, GROUP_CONCAT(smesh SEPARATOR ',') from clinical_biomarkers GROUP BY pmid 	;



 SELECT pmid,pmesh, GROUP_CONCAT(smesh SEPARATOR ',') from clinical_biomarkers GROUP BY pmid into outfile '/tmp/cbio_comma.csv' FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n';

//steps
select * from drug_target into outfile '/tmp/dtarget.csv' FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n';

SELECT pmid,pmesh, GROUP_CONCAT(smesh SEPARATOR ',') from drug_target GROUP BY pmid into outfile '/tmp/dtarget_comma.csv' FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n';

delete from drug_target;

load data infile '/tmp/dtarget_comma.csv' into table drug_target;

select pmid,pmesh,smesh,MAX(LENGTH(smesh)) from age_of_diagnosis order by length(smesh) limit 5;limit 5;

37) alter a column in table
	alter table marfan_main add id INT NOT NULL AUTO_INCREMENT FIRST, ADD PRIMARY KEY(id);
	alter table marfan_main add age_diagnosis varchar(200) AFTER pmid
	alter table marfan_main add age_onset varchar(110) AFTER age_diagnosis	

38)	SELECT Max(CHAR_LENGTH(`Tree`)) from therapy;


select * from  marfan_main left join age_of_diagnosis on marfan_main.pmid=age_of_diagnosis.pmid where marfan_main.age_diagnosis=age_of_diagnosis.smesh
update marfan_main left join age_of_diagnosis on marfan_main.pmid=age_of_diagnosis.pmid set marfan_main.age_diagnosis=age_of_diagnosis.smesh


 alter table age_of_onset change pmid pmid varchar(20) NULL;
	


update marfan_main left join chromosome on marfan_main.pmid=chromosome.pmid set marfan_main.chromosome=chromosome.Tree

update marfan_main left join clinical_biomarkers on marfan_main.pmid=clinical_biomarkers.pmid set marfan_main.clinical_biomarkers=clinical_biomarkers.smesh;

update marfan_main left join drug_name on marfan_main.pmid=drug_name.pmid set marfan_main.drug_name=drug_name.Tree;

update marfan_main left join drug_target on marfan_main.pmid=drug_target.pmid set marfan_main.drug_target=drug_target.smesh;

update marfan_main left join genes on marfan_main.pmid=genes.pmid set marfan_main.genes=genes.Tree;

update marfan_main left join geography on marfan_main.pmid=geography.pmid set marfan_main.geography=geography.Tree;

update marfan_main left join organ_onset on marfan_main.pmid=organ_onset.pmid set marfan_main.organ_onset=organ_onset.Tree;

update marfan_main left join pathway on marfan_main.pmid=pathway.pmid set marfan_main.pathway=pathway.Tree;

update marfan_main left join therapy on marfan_main.pmid=therapy.pmid set marfan_main.therapy=therapy.Tree;

update marfan_names left join drug_name on marfan_names.pmid=drug_name.pmid set marfan_names.drug_name=Mesh.DescriptionNameString;



****IMPORTANT

 update marfan_names left join marfan_main on marfan_names.pmid=marfan_main.pmid left join Mesh on marfan_main.clinical_biomarkers=Mesh.TreeNumber set marfan_names.clinical_biomarkers=Mesh.descriptorNameString;

create table sam select pmid, age_diagnosis from marfan_main where age_diagnosis is not null limit 10;

SELECT pmid, SUBSTRING_INDEX(SUBSTRING_INDEX(t.age_diagnosis, ',', n.n), ',', -1) value
 FROM sam t CROSS JOIN 
 (
  SELECT a.N + b.N * 10 + 1 n
    FROM 
   (SELECT 0 AS N UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) a
  ,(SELECT 0 AS N UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) b
   ORDER BY n 
  ) n
WHERE n.n <= 1 + (LENGTH(t.age_diagnosis) - LENGTH(REPLACE(t.age_diagnosis, ',', '')))
ORDER BY pmid, value limit 10;



SELECT pmid, SUBSTRING_INDEX(SUBSTRING_INDEX(t.drug_target, ',', n.n), ',', -1) value
 FROM sam_dtarget t CROSS JOIN 
 (
  SELECT a.N + b.N * 10 + 1 n
    FROM 
   (SELECT 0 AS N UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) a
  ,(SELECT 0 AS N UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) b
   ORDER BY n 
  ) n
WHERE n.n <= 1 + (LENGTH(t.drug_target) - LENGTH(REPLACE(t.drug_target, ',', '')))
ORDER BY pmid, value limit 10;

SELECT pmid, value, GROUP_CONCAT(Tree SEPARATOR '|') as Tree FROM sam_aged GROUP BY pmid limit 5;

update sam_aged INNER JOIN Mesh on sam_aged.value=Mesh.TreeNumber set Tree = DescriptorNameString ;

update sam_dtarget1 INNER JOIN Mesh on sam_dtarget1.value=Mesh.TreeNumber set Tree = DescriptorNameString ;

update marfan_names, sam_aged1 set age_diagnosis=Tree where marfan_names.pmid=sam_aged1.pmid;

SELECT pmid, value, GROUP_CONCAT(Tree SEPARATOR '|') as Tree FROM sam_dtarget1 GROUP BY pmid limit 5;

update marfan_names, sam_dtarget1 set drug_target=Tree where marfan_names.pmid=sam_dtarget1.pmid; 

SELECT pmid, SUBSTRING_INDEX(SUBSTRING_INDEX(t.clinical_biomarkers, ',', n.n), ',', -1) value
 FROM sam_cbio t CROSS JOIN 
 (
  SELECT a.N + b.N * 10 + 1 n
    FROM 
   (SELECT 0 AS N UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) a
  ,(SELECT 0 AS N UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) b
   ORDER BY n 
  ) n
WHERE n.n <= 1 + (LENGTH(t.clinical_biomarkers) - LENGTH(REPLACE(t.clinical_biomarkers, ',', '')))
ORDER BY pmid, value limit 10;

update sam_cbio1 INNER JOIN Mesh on sam_cbio1.value=Mesh.TreeNumber set Tree = DescriptorNameString ;

SELECT pmid, value, GROUP_CONCAT(Tree SEPARATOR '|') as Tree FROM sam_cbio1 GROUP BY pmid ;

update marfan_names, sam_cbio2 set clinical_biomarkers=Tree where marfan_names.pmid=sam_cbio2.pmid; 


.*(protective).* (rs.*).*


'.*(rs[[:digit:]]{8}).*protective'


39)	to match rsid with specified allele

			rs\d+(.*?)\s


40)	to load certain columns:

		load data infile '/tmp/pro_allel.csv' into table protective_allele(pmid, abstract);

41)	select DescriptorUI, body from mysql_ml, SUPP_TERMUI where DescriptorNameString = body limit 5;


42)	CREATE TABLE terms_in_abst(
				id INT NOT NULL AUTO_INCREMENT,
				pmid INT NOT NULL,
				rsid VARCHAR(50),
				keyword VARCHAR(100),
				disease VARCHAR(100),
				sentence text,
				PRIMARY KEY ( id )
				);
43)	https://www.youtube.com/watch?v=ActAA6_re3M

44)	SELECT LOCATE('st','myteststring');

45)	with open('/home/user/Desktop/HGVD_aug_2015_scripts/workflow/terms_in_abst.csv',"a") as csvfile:
							writerr=csv.writer(csvfile, delimiter='|')
							writerr.writerow([r[0],str1, word, str_row])

46)	alter table terms_in_abst add column allele varchar(100) after sentence;

47)	select GROUP_CONCAT(variantaccession), start, end, BD_start, BD_end from Breakdancer_Variants GROUP BY BD_start,BD_end limit 50 \G;
48)	mysql --local-infile -uroot -pyourpwd yourdbname


****
SELECT DISTINCT rsid, pmid ,count(*) FROM HGVD group by RSID having COUNT(*) > 1;

 select * from HGVD where pmid='22393390';

select RSID, PMID, DescriptorUI from HGVD where DescriptorUI='D003376' limit 10;

select t1.DescriptorUI, t2.TreeNumber from (SELECT DISTINCT rsid, pmid ,count(*), DescriptorUI FROM HGVD group by RSID having COUNT(*) > 1 limit 50) as t1, (select H.DescriptorUI, M.TreeNumber from HGVD H, MeshC M where H.DescriptorUI=M.DescriptorUI limit 50) as t2 group by t2.TreeNumber;


select t1.DescriptorUI, t2.TreeNumber from (SELECT DISTINCT rsid, pmid ,count(*), DescriptorUI FROM HGVD group by RSID having COUNT(*) > 1 limit 500) as t1, (select H.DescriptorUI, M.TreeNumber from HGVD H, MeshC M where H.DescriptorUI=M.DescriptorUI limit 500) as t2 group by t2.TreeNumber
    -> INTO OUTFILE '/tmp/OP.csv'
    -> FIELDS TERMINATED BY ','
    -> LINES TERMINATED BY '\n';



*

SELECT DISTINCT id, rsid, pmid, DescriptorUI FROM HGVD WHERE pmid > 1 limit 500;


select M.DescriptorUI, M.TreeNumber from MeshC M, HGVD H where M.DescriptorUI = H.DescriptorUI in (' + ','.join(map(str, a)) + ') limit 10;

select t1.RSID, t1.PMID, t1.DescriptorUI, t2.TreeNumber from (select DISTINCT rsid, pmid, DescriptorUI from HGVD where pmid>1 limit 5000) as t1, (select M.DescriptorUI, M.TreeNumber from MeshC M, HGVD H where M.DescriptorUI = H.DescriptorUI limit 5000) as t2 where t1.DescriptorUI = t2.DescriptorUI GROUP BY RSID having count(*)>1;


select * from MeshC where DescriptorUI='D003376'


select TreeNumber from MeshC
    -> INNER JOIN HGVD ON HGVD.DescriptorUI = MeshC.DescriptorUI
    -> where HGVD.DescriptorUI IN(select DISTINCT RSID, PMID from HGVD) limit 500;

######
select H.DescriptorUI, M.TreeNumber from   HGVD H, MeshC M where  H.DescriptorUI = M.DescriptorUI group by H.RSID, H.PMID limit 5;

select RSID, PMID, DescriptorUI from HGVD where DescriptorUI='D010300' limit 5;

select H.DescriptorUI, H.RSID, H.PMID, M.TreeNumber from HGVD H, MeshC M where  H.DescriptorUI = M.DescriptorUI group by H.RSID,H.PMID





